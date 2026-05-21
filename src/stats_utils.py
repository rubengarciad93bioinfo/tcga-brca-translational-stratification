import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu


def benjamini_hochberg(p_values):
    """
    Benjamini-Hochberg FDR correction.
    Returns adjusted p-values in the original order.
    """
    p_values = np.asarray(p_values, dtype=float)
    n = len(p_values)

    order = np.argsort(p_values)
    ranked_p = p_values[order]

    adjusted = ranked_p * n / (np.arange(1, n + 1))
    adjusted = np.minimum.accumulate(adjusted[::-1])[::-1]
    adjusted = np.clip(adjusted, 0, 1)

    adjusted_original_order = np.empty_like(adjusted)
    adjusted_original_order[order] = adjusted

    return adjusted_original_order


def differential_expression_mannwhitney(
    expression_log,
    metadata,
    group_col,
    group_a,
    group_b,
    min_abs_log2fc=0.0,
):
    """
    Exploratory differential expression using Mann-Whitney U test.

    Parameters
    ----------
    expression_log:
        DataFrame with samples as rows and genes as columns.
        Values should already be log-transformed.

    metadata:
        DataFrame with samples as rows and clinical/group annotations.

    group_col:
        Column containing group labels.

    group_a:
        First group. Positive log2FC means higher in group_a.

    group_b:
        Reference group.

    Returns
    -------
    DataFrame with gene-level statistics.
    """
    idx_a = metadata[group_col] == group_a
    idx_b = metadata[group_col] == group_b

    if idx_a.sum() == 0:
        raise ValueError(f"No samples found for group_a={group_a}")

    if idx_b.sum() == 0:
        raise ValueError(f"No samples found for group_b={group_b}")

    results = []

    for gene in expression_log.columns:
        values_a = expression_log.loc[idx_a, gene].dropna()
        values_b = expression_log.loc[idx_b, gene].dropna()

        if values_a.nunique() <= 1 and values_b.nunique() <= 1:
            continue

        median_a = values_a.median()
        median_b = values_b.median()
        mean_a = values_a.mean()
        mean_b = values_b.mean()

        log2fc = mean_a - mean_b

        try:
            stat, p_value = mannwhitneyu(
                values_a,
                values_b,
                alternative="two-sided"
            )
        except ValueError:
            stat = np.nan
            p_value = np.nan

        results.append(
            {
                "gene": gene,
                "group_a": group_a,
                "group_b": group_b,
                "n_a": len(values_a),
                "n_b": len(values_b),
                "mean_log2_group_a": mean_a,
                "mean_log2_group_b": mean_b,
                "median_log2_group_a": median_a,
                "median_log2_group_b": median_b,
                "log2fc_group_a_vs_group_b": log2fc,
                "p_value": p_value,
            }
        )

    results_df = pd.DataFrame(results)
    results_df = results_df.dropna(subset=["p_value"]).copy()

    results_df["fdr"] = benjamini_hochberg(results_df["p_value"].values)
    results_df["neg_log10_fdr"] = -np.log10(results_df["fdr"].clip(lower=1e-300))

    results_df["significant"] = (
        (results_df["fdr"] < 0.05)
        & (results_df["log2fc_group_a_vs_group_b"].abs() >= min_abs_log2fc)
    )

    results_df = results_df.sort_values(["fdr", "p_value"])

    return results_df