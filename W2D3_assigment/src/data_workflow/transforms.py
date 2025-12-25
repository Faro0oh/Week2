import pandas as pd


def parse_datetime(df: pd.DataFrame, col: str, *, utc: bool = True, warn_threshold: float = 0.05) -> pd.DataFrame:
    s = df[col]
    parsed = pd.to_datetime(s, errors="coerce", utc=utc)
    fail_rate = parsed.isna().mean()

    if fail_rate > warn_threshold:
        print(
            f"Warning: {fail_rate:.2%} of values in column {col} "
            "could not be parsed as datetimes"
        )

    return df.assign(**{col: parsed})


def add_time_parts(df: pd.DataFrame, ts_col: str) -> pd.DataFrame:
    ts = df[ts_col]
    return df.assign(
        **{
            f"{ts_col}_year": ts.dt.year,
            f"{ts_col}_month": ts.dt.month,
            f"{ts_col}_day": ts.dt.day,
            f"{ts_col}_hour": ts.dt.hour,
            f"{ts_col}_minute": ts.dt.minute,
            f"{ts_col}_second": ts.dt.second,
            f"{ts_col}_dayofweek": ts.dt.dayofweek,
            f"{ts_col}_is_weekend": ts.dt.dayofweek >= 5,
        }
    )


def iqr_bounds(s: pd.Series, k: float = 1.5) -> tuple[float, float]:
    s = pd.to_numeric(s, errors="coerce")
    s = s.dropna()

    if s.empty:
        return (float("nan"), float("nan"))

    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper


def winsorize(s: pd.Series, lo: float = 0.01, hi: float = 0.99) -> pd.Series:
    s_num = pd.to_numeric(s, errors="coerce")
    non_na = s_num.dropna()

    if non_na.empty:
        return s_num

    low_q = non_na.quantile(lo)
    high_q = non_na.quantile(hi)

    return s_num.clip(lower=low_q, upper=high_q)


def add_outlier_flag(df: pd.DataFrame, col: str, *, k: float = 1.5) -> pd.DataFrame:
    s = pd.to_numeric(df[col], errors="coerce")
    low, high = iqr_bounds(s, k)

    if pd.isna(low) or pd.isna(high):
        mask = pd.Series(False, index=df.index)
    else:
        mask = (s < low) | (s > high)

    return df.assign(**{f"{col}_outlier": mask})
