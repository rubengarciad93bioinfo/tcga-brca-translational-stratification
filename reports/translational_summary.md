# Translational Summary — TCGA-BRCA Multi-omic Stratification

## Objective

This project explores breast cancer molecular heterogeneity using public TCGA-BRCA data. The goal is to build a reproducible multi-omic workflow integrating RNA-seq, subtype annotations, mutation data, copy-number alterations and clinical metadata.

The analysis is designed as a computational biology portfolio case study for translational oncology and bioinformatics roles.

## Dataset

The project uses TCGA-BRCA breast invasive carcinoma data from cBioPortal/GDC-derived resources.

Data layers:

- RNA-seq expression
- Clinical metadata
- Molecular subtype annotations
- Mutation data
- Thresholded copy-number alteration data
- Survival/progression metadata where available

## Analytical workflow

1. Data loading and preprocessing
2. Marker gene exploration
3. Global transcriptomic stratification
4. Differential expression by subtype
5. Supervised subtype prediction baseline
6. Driver alteration analysis by subtype
7. Genotype-expression integration
8. Clinical outcome exploration
9. Subtype-adjusted exploratory discovery

## Key findings

### 1. Transcriptomic structure captures subtype-associated biology

Global expression profiles partially separate TCGA-BRCA molecular subtypes. Basal-like tumours show the clearest separation, while Luminal A, Luminal B and HER2-enriched samples show partial overlap.

### 2. Marker and differential-expression analyses recover expected breast cancer biology

Known luminal markers such as ESR1, PGR, FOXA1 and GATA3 are higher in luminal subtypes. ERBB2 is elevated in HER2-enriched samples, and proliferation-associated markers are higher in more aggressive/proliferative contexts.

### 3. Driver alterations are subtype-associated

Multi-omic integration revealed clear subtype-specific alteration patterns:

- Basal-like tumours are strongly enriched for TP53 mutation.
- HER2-enriched tumours are strongly enriched for ERBB2 amplification.
- Luminal A tumours show higher frequencies of PIK3CA, CDH1 and MAP3K1 mutations.
- Luminal B shows an intermediate molecular profile with stronger proliferative and copy-number-associated features.

### 4. Copy-number alterations show transcriptomic consequences

ERBB2 amplification is strongly associated with higher ERBB2 expression. CCND1 amplification, MYC amplification and PTEN deletion also show expected expression-level effects.

Subtype-adjusted models indicate that several alteration-expression associations remain significant after accounting for molecular subtype, while others appear largely subtype-driven.

### 5. Clinical associations are exploratory

Overall survival, defined as time until death or last follow-up, showed an exploratory association with subtype. Progression-free survival, defined as time until progression, recurrence or last follow-up, showed weaker differences across subtypes.

### 6. Discovery analyses generate hypotheses, not validated biomarkers

Subtype-adjusted CNA-expression scans and driver-associated transcriptome scans identified candidate dosage-sensitive genes and expression programs. These findings require external validation and should not be interpreted as causal or clinically actionable.

## Patient stratification interpretation

Molecular subtype was used as the initial stratification layer. Mutation, copy-number and expression data were then integrated to describe what makes each tumour group biologically distinct.

- Basal-like tumours showed high TP53 mutation frequency, together with additional MYC amplification and PTEN/RB1 loss signals, supporting a more proliferative and genomically altered profile.
- HER2-enriched tumours showed frequent ERBB2 amplification and high ERBB2 expression, linking subtype identity to a concrete genomic event and transcriptomic readout.
- Luminal A tumours showed higher PIK3CA, CDH1 and MAP3K1 mutation frequencies and comparatively lower TP53 mutation frequency.
- Luminal B retained luminal identity but showed stronger proliferative and copy-number-associated features than Luminal A.
- Normal-like samples were retained as an annotated subtype but interpreted cautiously due to sample size and possible tissue-composition effects.

This stratification is exploratory and should be interpreted as a molecular characterization workflow rather than a clinically validated decision tool.

## Translational relevance

This workflow demonstrates how public multi-omic cancer datasets can be used to:

- characterize disease heterogeneity;
- connect transcriptomic subtypes with genomic drivers;
- identify alteration-expression relationships;
- generate biomarker and mechanism hypotheses;
- communicate results in a decision-oriented translational format.

## Limitations

- TCGA is retrospective and not designed as a controlled clinical trial.
- Treatment and response data are limited.
- Molecular subtype labels are partly expression-derived.
- Copy-number events may span broad genomic regions, so gene-level effects require regional interpretation.
- Discovery analyses are exploratory and require independent validation.

## Suggested next steps

1. Map CNA-expression discovery hits to genomic coordinates to distinguish focal events from broad amplicons.
2. Perform pathway or gene-set enrichment on driver-associated expression signatures.
3. Validate candidate signatures in an independent breast cancer cohort.
4. Integrate breast cancer cell line or organoid datasets from DepMap/CCLE to identify ex-vivo models representing key TCGA-BRCA molecular subtypes.