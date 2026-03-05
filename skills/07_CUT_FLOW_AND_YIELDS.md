# Skill: Cut Flow and Yields

## Layer 1 — Physics Policy
A cut flow must describe event reduction step-by-step and preserve both unweighted and weighted interpretations.

Policy requirements:
- cut flow is ordered and physically meaningful
- each step reports unweighted counts and weighted yields
- report per-step and cumulative efficiencies
- final selected yield must match the sample contribution used in downstream histogramming

## Layer 2 — Workflow Contract
### Required Artifacts
- cut-flow table artifact per sample with ordered step metrics
- region-yield artifact per sample with unweighted counts, weighted yields, and uncertainty proxy terms (for example sum of squared weights)
- cut-flow provenance artifact linking steps to region definitions

### Acceptance Checks
- cut-flow steps are ordered and complete
- unweighted event counts do not increase across stricter sequential cuts
- final cut-flow selection agrees with region-yield selection used downstream
- weighted yields and uncertainty proxies are finite and reported

## Layer 3 — Example Implementation
### Output Schema (Current Repository)
Cut flow entries:
- `name`, `n_raw`, `n_weighted`, `eff_step`, `eff_cum`

Yield entries:
- `n_raw`, `yield`, `sumw2`

### CLI (Current Repository)
`python -m analysis.selections.engine --sample <ID> --registry outputs/samples.registry.json --regions analysis/regions.yaml --cutflow --out outputs/cutflows/<ID>.json`
