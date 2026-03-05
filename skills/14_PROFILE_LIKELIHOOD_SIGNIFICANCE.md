# Skill: Profile Likelihood Discovery Significance

## Layer 1 — Physics Policy
Discovery significance is computed with a profile-likelihood-ratio test comparing background-only and unconstrained fits.

Policy requirements:
- perform a conditional fit with signal strength fixed to the background-only hypothesis (`mu = 0`)
- perform an unconditional fit where signal strength is free
- construct the one-sided discovery test statistic

Test statistic definition:
`q0 = -2 ln lambda(0) = 2 * (NLL_mu0 - NLL_muhat)`

One-sided discovery convention:
- `q0 = max(q0, 0)`

Asymptotic significance:
- `Z = sqrt(q0)`

## Layer 2 — Workflow Contract
### Required Artifacts
- per-fit significance artifact containing fit identifiers, POI metadata, NLL values, test statistic, significance, and status diagnostics

### Acceptance Checks
- significance artifact exists for each fit under test
- successful result satisfies `q0 >= 0`
- successful result satisfies `z_discovery = sqrt(q0)` within numerical tolerance
- failed result includes actionable diagnostic information

## Layer 3 — Example Implementation
### Required Fields (Current Repository)
- `fit_id`
- `status`
- `poi_name`
- `mu_hat`
- `twice_nll_mu0`
- `twice_nll_free`
- `q0`
- `z_discovery`
- `error` (if failed)

### CLI (Current Repository)
`python -m analysis.stats.significance --workspace outputs/fit/workspace.json --fit-id FIT1 --out outputs/fit/FIT1/significance.json`
