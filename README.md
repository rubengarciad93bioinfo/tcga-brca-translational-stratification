# TCGA-BRCA Multi-omic Translational Stratification

A computational biology portfolio project exploring breast cancer molecular heterogeneity using public TCGA-BRCA data.

The project integrates:

- RNA-seq expression
- clinical metadata
- molecular subtype annotations
- mutation data
- copy-number alteration data
- survival/progression metadata

## Portfolio case study

The curated visual case study is available here:

[Open the portfolio case study](docs/index.html)

## Summary

This project builds a reproducible workflow to explore patient stratification, subtype-associated driver alterations and genotype-expression relationships in breast cancer.

Main analyses include:

1. RNA-seq preprocessing and marker gene exploration
2. Transcriptomic patient stratification
3. Differential expression by molecular subtype
4. Mutation and copy-number alteration analysis
5. Genotype-expression integration
6. Clinical outcome exploration
7. Subtype-adjusted exploratory multi-omic discovery

## Repository structure

```text
notebooks/   Full analysis notebooks
scripts/     Data download and portfolio preparation scripts
src/         Utility functions
results/     Generated figures and tables
reports/     Interpretative summaries
docs/        Curated visual portfolio case study
```

## Reproducibility

Install dependencies:

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt