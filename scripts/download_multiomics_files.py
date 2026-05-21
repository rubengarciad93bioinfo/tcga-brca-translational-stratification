from pathlib import Path
import requests

BASE_URL = "https://github.com/cBioPortal/datahub/raw/refs/heads/master/public/brca_tcga_pan_can_atlas_2018"

FILES = {
    "mutations": "data_mutations.txt",
    "cna_thresholded": "data_cna.txt",
}

OUTDIR = Path("data/raw/cbioportal_brca_multiomics")
OUTDIR.mkdir(parents=True, exist_ok=True)


def download_file(filename: str) -> None:
    url = f"{BASE_URL}/{filename}"
    outpath = OUTDIR / filename

    if outpath.exists() and outpath.stat().st_size > 1000:
        size_mb = outpath.stat().st_size / 1024 / 1024
        print(f"Skipping {filename}; already exists ({size_mb:.2f} MB)")
        return

    print(f"\nDownloading {filename}")
    print(url)

    with requests.get(url, stream=True, timeout=300, allow_redirects=True) as response:
        print("Status:", response.status_code)
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")
        print("Content-Type:", content_type)

        with open(outpath, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

    size_mb = outpath.stat().st_size / 1024 / 1024
    print(f"Saved to {outpath} ({size_mb:.2f} MB)")

    # Basic sanity check: avoid saving an HTML error page by mistake
    with open(outpath, "rb") as f:
        preview = f.read(200).decode("utf-8", errors="ignore")

    if preview.lstrip().startswith("<!DOCTYPE html") or preview.lstrip().startswith("<html"):
        raise RuntimeError(
            f"{filename} looks like an HTML page, not a data file. "
            "Delete it and retry with another URL."
        )


def main() -> None:
    for filename in FILES.values():
        download_file(filename)

    print("\nDone.")
    print(f"Files saved in: {OUTDIR}")


if __name__ == "__main__":
    main()