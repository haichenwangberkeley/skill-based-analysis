# Skill: Workspace and Fit (pyhf)

## Layer 1 — Physics Policy
Statistical inference must map selected regions, signal/background models, and nuisance parameters into a likelihood model with explicit parameters of interest.

Policy requirements:
- each fit configuration defines channels, samples, POIs, and nuisance terms
- control-region information may constrain signal-region background normalizations when correlations are defined
- analytic mass-shape choices (when used) must feed the final statistical model consistently
- fit diagnostics and parameter estimates must be preserved for interpretation

## Layer 2 — Workflow Contract
### Required Artifacts
- statistical-workspace artifact per fit configuration
- fit-result artifact containing best-fit POI estimates, uncertainties, status, and diagnostics
- fit-configuration hash/provenance artifact to ensure reproducibility of the model setup

### Acceptance Checks
- workspace artifact loads successfully in the chosen inference backend
- fit execution completes with converged status or actionable diagnostics
- POI estimates and uncertainties are present when fit succeeds
- model provenance metadata is attached to fit results

## Layer 3 — Example Implementation
### Mapping (Current Repository)
A fit configuration maps to:
- channels: included regions
- samples: signal/background/data
- POIs: parameters of interest
- nuisances: from systematics artifact
- CR/SR correlations: from constraint-map artifact when available
- analytic mass-model choice: from signal/background PDF artifacts when available

### CLI (Current Repository)
`python -m analysis.stats.fit --workspace outputs/fit/workspace.json --fit-id FIT1 --out outputs/fit/FIT1/results.json`

### Downstream Reference
After this skill, run:
- `14_PROFILE_LIKELIHOOD_SIGNIFICANCE.md`
