# Skill: Plotting and Report

## Layer 1 — Physics Policy
Result communication must make agreement and discrepancies between data and expectations auditable.

Policy requirements:
- provide region-level observable visualizations with consistent binning and axis semantics
- include cut flow summaries and fit summaries in the final narrative
- include signal/background modeling rationale and uncertainty context
- include blinding policy behavior when the analysis is blinded

## Layer 2 — Workflow Contract
### Required Artifacts
- region-plot artifact set for fit observables
- cut-flow visualization artifact
- narrative report artifact integrating methodology, yields, fit outcomes, significance, and key diagnostics
- artifact-link inventory enabling traceability from report statements to produced artifacts

### Acceptance Checks
- at least one observable plot exists for each fit region
- report includes event-selection summary, cut flow summary, and fit result summary
- report includes significance summary when significance artifacts exist
- report includes blinding summary when blinding artifacts exist

## Layer 3 — Example Implementation
### Report Inputs (Current Repository)
- `outputs/background_modeling_strategy.json`
- `outputs/fit/*/signal_pdf.json`
- `outputs/fit/*/background_pdf_choice.json`
- `outputs/fit/*/spurious_signal.json`
- `outputs/report/blinding_summary.json`
- `outputs/fit/*/blinded_cr_fit.json`
- `outputs/fit/*/results.json`
- `outputs/fit/*/significance.json`

### CLI (Current Repository)
`python -m analysis.report.make_report --summary outputs/summary.normalized.json --outputs outputs --out outputs/report/report.md`

### Downstream Reference
Use:
- `17_CONTROL_REGION_SIGNAL_REGION_BLINDING_AND_VISUALIZATION.md`
- `19_FINAL_ANALYSIS_REPORT_AGENT_WORKFLOW.md`
