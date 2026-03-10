---
skill_type: procedure
domain: hep_analysis
stage: fit
original_id: "33"
original_filename: "33_ASIMOV_EXPECTED_SIGNIFICANCE_SPLUSB.md"
---

# Skill: Asimov Expected Significance (S+B Generation)

## Layer 1 — Physics Policy
Expected discovery significance must use signal-plus-background Asimov pseudo-data with `mu_gen = 1`.

Policy requirements:
- determine background-PDF parameters from a fit where signal strength is fixed to background-only (`mu = 0`), typically using sidebands under blinding
- keep this parameter snapshot as the background-shape provenance for Asimov generation
- generate expected-significance Asimov pseudo-data from the full model with `mu_gen = 1` (signal plus background)
- do not conflate the background-shape fit hypothesis (`mu = 0`) with the Asimov generation hypothesis (`mu_gen = 1`)
- evaluate discovery `q0` on the generated Asimov dataset using the standard conditional (`mu = 0`) versus unconditional (free `mu`) fits
- for blinded resonance workflows, allow full-range generation/evaluation because Asimov datasets are pseudo-data
- label outputs as expected/Asimov and record both hypotheses in metadata

## Layer 2 — Workflow Contract
### Required Artifacts
- Asimov expected-significance artifact per fit with:
  - `dataset_type = "asimov"`
  - `generation_hypothesis = "signal_plus_background"`
  - `mu_gen = 1`
  - `background_parameter_source` describing the `mu = 0` data-fit snapshot used for background-PDF parameters
  - `fit_range` used for generation/evaluation
  - `q0` and `z_discovery`
- optional sideband/background-fit provenance artifact linking parameter values to the `mu = 0` fit used for shape determination

### Acceptance Checks
- expected-significance Asimov artifacts use `mu_gen = 1`
- artifact provenance explicitly records that background-PDF parameters came from a `mu = 0` data fit
- expected-significance claims in blinded mode do not rely on observed signal-region data
- Asimov generation/evaluation range for expected significance includes the signal region (full observable range) unless an explicit justified exception is documented
- expected (Asimov) and observed significance outputs are reported separately

## Layer 3 — Example Implementation
### Procedure
1. Fit real data to determine background-shape parameters with `mu` fixed to `0` (often sideband-constrained when blinded).
2. Snapshot those background parameters as the Asimov-generation baseline.
3. Set `mu_gen = 1` and generate Asimov pseudo-data from the S+B model over the full analysis range.
4. On this Asimov dataset, compute discovery significance with:
   - conditional fit at `mu = 0`
   - unconditional fit with free `mu`
   - `q0 = max(2 * (NLL_mu0 - NLL_free), 0)` and `Z = sqrt(q0)`
5. Save expected-significance output with explicit provenance of both:
   - background-shape fit hypothesis (`mu_fit_for_bkg = 0`)
   - Asimov generation hypothesis (`mu_gen = 1`)

### Related Skills
- `core_pipeline/profile_likelihood_significance.md`
- `core_pipeline/workspace_and_fit_pyhf.md`
- `core_pipeline/final_analysis_report_agent_workflow.md`
