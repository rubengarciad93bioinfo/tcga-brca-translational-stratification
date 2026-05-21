from pathlib import Path
import shutil

PROJECT_ROOT = Path(__file__).resolve().parents[1]

FIGURES_DIR = PROJECT_ROOT / "results" / "figures"
DOCS_ASSETS_DIR = PROJECT_ROOT / "docs" / "assets"
SELECTED_DIR = PROJECT_ROOT / "results" / "selected_figures"

DOCS_ASSETS_DIR.mkdir(parents=True, exist_ok=True)
SELECTED_DIR.mkdir(parents=True, exist_ok=True)

FIGURE_MAP = {
    # 03 — transcriptomic structure
    "pca_pc1_pc2_by_subtype.png": "01_pca_by_subtype.png",

    # 04 — subtype signatures
    "subtype_signature_gene_heatmap.png": "02_subtype_signature_heatmap.png",

    # 06 — multi-omic driver alterations
    "selected_specific_alteration_frequency_by_subtype_heatmap.png": "03_driver_alterations_by_subtype.png",

    # 07 — genotype-expression integration
    "ERBB2_expression_by_ERBB2_amplification.png": "04_erbb2_amp_expression.png",
    "ERBB2_expression_by_subtype_and_amplification.png": "05_erbb2_subtype_amp_expression.png",

    # 09 — exploratory discovery
    "driver_associated_expression_effects_heatmap.png": "06_driver_associated_expression_heatmap.png",
    "subtype_adjusted_module_event_associations_heatmap.png": "07_module_event_associations.png",

    # 08 — optional clinical outcome
    "overall_survival_by_subtype.png": "08_overall_survival_by_subtype.png",
    # 10 — ex-vivo model matching
    "depmap_breast_models_tcga_subtype_similarity_heatmap.png": "09_depmap_model_matching_heatmap.png",
    "depmap_top_matches_marker_sanity_check.png": "10_depmap_marker_sanity_check.png",
    # 10 — sample-level ex-vivo model matching
    "sample_level_depmap_model_matching_frequency_by_subtype.png": "11_sample_level_model_frequency_by_subtype.png",
    "sample_level_best_depmap_similarity_by_subtype.png": "12_sample_level_best_similarity_by_subtype.png",
}

missing = []

for src_name, dst_name in FIGURE_MAP.items():
    src = FIGURES_DIR / src_name

    if not src.exists():
        missing.append(src_name)
        continue

    for outdir in [DOCS_ASSETS_DIR, SELECTED_DIR]:
        dst = outdir / dst_name
        shutil.copy2(src, dst)
        print(f"Copied {src_name} -> {dst}")

if missing:
    print("\nMissing figures:")
    for name in missing:
        print(f"  - {name}")

print("\nDone.")