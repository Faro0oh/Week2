import numpy as np
import pandas as pd


def bootstrap_diff_means(w, u, n_boot=2000, seed=0):
    w_clean= pd.to_numeric(w, errors="coerce").dropna().to_numpy()
    u_clean= pd.to_numeric(u, errors="coerce").dropna().to_numpy()

    assert len(w_clean) > 0 and len(u_clean) > 0, "the groups is empty after cleaning"

    rng = np.random.default_rng(seed)
    diffs = []

    for _ in range(n_boot):
        w_sam = rng.choice(w_clean, size=len(w_clean), replace=True)
        u_sam = rng.choice(u_clean, size=len(u_clean), replace=True)
        diffs.append(w_sam.mean() - u_sam.mean())

    diffs= np.array(diffs)

    return{
        "difference_mean":float(w_clean.mean() - u_clean.mean()),
        "ci_low":float(np.quantile(diffs, 0.025)),
        "ci_high":float(np.quantile(diffs, 0.975)),
    }

df["signup_year"] = pd.to_datetime(df["signup_date"], errors="coerce").dt.year

cohort_avg = (
    df.groupby("signup_year", dropna=False)["amount_wins"]
      .mean()
      .reset_index()
      .sort_values("amount_wins", ascending=False)
)

cohort_avg