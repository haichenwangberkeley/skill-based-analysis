# Skill-Based Analysis Repository

This repository contains a config-driven HEP analysis framework focused on an ATLAS Open Data diphoton workflow (`H -> gammagamma`) with:

- executable region/category definitions
- full sample processing from ROOT ntuples
- template production, fitting, and significance
- blinded SR/CR visualization
- publication-style report generation

## Repository Layout

- `analysis/`
  - main pipeline code and CLI (`python -m analysis.cli run`)
- `skills/`
  - workflow contracts and acceptance criteria (`skills/00_INDEX.md`)
- `input-data/`
  - open-data ROOT ntuples (`data/`, `MC/`)
- `outputs*/`
  - generated run artifacts
- `reports/`
  - final markdown reports
- `tests/`
  - parser/smoke/unit tests

Detailed package docs: [analysis/README.md](/global/homes/h/haichen/disk/skill-based-analysis/analysis/README.md)

## Environment Setup

```bash
python3.11 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install numpy pyyaml uproot awkward pyarrow pandas matplotlib pyhf pydantic pytest scipy
```

## Main Pipeline Command

```bash
. .venv/bin/activate
python -m analysis.cli run \
  --summary analysis/ATLAS_2012_H_to_gammagamma_discovery.analysis.json \
  --categories analysis/categories.yaml \
  --inputs input-data \
  --outputs <OUTPUT_DIR> \
  --all-samples
```

## Post-Processing Commands

Mass-model selection:

```bash
python -m analysis.stats.mass_model_selection \
  --fit-id FIT_MAIN \
  --summary <OUTPUT_DIR>/summary.normalized.json \
  --hists <OUTPUT_DIR>/hists \
  --strategy <OUTPUT_DIR>/background_modeling_strategy.json \
  --out <OUTPUT_DIR>/fit/FIT_MAIN/background_pdf_choice.json
```

Pipeline report:

```bash
python -m analysis.report.make_report \
  --summary <OUTPUT_DIR>/summary.normalized.json \
  --outputs <OUTPUT_DIR> \
  --out <OUTPUT_DIR>/report/report.md
```

Publication-style final report:

```bash
python -m analysis.report.final_report \
  --summary <OUTPUT_DIR>/summary.normalized.json \
  --outputs <OUTPUT_DIR> \
  --out reports/final_analysis_report_hgg_reference_20260305.md \
  --target-lumi-fb 36.1
```

Blinded region plots (CR shown, SR hidden):

```bash
python -m analysis.plotting.blinded_regions \
  --outputs <OUTPUT_DIR> \
  --registry <OUTPUT_DIR>/samples.registry.json \
  --regions analysis/regions.yaml \
  --fit-id FIT_MAIN
```

## How This Framework Was Run Here (2026-03-05)

1. Full all-samples pipeline run:

```bash
. .venv/bin/activate
python -m analysis.cli run \
  --summary analysis/ATLAS_2012_H_to_gammagamma_discovery.analysis.json \
  --categories analysis/categories.yaml \
  --inputs input-data \
  --outputs outputs_hgg_reference_20260305T173042Z \
  --all-samples
```

2. Mass-model selection and final report generation:

```bash
python -m analysis.stats.mass_model_selection \
  --fit-id FIT_MAIN \
  --summary outputs_hgg_reference_20260305T173042Z/summary.normalized.json \
  --hists outputs_hgg_reference_20260305T173042Z/hists \
  --strategy outputs_hgg_reference_20260305T173042Z/background_modeling_strategy.json \
  --out outputs_hgg_reference_20260305T173042Z/fit/FIT_MAIN/background_pdf_choice.json

python -m analysis.report.final_report \
  --summary outputs_hgg_reference_20260305T173042Z/summary.normalized.json \
  --outputs outputs_hgg_reference_20260305T173042Z \
  --out reports/final_analysis_report_hgg_reference_20260305.md \
  --target-lumi-fb 36.1
```

3. Sideband/control-plot fix and regeneration:

```bash
python -m analysis.plotting.blinded_regions \
  --outputs outputs_hgg_reference_20260305T173042Z \
  --registry outputs_hgg_reference_20260305T173042Z/samples.registry.json \
  --regions analysis/regions.yaml \
  --fit-id FIT_MAIN

python -m analysis.report.make_report \
  --summary outputs_hgg_reference_20260305T173042Z/summary.normalized.json \
  --outputs outputs_hgg_reference_20260305T173042Z \
  --out outputs_hgg_reference_20260305T173042Z/report/report.md
```

4. Tests:

```bash
PYTHONPATH=. pytest -q
```

Result in this workspace: `8 passed`.

## Latest Output Pointer

The latest full output directory is tracked in:

- [latest_hgg_reference_outdir.txt](/global/homes/h/haichen/disk/skill-based-analysis/reports/latest_hgg_reference_outdir.txt)

Current value:

- `outputs_hgg_reference_20260305T173042Z`
