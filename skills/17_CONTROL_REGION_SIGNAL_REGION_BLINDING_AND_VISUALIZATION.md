# Skill: Control/Signal Region Blinding and Visualization

## Layer 1 — Physics Policy
Blinding protects against analysis bias by preventing inspection of signal-region data during model development and validation.

Policy requirements:
- control-region visualizations may show observed data and modeled expectations
- signal-region visualizations must hide observed data during blinded operation
- signal expectation must be stacked on top of background expectation in region plots
- normalization used for expected region plots should be derived from control-region-only fitting when blinding is active
- control and signal region selections must be mutually exclusive for blinded workflows unless an explicit overlap exception is documented
- unblinding is an explicit, deliberate action outside the default workflow

## Layer 2 — Workflow Contract
### Required Artifacts
- control-region-only normalization-fit artifact containing fitted normalization parameters and fit status
- blinding-summary artifact indicating region classification and whether data were shown or hidden
- region-visualization artifact set covering all declared control and signal regions
- blinding overlap-audit artifact confirming SR events are excluded from CR normalization scope by default

### Acceptance Checks
- normalization-fit artifact confirms control-region-only fit scope
- blinding-summary artifact marks signal regions as data hidden during blinded operation
- number of produced region plots equals number of declared regions
- stacked composition places signal above background in expectation plots
- overlap audit confirms zero SR/CR overlap for blinded normalization unless an explicit exception is declared

## Layer 3 — Example Implementation
### CLI (Current Repository)
Blinded (default):
`python -m analysis.plotting.blinded_regions --outputs outputs --registry outputs/samples.registry.json --regions analysis/regions.yaml --fit-id FIT1`

Explicit unblind:
`python -m analysis.plotting.blinded_regions --outputs outputs --registry outputs/samples.registry.json --regions analysis/regions.yaml --fit-id FIT1 --unblind-sr`

### Expected Outputs (Current Repository)
- `outputs/fit/<fit_id>/blinded_cr_fit.json`
- `outputs/report/blinding_summary.json`
- `outputs/report/plots/blinded_region_<region_id>.png`

### Downstream Reference
Use with:
- `11_PLOTTING_AND_REPORT.md`
- `13_VISUAL_VERIFICATION.md`
