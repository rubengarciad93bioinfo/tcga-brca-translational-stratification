from pathlib import Path
import pandas as pd


def read_cbioportal_table(path: str | Path) -> pd.DataFrame:
    """
    Read a cBioPortal tab-separated file.

    cBioPortal files often contain metadata/comment lines starting with '#'.
    This function skips them and returns a pandas DataFrame.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    return pd.read_csv(path, sep="\t", comment="#", low_memory=False)


def harmonize_tcga_sample_id(sample_id: str, n: int = 15) -> str:
    """
    Harmonize TCGA sample IDs.

    TCGA sample barcodes often contain multiple fields.
    n=15 keeps the sample-level barcode, e.g. TCGA-XX-YYYY-01.
    n=12 keeps the patient-level barcode, e.g. TCGA-XX-YYYY.
    """
    if pd.isna(sample_id):
        return sample_id

    return str(sample_id).strip()[:n]


def harmonize_tcga_patient_id(sample_id: str) -> str:
    """
    Extract patient-level TCGA barcode.
    """
    return harmonize_tcga_sample_id(sample_id, n=12)


def find_columns_containing(df: pd.DataFrame, keywords: list[str]) -> list[str]:
    """
    Return columns containing any of the provided keywords.
    Case-insensitive.
    """
    matches = []

    for col in df.columns:
        col_upper = col.upper()
        if any(keyword.upper() in col_upper for keyword in keywords):
            matches.append(col)

    return matches


def clean_expression_matrix(expression: pd.DataFrame) -> pd.DataFrame:
    """
    Clean cBioPortal mRNA expression table.

    Expected format:
    - rows: genes
    - columns: samples
    - first columns usually include Hugo_Symbol and Entrez_Gene_Id

    Returns:
    - rows: samples
    - columns: genes
    """
    expression = expression.copy()

    if "Hugo_Symbol" not in expression.columns:
        raise ValueError("Expected column 'Hugo_Symbol' not found in expression table.")

    # Remove genes with missing symbols
    expression = expression.dropna(subset=["Hugo_Symbol"])

    # Keep only gene symbol + sample columns
    metadata_cols = [col for col in ["Hugo_Symbol", "Entrez_Gene_Id"] if col in expression.columns]
    sample_cols = [col for col in expression.columns if col not in metadata_cols]

    expression_values = expression[["Hugo_Symbol"] + sample_cols].copy()

    # Convert expression values to numeric
    for col in sample_cols:
        expression_values[col] = pd.to_numeric(expression_values[col], errors="coerce")

    # If duplicated gene symbols exist, average them
    expression_values = expression_values.groupby("Hugo_Symbol", as_index=True).mean(numeric_only=True)

    # Transpose: samples x genes
    expression_samples = expression_values.T
    expression_samples.index.name = "SAMPLE_ID"

    return expression_samples