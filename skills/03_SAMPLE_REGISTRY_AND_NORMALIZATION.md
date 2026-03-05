# Skill: Sample Registry and Normalization

## Layer 1 — Physics Policy
Each sample must be mapped to a physics process and classified as data, signal, or background with an explicit normalization convention.

Policy requirements:
- preserve process identity and sample provenance
- distinguish data from simulated samples
- apply a consistent MC normalization based on cross section, correction factors, luminosity, and generator-weight sum
- record missing normalization inputs explicitly rather than silently assuming values

Normalization convention for simulated samples:
`w_norm = (xsec_pb * k_factor * filter_eff * lumi_fb * 1000.0) / sumw`

## Layer 2 — Workflow Contract
### Required Artifacts
- sample-registry artifact containing sample identity, process mapping, classification, and normalization inputs
- normalization-expression artifact describing how per-event weights are formed
- normalization-audit artifact listing missing inputs and warnings

### Acceptance Checks
- every registered sample has exactly one classification among data, signal, background
- each sample contains process identity and source-file linkage
- normalization terms are present or explicitly marked as not specified
- normalization value is computable when all required terms are available

## Layer 3 — Example Implementation
### Registry Fields (Current Repository)
For each sample:
- `sample_id`
- `process_name`
- `kind`: `data | signal | background`
- `files`
- `xsec_pb`
- `k_factor`
- `filter_eff`
- `sumw`
- `lumi_fb`
- `weight_expr`

### CLI (Current Repository)
`python -m analysis.samples.registry --inputs inputs/ --summary analysis/analysis.summary.json --out outputs/samples.registry.json`

### Downstream Reference
After this skill, run:
- `18_MC_NORMALIZATION_METADATA_STACKING.md` for metadata.csv-driven normalization of multi-sample MC stacks in ATLAS Open Data workflows
- `15_SIGNAL_BACKGROUND_STRATEGY_AND_CR_CONSTRAINTS.md`
