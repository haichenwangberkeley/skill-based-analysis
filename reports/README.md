# Reports README

This folder contains final, publication-style summaries for the diphoton analysis runs in this repository.

## Main Files

- `final_analysis_report_hgg_reference_20260305.md`
  - Latest full-statistics final report for the reference-aligned H->gammagamma workflow.
- `final_analysis_report_fullstat_20260305.md`
  - Earlier full-stat report snapshot.
- `final_analysis_report.md`
  - Baseline report from an earlier pipeline state.
- `latest_hgg_reference_outdir.txt`
  - Pointer to the most recent full output directory.

## Latest Output Directory

Current value in `latest_hgg_reference_outdir.txt`:

- `outputs_hgg_reference_20260305T173042Z`

Important artifacts inside that directory:

- `report/report.md`
- `report/blinding_summary.json`
- `report/plots/blinded_region_*.png`
- `fit/FIT_MAIN/results.json`
- `fit/FIT_MAIN/significance.json`
- `fit/FIT_MAIN/significance_asimov.json`

## Regeneration Commands

From repository root:

```bash
. .venv/bin/activate
OUT=$(cat reports/latest_hgg_reference_outdir.txt)

# Rebuild blinded region plots (SR blinded, CR shown)
python -m analysis.plotting.blinded_regions \
  --outputs "$OUT" \
  --registry "$OUT/samples.registry.json" \
  --regions analysis/regions.yaml \
  --fit-id FIT_MAIN

# Rebuild pipeline report
python -m analysis.report.make_report \
  --summary "$OUT/summary.normalized.json" \
  --outputs "$OUT" \
  --out "$OUT/report/report.md"

# Rebuild publication-style final report
python -m analysis.report.final_report \
  --summary "$OUT/summary.normalized.json" \
  --outputs "$OUT" \
  --out reports/final_analysis_report_hgg_reference_20260305.md \
  --target-lumi-fb 36.1
```

## Note on Blinded Sideband Plots

Control-region sideband plots now include observed data points.
Signal-region plots remain blinded by default.
