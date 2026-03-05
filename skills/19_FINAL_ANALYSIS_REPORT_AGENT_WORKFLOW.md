# Skill: Final Analysis Report (ATLAS Open Data Agent Workflow)

## Layer 1 — Physics Policy
The final analysis report must communicate the physics analysis in a concise note-style format while preserving transparency of agent decisions.

Policy requirements:
- follow the user-defined analysis goal; do not invent new physics objectives
- document the studied process, discriminating observable, and tested hypothesis
- describe data and simulated samples, including integrated luminosity and run period
- report Monte Carlo normalization based on cross section, k-factor, filter efficiency, and signed generator-weight sum
- define reconstructed objects and event selections using available dataset observables
- document signal and control region purposes and selection logic
- preserve blinding by hiding signal-region data before unblinding
- describe the statistical interpretation framework and expected (pre-unblinding) results using Asimov-based fits when applicable
- avoid inventing systematic uncertainties when not provided; use explicit placeholder language instead
- include a mandatory appendix that documents all agent deviations, substitutions, and assumptions with justification

Normalization relation to state in report:
- `norm_factor = (sigma_pb * k_factor * filter_eff * lumi_pb) / sumw`
- `w_final = w_event * norm_factor`

## Layer 2 — Workflow Contract
### Required Artifacts
- final report artifact in Markdown with the following sections in order:
  1. Introduction
  2. Data and Monte Carlo Samples
  3. Object Definition and Event Selection
  4. Overview of the Analysis Strategy
  5. Signal and Control Regions
  6. Cut Flow
  7. Distributions in Signal and Control Regions
  8. Systematic Uncertainties
  9. Statistical Interpretation
  10. Summary
  Appendix A: Agent Decisions and Deviations
- Monte Carlo sample-table artifact within the report containing DSID, sample label, process, cross section, k-factor, and filter efficiency
- cut-flow table artifact with data counts and weighted simulated yields
- region-plot artifact references including blinded signal-region visualizations
- statistical-summary artifact reporting expected sensitivity outputs produced before unblinding
- agent-decision audit artifact in Appendix A with issue, decision, and justification for each deviation

### Acceptance Checks
- section headers exist and appear in required order
- report explicitly states metadata-driven MC normalization inputs and formula
- sample table includes required Monte Carlo normalization columns
- signal-region plots are marked/blinded with no overlaid data points
- systematics section contains explicit placeholder statement when systematics are unspecified
- statistical interpretation section documents Asimov/pre-unblinding treatment when blinding is active
- Appendix A exists and contains at least one structured entry whenever substitutions/deviations occurred

## Layer 3 — Example Implementation
### Output Location (Current Repository Workflow)
- `reports/final_analysis_report.md`

### Inputs to Reference (Current Repository Workflow)
- analysis summary specification
- region definitions
- metadata table for open-data sample normalization
- cut-flow, yield, fit, significance, and blinding artifacts produced by pipeline stages

### Related Skills
- `03_SAMPLE_REGISTRY_AND_NORMALIZATION.md`
- `18_MC_NORMALIZATION_METADATA_STACKING.md`
- `11_PLOTTING_AND_REPORT.md`
- `17_CONTROL_REGION_SIGNAL_REGION_BLINDING_AND_VISUALIZATION.md`
- `14_PROFILE_LIKELIHOOD_SIGNIFICANCE.md`

### Example Generation Path (Current Repository Workflow)
- generate a baseline report from pipeline report stage
- enrich/reshape to match this final section structure
- write final artifact to `reports/final_analysis_report.md`
