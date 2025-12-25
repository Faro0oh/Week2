import json
import logging
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd

from data_workflow.io import read_orders_csv, write_parquet
from data_workflow.joins import safe_left_join
from data_workflow.quality import require_columns, assert_unique_key
from data_workflow.transforms import (
    parse_datetime,
    add_time_parts,
    winsorize,
    add_outlier_flag,
)

log = logging.getLogger(__name__)


@dataclass(frozen=True)
class ETLConfig:
    root: Path
    raw_orders: Path
    raw_users: Path
    out_analytics: Path
    run_meta: Path


def load_inputs(cfg: ETLConfig):
    orders = read_orders_csv(cfg.raw_orders)
    users = pd.read_csv(cfg.raw_users, dtype={"user_id": "string"})
    return orders, users


def transform(orders: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    require_columns(orders, ["order_id", "user_id", "amount", "quantity", "created_at"])
    require_columns(users, ["user_id"])
    assert_unique_key(users, "user_id")

    orders = parse_datetime(orders, "created_at")
    orders = add_time_parts(orders, "created_at")
    orders["amount_wins"] = winsorize(orders["amount"])
    orders = add_outlier_flag(orders, "amount")

    joined = safe_left_join(orders, users, on="user_id")
    assert len(joined) == len(orders)

    return joined


def load_outputs(analytics: pd.DataFrame, cfg: ETLConfig):
    write_parquet(analytics, cfg.out_analytics)


def write_run_meta(cfg: ETLConfig, analytics: pd.DataFrame):
    meta = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "rows": int(len(analytics)),
        "missing_created_at": int(analytics["created_at"].isna().sum()),
        "config": {k: str(v) for k, v in asdict(cfg).items()},
    }

    cfg.run_meta.parent.mkdir(parents=True, exist_ok=True)
    cfg.run_meta.write_text(json.dumps(meta, indent=2), encoding="utf-8")


def run_etl(cfg: ETLConfig):
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    log.info("Loading inputs")
    orders, users = load_inputs(cfg)

    log.info("Transforming data")
    analytics = transform(orders, users)

    log.info("Writing outputs")
    load_outputs(analytics, cfg)

    log.info("Writing run metadata")
    write_run_meta(cfg, analytics)

    log.info("ETL complete: %s rows", len(analytics))
