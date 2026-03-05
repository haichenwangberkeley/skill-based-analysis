# Skill: Skills Pack Index

## Layer 1 — Physics Policy
The analysis skill pack must encode a complete, scientifically coherent HEP workflow from analysis definition to statistical interpretation.

Core policy requirements:
- Keep analysis decisions config-driven and reproducible.
- Preserve a clear chain from event selection through statistical inference.
- Treat signal and background modeling choices as explicit methodological choices.
- Enforce blinding where required by the analysis strategy.
- Require visual and statistical validation before declaring completion.
- Use the term **cut flow** consistently.

## Layer 2 — Workflow Contract
### Required Artifacts
- normalized analysis-definition artifact with validated region and fit semantics
- sample-classification and normalization artifact
- open-data metadata-driven normalization artifact for multi-component MC stacking (when this workflow is used)
- signal/background strategy artifact including control-to-signal normalization intent
- category/region partition specification artifact (category axis x region axis)
- partition completeness/exclusivity check artifact
- partition manifest artifact for downstream stages
- region-selection artifact with cut flow and yield summaries
- region-overlap audit artifact documenting SR/CR overlap checks and any explicit exceptions
- histogram-template artifact for fit observables
- signal-shape and background-model-selection artifacts when analytic mass modeling is used
- systematic-uncertainty artifact
- statistical-workspace artifact and per-fit result artifacts
- discovery-significance artifact per fit
- blinding-summary artifact and blinded region-visualization artifact set
- visual-verification artifact set for required diagnostics
- narrative analysis report artifact
- final publication-style report artifact with agent decision appendix

### Acceptance Checks
- all pipeline-stage artifacts exist and are readable by downstream stages
- each declared fit has a fit-result artifact and significance artifact
- region-level histograms, yields, and cut flows are mutually consistent within tolerance
- signal and control regions used together in a fit are mutually exclusive at event level unless an explicit, justified overlap exception is declared
- blinding metadata confirms signal-region data handling policy
- required verification plots are present
- final report summarizes selection, modeling, fit, significance, and implementation differences
- partition checks confirm category coverage/exclusivity and unique `(category, region)` keys

## Layer 3 — Example Implementation
### Required Inputs (Current Repository)
- Analysis summary JSON: `analysis/analysis.summary.json`
- Samples: `inputs/` (or a provided path)
- Output directory: `outputs/`

### Minimum Outputs (Current Repository)
- `outputs/cutflows/*.json`
- `outputs/yields/*.json`
- `outputs/hists/**/*.npz` (or ROOT, but be consistent)
- `outputs/fit/*/results.json`
- `outputs/fit/*/significance.json`
- `outputs/background_modeling_strategy.json`
- `outputs/samples.classification.json`
- `outputs/cr_sr_constraint_map.json`
- `outputs/report/partition_spec.json`
- `outputs/report/partition_checks.json`
- `outputs/manifest/partitions.json`
- `outputs/fit/*/signal_pdf.json`
- `outputs/fit/*/background_pdf_scan.json`
- `outputs/fit/*/background_pdf_choice.json`
- `outputs/fit/*/spurious_signal.json`
- `outputs/fit/*/blinded_cr_fit.json`
- `outputs/report/blinding_summary.json`
- `outputs/report/plots/blinded_region_*.png`
- `outputs/report/report.md`
- `outputs/report/*.png`

### Canonical Pipeline Stages (Current Repository)
1. Parse and validate summary JSON.
2. Build sample registry.
3. Build metadata-driven MC normalization factors for stacked components (when metadata workflow is used).
4. Build category/region partition specification, checks, and manifest.
5. Build signal/background strategy and CR/SR normalization map.
6. Ingest events.
7. Build objects.
8. Apply selections and region masks.
9. Produce cut flow and yields.
10. Produce histograms for fit observables.
11. Build signal/background mass-shape models and run spurious-signal model selection.
12. Build statistical model and run fits.
13. Compute discovery significance from profile likelihood ratio.
14. Produce blinded CR/SR visualization products.
15. Make plots and report.
16. Run smoke tests.

### Skill List (Current Repository)
Core pipeline skills:
- `01_BOOTSTRAP_REPO.md`
- `02_READ_SUMMARY_AND_VALIDATE.md`
- `03_SAMPLE_REGISTRY_AND_NORMALIZATION.md`
- `18_MC_NORMALIZATION_METADATA_STACKING.md`
- `15_SIGNAL_BACKGROUND_STRATEGY_AND_CR_CONSTRAINTS.md`
- `04_EVENT_IO_AND_COLUMNAR_MODEL.md`
- `05_OBJECT_DEFINITIONS.md`
- `06_SELECTION_ENGINE_AND_REGIONS.md`
- `07_CUT_FLOW_AND_YIELDS.md`
- `08_HISTOGRAMMING_AND_TEMPLATES.md`
- `16_SIGNAL_SHAPE_AND_SPURIOUS_SIGNAL_MODEL_SELECTION.md`
- `09_SYSTEMATICS_AND_NUISANCES.md`
- `10_WORKSPACE_AND_FIT_PYHF.md`
- `11_PLOTTING_AND_REPORT.md`
- `19_FINAL_ANALYSIS_REPORT_AGENT_WORKFLOW.md`
- `17_CONTROL_REGION_SIGNAL_REGION_BLINDING_AND_VISUALIZATION.md`
- `12_SMOKE_TESTS_AND_REPRODUCIBILITY.md`
- `14_PROFILE_LIKELIHOOD_SIGNIFICANCE.md`
- `20_CATEGORY_CHANNEL_REGION_PARTITIONING.md`

Verification skills:
- `13_VISUAL_VERIFICATION.md`
