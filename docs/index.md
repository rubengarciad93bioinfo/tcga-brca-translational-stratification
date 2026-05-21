# Multi-omic exploration of breast cancer molecular heterogeneity using TCGA-BRCA

## Overview

This project is a computational biology portfolio case study using public TCGA-BRCA breast cancer data.

The goal was to build a reproducible multi-omic workflow integrating:

- bulk RNA-seq expression
- molecular subtype annotations
- mutation data
- copy-number alteration data
- clinical metadata

The analysis focuses on breast cancer molecular heterogeneity, patient stratification, driver alteration patterns and genotype-expression integration.

This is an exploratory analysis. The results are intended to generate and communicate translational hypotheses, not to establish clinically validated biomarkers.

---

## Biological context

TCGA-BRCA contains breast invasive carcinoma samples. The analysis focuses on molecular subtypes such as:

- **Luminal A**: hormone receptor/luminal-like profile, typically higher ESR1, PGR, FOXA1 and GATA3.
- **Luminal B**: luminal profile with stronger proliferative features.
- **HER2-enriched**: associated with ERBB2/HER2 biology.
- **Basal-like**: transcriptionally distinct, often more proliferative and TP53-altered.
- **Normal-like**: retained as an annotated subtype, interpreted cautiously due to smaller sample size and possible normal-like tissue composition effects.

The objective is not cancer-vs-normal classification. Instead, the project explores heterogeneity among breast cancer samples.

---

## Workflow

```text
TCGA-BRCA public data
│
├── RNA-seq expression
├── Clinical metadata
├── Mutation data
└── Copy-number alteration data
        │
        ▼
Data harmonization and quality checks
        │
        ▼
Subtype marker validation
        │
        ▼
Transcriptomic stratification
        │
        ▼
Differential expression and subtype signatures
        │
        ▼
Driver alteration analysis by subtype
        │
        ▼
Genotype-expression integration
        │
        ▼
Subtype-adjusted exploratory discovery