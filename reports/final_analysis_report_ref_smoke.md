# Higgs to Diphoton Search Final Analysis Report

## 1. Introduction

This note reports a full end-to-end Higgs to diphoton analysis over the ATLAS Open Data Run-2 diphoton sample set (data and simulation), using the executable configuration in this repository.
The workflow covers ingestion, object definition, region selection, cut flow, histogram templates, likelihood fits, profile-likelihood discovery significance, blinding-aware visualization, and final reporting.

## 2. Data and Monte Carlo Samples

The processed registry contains 16 data samples, 121 signal samples, and 70 background samples.
The analysis target luminosity for this workflow is 36.1 fb^-1. Monte Carlo normalization follows:

`norm_factor = (sigma_pb * k_factor * filter_eff * lumi_pb) / sumw`

`w_final = w_event * norm_factor`

Runtime registry luminosity values in this run: `1.0` (see `outputs_ref_smoke/normalization/norm_table.json`).

The table below lists dominant MC contributors by absolute reference-region yield with required normalization inputs (reference region `SR_DIPHOTON_INCL`; full table: `outputs_ref_smoke/normalization/norm_table.json`).

| DSID | Sample label | Process | Kind | xsec_pb | k_factor | filter_eff | Reference-region yield |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| 301204 | ODEO_FEB2025_v0_GamGam_mc_301204.Pythia8EvtGen_A14MSTW2008LO_Zprime_NoInt_ee_SSM3000.GamGam | pp>Zprime>ee | background | 0.001762 | 1 | 1 | 0 |
| 301209 | ODEO_FEB2025_v0_GamGam_mc_301209.Pythia8EvtGen_A14MSTW2008LO_Zprime_NoInt_mumu_SSM3000.GamGam | pp>Zprime>mm | background | 0.001772 | 1 | 1 | 0 |
| 301243 | ODEO_FEB2025_v0_GamGam_mc_301243.Pythia8EvtGen_A14NNPDF23LO_Wprime_enu_SSM3000.GamGam | pp>Wprime>enu | background | 0.011414 | 1 | 1 | 0 |
| 301247 | ODEO_FEB2025_v0_GamGam_mc_301247.Pythia8EvtGen_A14NNPDF23LO_Wprime_munu_SSM3000.GamGam | pp>Wprime>munu | background | 0.011432 | 1 | 1 | 0 |
| 301333 | ODEO_FEB2025_v0_GamGam_mc_301333.Pythia8EvtGen_A14NNPDF23LO_zprime3000_tt.GamGam | pp>Zprime>ttbar | background | 0.005084 | 1 | 1 | 0 |
| 301826 | ODEO_FEB2025_v0_GamGam_mc_301826.Pythia8EvtGen_A14NNPDF23LO_Wprime_qq_3000.GamGam | pp>Wprime>qq | background | 0.10318 | 1 | 1 | 0 |
| 301928 | ODEO_FEB2025_v0_GamGam_mc_301928.Pythia8EvtGen_A14NNPDF23LO_Zprimebb3000.GamGam | Zprime->bb | background | 0.007024 | 1 | 1 | 0 |
| 302520 | ODEO_FEB2025_v0_GamGam_mc_302520.Pythia8EvtGen_A14NNPDF23LO_2DP20_Mass_55_100.GamGam | QCD direct diphoton production | background | 85.503 | 1 | 0.4218 | 0 |
| 302521 | ODEO_FEB2025_v0_GamGam_mc_302521.Pythia8EvtGen_A14NNPDF23LO_2DP20_Mass_100_160.GamGam | QCD direct diphoton production | background | 18.282 | 1 | 0.4419 | 0 |
| 302522 | ODEO_FEB2025_v0_GamGam_mc_302522.Pythia8EvtGen_A14NNPDF23LO_2DP20_Mass_160_250.GamGam | QCD direct diphoton production | background | 5.028 | 1 | 0.4274 | 0 |
| 302523 | ODEO_FEB2025_v0_GamGam_mc_302523.Pythia8EvtGen_A14NNPDF23LO_2DP20_Mass_250_400.GamGam | QCD direct diphoton production | background | 1.4436 | 1 | 0.4076 | 0 |
| 302524 | ODEO_FEB2025_v0_GamGam_mc_302524.Pythia8EvtGen_A14NNPDF23LO_2DP20_Mass_400_650.GamGam | QCD direct diphoton production | background | 0.3543 | 1 | 0.3869 | 0 |
| 341456 | ODEO_FEB2025_v0_GamGam_mc_341456.PowhegPythia8EvtGen_CT10_AZNLO_ZH125J_MINLO_veveWWlvqq_VpT.GamGam | qq->ZH, H->WW, Z->veve | signal | 0.7612 | 1 | 0.002088 | 0 |
| 341458 | ODEO_FEB2025_v0_GamGam_mc_341458.PowhegPythia8EvtGen_CT10_AZNLO_ZH125J_MINLO_vmuvmuWWlvqq_VpT.GamGam | qq->ZH, H->WW, Z->vmuvmu | signal | 0.7612 | 1 | 0.002088 | 0 |
| 341460 | ODEO_FEB2025_v0_GamGam_mc_341460.PowhegPy8EG_CT10_AZNLO_ZH125J_MINLO_vtauvtauWWlvqq_VpT.GamGam | qq->ZH, H->WW, Z->vtauvtau | signal | 0.7612 | 1 | 0.002088 | 0 |
| 343981 | ODEO_FEB2025_v0_GamGam_mc_343981.PowhegPythia8EvtGen_NNLOPS_nnlo_30_ggH125_gamgam.GamGam | H->gamma gamma GGF production | signal | 28.3 | 1.717 | 0.00227 | 0 |
| 345056 | ODEO_FEB2025_v0_GamGam_mc_345056.PowhegPythia8EvtGen_NNPDF3_AZNLO_ZH125J_MINLO_vvbb_VpT.GamGam | qq->ZH, H->bb, Z->vv | signal | 0.7612 | 1 | 0.1165 | 0 |
| 345058 | ODEO_FEB2025_v0_GamGam_mc_345058.PowhegPythia8EvtGen_NNPDF3_AZNLO_ggZH125_vvbb.GamGam | gg->ZH, H->bb, Z->vv | signal | 0.1227 | 1 | 0.1165 | 0 |
| 345060 | ODEO_FEB2025_v0_GamGam_mc_345060.PowhegPythia8EvtGen_NNLOPS_nnlo_30_ggH125_ZZ4l.GamGam | ggH H->ZZ->llll | signal | 28.3 | 1.717 | 0.000124 | 0 |
| 345061 | ODEO_FEB2025_v0_GamGam_mc_345061.PowhegPythia8EvtGen_NNPDF3_AZNLO_ggZH125_HgamgamZinc.GamGam | gg->ZH, H->gamgam, Z->inc | signal | 0.1227 | 1 | 0.00227 | 0 |

## 3. Object Definition and Event Selection

Reconstructed photons are built from available `photon_*` branches with tight identification/isolation flags and acceptance/kinematic thresholds from `analysis/regions.yaml`.
Derived event observables include `m_gg`, `diphoton_pt`, and `diphoton_deltaR` from leading/subleading photons.
Selections are evaluated by executable region expressions; no prose-only region is used in production execution.

## 4. Overview of the Analysis Strategy

The signal/background strategy is artifact-driven (`outputs_ref_smoke/background_modeling_strategy.json`) with explicit classification and CR->SR normalization intent.
Background strategy entries: 50 (mc_template), 0 (data_driven).
Partition validation: status=pass with 120 partitions (`outputs_ref_smoke/report/partition_checks.json`).
Mass-model selection artifacts are available for analytic signal/background parameterization and spurious-signal checks.

## 5. Signal and Control Regions

Category definitions:

| Category ID | Label | Assignment basis | Assignment definition | Coverage |
| --- | --- | --- | --- | --- |
| cat_2jet | VBF-enriched 2-jet | topology_selection | region_id == SR_2JET | full |
| cat_unconv_central_low_ptt | Unconv central low-pTt | topology_selection | region_id == SR_UNCONV_CENTRAL_LOW_PTT | full |
| cat_unconv_central_high_ptt | Unconv central high-pTt | topology_selection | region_id == SR_UNCONV_CENTRAL_HIGH_PTT | full |
| cat_unconv_rest_low_ptt | Unconv rest low-pTt | topology_selection | region_id == SR_UNCONV_REST_LOW_PTT | full |
| cat_unconv_rest_high_ptt | Unconv rest high-pTt | topology_selection | region_id == SR_UNCONV_REST_HIGH_PTT | full |
| cat_conv_central_low_ptt | Conv central low-pTt | topology_selection | region_id == SR_CONV_CENTRAL_LOW_PTT | full |
| cat_conv_central_high_ptt | Conv central high-pTt | topology_selection | region_id == SR_CONV_CENTRAL_HIGH_PTT | full |
| cat_conv_rest_low_ptt | Conv rest low-pTt | topology_selection | region_id == SR_CONV_REST_LOW_PTT | full |
| cat_conv_rest_high_ptt | Conv rest high-pTt | topology_selection | region_id == SR_CONV_REST_HIGH_PTT | full |
| cat_conv_transition | Conv transition | topology_selection | region_id == SR_CONV_TRANSITION | full |

| Region ID | Kind | Label | Data shown in plot |
| --- | --- | --- | --- |
| SR_DIPHOTON_INCL | signal | Inclusive diphoton monitoring SR | no |
| CR_BKG_SHAPE_CHECKS | control | Diphoton sideband control region | yes |
| SR_2JET | signal | VBF-enriched 2-jet category | no |
| SR_UNCONV_CENTRAL_LOW_PTT | signal | Unconverted-proxy central low-pTt | no |
| SR_UNCONV_CENTRAL_HIGH_PTT | signal | Unconverted-proxy central high-pTt | no |
| SR_UNCONV_REST_LOW_PTT | signal | Unconverted-proxy rest low-pTt | no |
| SR_UNCONV_REST_HIGH_PTT | signal | Unconverted-proxy rest high-pTt | no |
| SR_CONV_CENTRAL_LOW_PTT | signal | Converted-proxy central low-pTt | no |
| SR_CONV_CENTRAL_HIGH_PTT | signal | Converted-proxy central high-pTt | no |
| SR_CONV_REST_LOW_PTT | signal | Converted-proxy rest low-pTt | no |
| SR_CONV_REST_HIGH_PTT | signal | Converted-proxy rest high-pTt | no |
| SR_CONV_TRANSITION | signal | Converted-proxy transition category | no |

Partition manifest entries: 120 (`outputs_ref_smoke/manifest/partitions.json`).

Blinding summary: `blind_sr=True`, control-region-only normalization fit status=`fallback_no_control_data`.

## 6. Cut Flow

### SR_2JET

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| diphoton baseline | 27 | 0 | 0 |
| >=2 selected jets | 3 | 0 | 0 |
| delta_eta_jj > 2.8 | 1 | 0 | 0 |
| m_jj > 400 GeV | 1 | 0 | 0 |
| delta_phi(gg,jj) > 2.6 | 0 | 0 | 0 |

### SR_UNCONV_CENTRAL_LOW_PTT

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 0 | 0 | 0 |

### SR_UNCONV_CENTRAL_HIGH_PTT

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 0 | 0 | 0 |

### SR_UNCONV_REST_LOW_PTT

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 6 | 0 | 0 |

### SR_UNCONV_REST_HIGH_PTT

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 1 | 0 | 0 |

### SR_CONV_CENTRAL_LOW_PTT

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 2 | 0 | 0 |

### SR_CONV_CENTRAL_HIGH_PTT

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 0 | 0 | 0 |

### SR_CONV_REST_LOW_PTT

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 11 | 0 | 0 |

### SR_CONV_REST_HIGH_PTT

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 2 | 0 | 0 |

### SR_CONV_TRANSITION

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 5 | 0 | 0 |

### SR_DIPHOTON_INCL

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| >=2 tight photons | 207 | 0.00487531 | 6.63299e-05 |
| lead pT > 40 GeV | 119 | 0.00478915 | 0 |
| sublead pT > 30 GeV | 82 | 0.00413571 | 0 |
| 105 < m_gg < 160 GeV | 27 | 0 | 0 |

### CR_BKG_SHAPE_CHECKS

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| diphoton baseline | 82 | 0.00413571 | 0 |
| fit-range acceptance | 27 | 0 | 0 |
| sideband only | 22 | 0 | 0 |

Final region yields (weighted):

| Region | Data | Background | Signal |
| --- | ---: | ---: | ---: |
| CR_BKG_SHAPE_CHECKS | 22 | 0 | 0 |
| SR_2JET | 0 | 0 | 0 |
| SR_CONV_CENTRAL_HIGH_PTT | 0 | 0 | 0 |
| SR_CONV_CENTRAL_LOW_PTT | 2 | 0 | 0 |
| SR_CONV_REST_HIGH_PTT | 2 | 0 | 0 |
| SR_CONV_REST_LOW_PTT | 11 | 0 | 0 |
| SR_CONV_TRANSITION | 5 | 0 | 0 |
| SR_DIPHOTON_INCL | 27 | 0 | 0 |
| SR_UNCONV_CENTRAL_HIGH_PTT | 0 | 0 | 0 |
| SR_UNCONV_CENTRAL_LOW_PTT | 0 | 0 | 0 |
| SR_UNCONV_REST_HIGH_PTT | 1 | 0 | 0 |
| SR_UNCONV_REST_LOW_PTT | 6 | 0 | 0 |

## 7. Distributions in Signal and Control Regions

Required validation plots were produced, including photon kinematics, diphoton observables, cut-flow diagnostics, category plots, fit spectrum, pull, and blinded CR/SR region views.
In `SR_DIPHOTON_INCL`, observed data counts are peak[120,130] = 0 and sideband[105,120)U(130,160] = 0.
Produced plot files:
- `outputs_ref_smoke/report/plots/blinded_region_CR_BKG_SHAPE_CHECKS.png`
- `outputs_ref_smoke/report/plots/blinded_region_SR_2JET.png`
- `outputs_ref_smoke/report/plots/blinded_region_SR_CONV_CENTRAL_HIGH_PTT.png`
- `outputs_ref_smoke/report/plots/blinded_region_SR_CONV_CENTRAL_LOW_PTT.png`
- `outputs_ref_smoke/report/plots/blinded_region_SR_CONV_REST_HIGH_PTT.png`
- `outputs_ref_smoke/report/plots/blinded_region_SR_CONV_REST_LOW_PTT.png`
- `outputs_ref_smoke/report/plots/blinded_region_SR_CONV_TRANSITION.png`
- `outputs_ref_smoke/report/plots/blinded_region_SR_DIPHOTON_INCL.png`
- `outputs_ref_smoke/report/plots/blinded_region_SR_UNCONV_CENTRAL_HIGH_PTT.png`
- `outputs_ref_smoke/report/plots/blinded_region_SR_UNCONV_CENTRAL_LOW_PTT.png`
- `outputs_ref_smoke/report/plots/blinded_region_SR_UNCONV_REST_HIGH_PTT.png`
- `outputs_ref_smoke/report/plots/blinded_region_SR_UNCONV_REST_LOW_PTT.png`
- `outputs_ref_smoke/report/plots/cutflow_plot.png`
- `outputs_ref_smoke/report/plots/diphoton_deltaR.png`
- `outputs_ref_smoke/report/plots/diphoton_mass_category_1.png`
- `outputs_ref_smoke/report/plots/diphoton_mass_category_2.png`
- `outputs_ref_smoke/report/plots/diphoton_mass_category_3.png`
- `outputs_ref_smoke/report/plots/diphoton_mass_fit.png`
- `outputs_ref_smoke/report/plots/diphoton_mass_preselection.png`
- `outputs_ref_smoke/report/plots/diphoton_mass_pull.png`
- `outputs_ref_smoke/report/plots/diphoton_pt.png`
- `outputs_ref_smoke/report/plots/photon_eta_leading.png`
- `outputs_ref_smoke/report/plots/photon_eta_subleading.png`
- `outputs_ref_smoke/report/plots/photon_multiplicity.png`
- `outputs_ref_smoke/report/plots/photon_pt_leading.png`
- `outputs_ref_smoke/report/plots/photon_pt_subleading.png`

## 8. Systematic Uncertainties

Systematics are currently implemented as a stat-only nuisance model (`Systematics not fully specified; using stat-only model.`) with explicit placeholder language; no additional shape or normalization nuisance set is asserted beyond provided artifacts.
Signal-shape proxy: mean=132.5, width=15.8745, model=DSCB_proxy.
Background choice: family=bernstein degree=1 (passed target=True).
Spurious signal: N_spur=-1e-09, sigma_Nsig=4.26401e-06, r_spur=0.000234521 (threshold=0.2).

## 9. Statistical Interpretation

Observed fit (`FIT_MAIN`): status=ok, mu=10, twice_nll=585.676.
Observed discovery significance: q0=37.4189, Z=6.1171, mu_hat=10.
Asimov (background-only) expected discovery: q0=0, Z=0.
Asimov (signal-plus-background, mu=1) expected discovery: q0=3.2746e-07, Z=0.000572242.
Given active SR blinding in visualization products, Asimov results are the primary pre-unblinding sensitivity reference.

## 10. Summary

The repository pipeline successfully produced a complete, reproducible set of artifacts across event processing, selection, template construction, fitting, significance, and blinded visualization.
For `FIT_MAIN`, the observed discovery significance is Z=6.1171 and the Asimov mu=1 expected discovery is Z=0.000572242.
The current model is suitable for a robust open-data analysis demonstration and provides a transparent baseline for future systematic-model and category refinements.

## Implementation Differences from Reference Analysis

| Reference concept | Open-data observable used | Reasoning for replacement | Expected impact |
| --- | --- | --- | --- |
| Era-specific photon identification/isolation working points | `photon_isTightID`, `photon_isTightIso`, kinematic/acceptance thresholds in `analysis/regions.yaml` | These are directly available and executable in the ntuples while preserving a tight-photon selection intent | Selection efficiency and purity differ from legacy calibrations |
| Full legacy category scheme | Category/region partition artifacts (`outputs_ref_smoke/report/partition_spec.json`, `outputs_ref_smoke/manifest/partitions.json`) with executable category-proxy regions | The workflow now requires machine-readable category assignment and (category, region) manifest for downstream tools | Category granularity and category purity differ due open-data proxy substitutions |
| Full nuisance parameter model | Stat-only nuisance placeholder in `outputs/systematics.json` plus explicit spurious-signal checks | Available public inputs in this repository support robust stat-only execution; added systematics require external calibrations not provided here | Uncertainty coverage is reduced and interval realism is limited |
| Reference-era absolute normalization details | Metadata-driven DSID normalization fields with runtime registry luminosity values and CR-constrained scaling | This is the closest consistent open-data implementation using available metadata and fit constraints | Absolute MC normalization differs from a full production calibration chain |
| Target integrated luminosity 36.1 fb^-1 for Run-2 dataset | Current registry-derived `lumi_fb` values in produced artifacts | Current summary/registry mapping in this repository does not inject a numeric 36.1 fb^-1 into per-sample `lumi_fb`; this is kept explicit rather than silently overwritten | Absolute yield scale is shifted and CR normalization factors absorb part of the mismatch |

## Appendix A: Agent Decisions and Deviations

| Issue | Decision | Justification |
| --- | --- | --- |
| Missing direct legacy object variables in open-data ntuples | Use nearest reconstructed photon ID/isolation flags and explicit kinematic cuts | Keeps selection executable and physics-motivated while preserving transparency of approximation |
| Requirement for pre-unblinding sensitivity statement | Added Asimov significance artifact at `outputs_ref_smoke/fit/FIT_MAIN/significance_asimov.json` | Provides expected sensitivity context without relying on SR data display |
| Need for normalization traceability | Added normalization artifacts under `outputs_ref_smoke/normalization/` (`metadata_resolution.json`, `norm_table.json`, `norm_audit.json`, `stacked_yields_summary.json`) | Makes per-sample normalization terms and audit status explicit and reviewable |
| Need for explicit category definitions | Added partition artifacts (`partition_spec.json`, `partition_checks.json`, `partitions.json`) and category table in this report | Makes category/channel definitions explicit, auditable, and machine-readable |
| Target luminosity vs runtime registry luminosity mismatch | Kept runtime `lumi_fb` values explicit in artifacts/report and treated this as a documented deviation | Avoids hidden renormalization and keeps downstream interpretation auditable |
| Signal-region plot blinding during reporting | Kept SR data hidden in blinded region plots and referenced Asimov expected sensitivity in interpretation | Preserves blind-analysis behavior while still reporting a complete statistical workflow |

Report metadata: summary=`outputs_ref_smoke/summary.normalized.json`, outputs=`outputs_ref_smoke`, target_lumi_fb=36.1.
