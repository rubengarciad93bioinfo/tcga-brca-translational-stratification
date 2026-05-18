from pathlib import Path
import requests

BASE_URL = "https://media.githubusercontent.com/media/cBioPortal/datahub/master/public/brca_tcga_pan_can_atlas_2018"

FILES = {
    "clinical_patient": "data_clinical_patient.txt",
    "clinical_sample": "data_clinical_sample.txt",
    "expression_rsem": "data_mrna_seq_v2_rsem.txt",
}

OUTDIR = Path("data/raw/cbioportal_brca")
OUTDIR.mkdir(parents=True, exist_ok=True)


def download_file(filename: str) -> None:
    url = f"{BASE_URL}/{filename}"
    outpath = OUTDIR / filename

    print(f"Downloading {filename}...")
    response = requests.get(url, timeout=120)
    response.raise_for_status()

    text_start = response.content[:100].decode("utf-8", errors="ignore")
    if text_start.startswith("version https://git-lfs.github.com/spec"):
        raise RuntimeError(
            f"{filename} was downloaded as a Git LFS pointer, not as the real file. "
            "Try installing git-lfs or check the media.githubusercontent.com URL."
        )

    outpath.write_bytes(response.content)
    print(f"Saved to {outpath}")


def main() -> None:
    for filename in FILES.values():
        download_file(filename)

    print("\nDone.")
    print(f"Files saved in: {OUTDIR}")


if __name__ == "__main__":
    main()