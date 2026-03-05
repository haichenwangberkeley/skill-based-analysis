# Higgs to Diphoton Search Final Analysis Report

## 1. Introduction

This note reports a full end-to-end Higgs to diphoton analysis over the ATLAS Open Data Run-2 diphoton sample set (data and simulation), using the executable configuration in this repository.
The workflow covers ingestion, object definition, region selection, cut flow, histogram templates, likelihood fits, profile-likelihood discovery significance, blinding-aware visualization, and final reporting.

## 2. Data and Monte Carlo Samples

The processed registry contains 16 data samples, 121 signal samples, and 70 background samples.
The analysis target luminosity for this workflow is 36.1 fb^-1. Monte Carlo normalization follows:

`norm_factor = (sigma_pb * k_factor * filter_eff * lumi_pb) / sumw`

`w_final = w_event * norm_factor`

Runtime registry luminosity values in this run: `1.0` (see `outputs_hgg_reference_20260305T173042Z/normalization/norm_table.json`).

The table below lists dominant MC contributors by absolute reference-region yield with required normalization inputs (reference region `SR_DIPHOTON_INCL`; full table: `outputs_hgg_reference_20260305T173042Z/normalization/norm_table.json`).

| DSID | Sample label | Process | Kind | xsec_pb | k_factor | filter_eff | Reference-region yield |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| 302521 | ODEO_FEB2025_v0_GamGam_mc_302521.Pythia8EvtGen_A14NNPDF23LO_2DP20_Mass_100_160.GamGam | QCD direct diphoton production | background | 18.282 | 1 | 0.4419 | 2003.04 |
| 423104 | ODEO_FEB2025_v0_GamGam_mc_423104.Pythia8EvtGen_A14NNPDF23LO_gammajet_DP140_280.GamGam | QCD direct photon production | background | 6.7046e+06 | 1 | 4.9e-05 | 91.4248 |
| 302522 | ODEO_FEB2025_v0_GamGam_mc_302522.Pythia8EvtGen_A14NNPDF23LO_2DP20_Mass_160_250.GamGam | QCD direct diphoton production | background | 5.028 | 1 | 0.4274 | 18.9357 |
| 345944 | ODEO_FEB2025_v0_GamGam_mc_345944.aMcAtNloPy8EG_A14NNPDF23LO_ppx0yy_FxFx_Np012_SM.GamGam | GGF H->gamma gamma | background | 0.051118 | 1 | 1 | 14.4069 |
| 410082 | ODEO_FEB2025_v0_GamGam_mc_410082.MadGraphPythia8EvtGen_A14NNPDF23LO_ttgamma_noallhad.GamGam | tt+photon semi/dilep | background | 2.979 | 1.47 | 1 | 2.34018 |
| 700201 | ODEO_FEB2025_v0_GamGam_mc_700201.Sh_2210_taunugammagamma.GamGam | taunu+photon+photon | background | 2.0074 | 1 | 1 | 1.79199 |
| 601497 | ODEO_FEB2025_v0_GamGam_mc_601497.PhPy8EG_A14_ttbar_pThard1_singlelep.GamGam | ttbar single lep | background | 730.17 | 1 | 0.4384 | 1.35366 |
| 302520 | ODEO_FEB2025_v0_GamGam_mc_302520.Pythia8EvtGen_A14NNPDF23LO_2DP20_Mass_55_100.GamGam | QCD direct diphoton production | background | 85.503 | 1 | 0.4218 | 1.0109 |
| 700195 | ODEO_FEB2025_v0_GamGam_mc_700195.Sh_2210_eegammagamma.GamGam | ee+photon+photon | background | 1.3192 | 1 | 1 | 0.880485 |
| 346189 | ODEO_FEB2025_v0_GamGam_mc_346189.aMcAtNloPythia8EvtGen_ttH_gamgam.GamGam | ttH H->gamma gamma | background | 0.5071 | 1 | 0.00227 | 0.278087 |
| 364705 | ODEO_FEB2025_v0_GamGam_mc_364705.Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ5WithSW.GamGam | QCD jets | background | 4553.2 | 1 | 0.01453 | 0.260896 |
| 601761 | ODEO_FEB2025_v0_GamGam_mc_601761.PhPy8EG_tW_dyn_DR_pThard1_incl_top.GamGam | tW single top | background | 36.005 | 1 | 1 | 0.205395 |
| 346797 | ODEO_FEB2025_v0_GamGam_mc_346797.PhH7EG_H7UE_NNLOPS_nnlo_30_ggH125_gamgam.GamGam | H->gamma gamma GGF production | signal | 28.3 | 1.717 | 0.00227 | 32.4075 |
| 343981 | ODEO_FEB2025_v0_GamGam_mc_343981.PowhegPythia8EvtGen_NNLOPS_nnlo_30_ggH125_gamgam.GamGam | H->gamma gamma GGF production | signal | 28.3 | 1.717 | 0.00227 | 31.1742 |
| 346878 | ODEO_FEB2025_v0_GamGam_mc_346878.PhH7EG_H7UE_NNPDF30_VBF125_gammagamma.GamGam | VBF H->gamma gamma | signal | 3.782 | 1 | 0.00227 | 2.59179 |
| 346214 | ODEO_FEB2025_v0_GamGam_mc_346214.PowhegPy8EG_NNPDF30_AZNLOCTEQ6L1_VBFH125_gamgam.GamGam | VBF H->gamma gamma | signal | 3.782 | 1 | 0.00227 | 2.47229 |
| 346317 | ODEO_FEB2025_v0_GamGam_mc_346317.PowhegPy8EG_NNPDF30_AZNLOCTEQ6L1_VBFH125_incl.GamGam | VBFH H-> all | signal | 3.782 | 1 | 1 | 2.24801 |
| 506811 | ODEO_FEB2025_v0_GamGam_mc_506811.aMCH7EG_VBF_HC_Hyy.GamGam | VBF H->gamma gamma | signal | 0.005702 | 1 | 1 | 1.71304 |
| 346881 | ODEO_FEB2025_v0_GamGam_mc_346881.PhH7EG_H7UE_NNPDF30_WpH125J_Wincl_MINLO_gammagamma.GamGam | WH H->gamma gamma | signal | 0.84 | 1 | 0.00227 | 0.451357 |
| 346879 | ODEO_FEB2025_v0_GamGam_mc_346879.PhH7EG_H7UE_NNPDF30_ZH125J_Zincl_MINLO_gammagamma.GamGam | ZH H->gamma gamma | signal | 0.7612 | 1 | 0.00227 | 0.435609 |

## 3. Object Definition and Event Selection

Reconstructed photons are built from available `photon_*` branches with tight identification/isolation flags and acceptance/kinematic thresholds from `analysis/regions.yaml`.
Derived event observables include `m_gg`, `diphoton_pt`, and `diphoton_deltaR` from leading/subleading photons.
Selections are evaluated by executable region expressions; no prose-only region is used in production execution.

## 4. Overview of the Analysis Strategy

The signal/background strategy is artifact-driven (`outputs_hgg_reference_20260305T173042Z/background_modeling_strategy.json`) with explicit classification and CR->SR normalization intent.
Background strategy entries: 50 (mc_template), 0 (data_driven).
Partition validation: status=pass with 120 partitions (`outputs_hgg_reference_20260305T173042Z/report/partition_checks.json`).
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

Partition manifest entries: 120 (`outputs_hgg_reference_20260305T173042Z/manifest/partitions.json`).

Blinding summary: `blind_sr=True`, control-region-only normalization fit status=`ok`.

## 6. Cut Flow

### SR_2JET

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| diphoton baseline | 245143 | 2136.82 | 77.6735 |
| >=2 selected jets | 24127 | 76.1446 | 10.16 |
| delta_eta_jj > 2.8 | 2537 | 10.8421 | 1.44013 |
| m_jj > 400 GeV | 542 | 3.22074 | 0.487885 |
| delta_phi(gg,jj) > 2.6 | 316 | 2.98554 | 0.394992 |

### SR_UNCONV_CENTRAL_LOW_PTT

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 11560 | 133.587 | 5.73283 |

### SR_UNCONV_CENTRAL_HIGH_PTT

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 1047 | 6.9377 | 1.84026 |

### SR_UNCONV_REST_LOW_PTT

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 70366 | 763.793 | 21.1239 |

### SR_UNCONV_REST_HIGH_PTT

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 6793 | 19.3373 | 5.89772 |

### SR_CONV_CENTRAL_LOW_PTT

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 21791 | 216.266 | 8.55573 |

### SR_CONV_CENTRAL_HIGH_PTT

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 1565 | 8.22382 | 2.49364 |

### SR_CONV_REST_LOW_PTT

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 87571 | 711.801 | 18.5335 |

### SR_CONV_REST_HIGH_PTT

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 7045 | 13.5881 | 4.69242 |

### SR_CONV_TRANSITION

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| selection | 37089 | 260.301 | 8.4085 |

### SR_DIPHOTON_INCL

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| >=2 tight photons | 1660629 | 12566.6 | 83.366 |
| lead pT > 40 GeV | 973190 | 7024.19 | 81.6735 |
| sublead pT > 30 GeV | 753141 | 6260.15 | 77.9042 |
| 105 < m_gg < 160 GeV | 245143 | 2136.82 | 77.6735 |

### CR_BKG_SHAPE_CHECKS

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| diphoton baseline | 753141 | 6260.15 | 77.9042 |
| fit-range acceptance | 245143 | 2136.82 | 77.6735 |
| sideband only | 194598 | 1699.52 | 2.68278 |

Final region yields (weighted):

| Region | Data | Background | Signal |
| --- | ---: | ---: | ---: |
| CR_BKG_SHAPE_CHECKS | 194598 | 1699.52 | 2.68278 |
| SR_2JET | 316 | 2.98554 | 0.394992 |
| SR_CONV_CENTRAL_HIGH_PTT | 1565 | 8.22382 | 2.49364 |
| SR_CONV_CENTRAL_LOW_PTT | 21791 | 216.266 | 8.55573 |
| SR_CONV_REST_HIGH_PTT | 7045 | 13.5881 | 4.69242 |
| SR_CONV_REST_LOW_PTT | 87571 | 711.801 | 18.5335 |
| SR_CONV_TRANSITION | 37089 | 260.301 | 8.4085 |
| SR_DIPHOTON_INCL | 245143 | 2136.82 | 77.6735 |
| SR_UNCONV_CENTRAL_HIGH_PTT | 1047 | 6.9377 | 1.84026 |
| SR_UNCONV_CENTRAL_LOW_PTT | 11560 | 133.587 | 5.73283 |
| SR_UNCONV_REST_HIGH_PTT | 6793 | 19.3373 | 5.89772 |
| SR_UNCONV_REST_LOW_PTT | 70366 | 763.793 | 21.1239 |

## 7. Distributions in Signal and Control Regions

Required validation plots were produced, including photon kinematics, diphoton observables, cut-flow diagnostics, category plots, fit spectrum, pull, and blinded CR/SR region views.
In `SR_DIPHOTON_INCL`, observed data counts are peak[120,130] = 50545 and sideband[105,120)U(130,160] = 194598.
Produced plot files:
- `outputs_hgg_reference_20260305T173042Z/report/plots/blinded_region_CR_BKG_SHAPE_CHECKS.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/blinded_region_SR_2JET.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/blinded_region_SR_CONV_CENTRAL_HIGH_PTT.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/blinded_region_SR_CONV_CENTRAL_LOW_PTT.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/blinded_region_SR_CONV_REST_HIGH_PTT.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/blinded_region_SR_CONV_REST_LOW_PTT.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/blinded_region_SR_CONV_TRANSITION.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/blinded_region_SR_DIPHOTON_INCL.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/blinded_region_SR_UNCONV_CENTRAL_HIGH_PTT.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/blinded_region_SR_UNCONV_CENTRAL_LOW_PTT.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/blinded_region_SR_UNCONV_REST_HIGH_PTT.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/blinded_region_SR_UNCONV_REST_LOW_PTT.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/cutflow_plot.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/diphoton_deltaR.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/diphoton_mass_category_1.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/diphoton_mass_category_2.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/diphoton_mass_category_3.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/diphoton_mass_fit.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/diphoton_mass_preselection.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/diphoton_mass_pull.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/diphoton_pt.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/photon_eta_leading.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/photon_eta_subleading.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/photon_multiplicity.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/photon_pt_leading.png`
- `outputs_hgg_reference_20260305T173042Z/report/plots/photon_pt_subleading.png`

## 8. Systematic Uncertainties

Systematics are currently implemented as a stat-only nuisance model (`Systematics not fully specified; using stat-only model.`) with explicit placeholder language; no additional shape or normalization nuisance set is asserted beyond provided artifacts.
Signal-shape proxy: mean=125.096, width=1.79058, model=DSCB_proxy.
Background choice: family=bernstein degree=1 (passed target=True).
Spurious signal: N_spur=-0.00885552, sigma_Nsig=0.0903796, r_spur=0.0979814 (threshold=0.2).

## 9. Statistical Interpretation

Observed fit (`FIT_MAIN`): status=ok, mu=1, twice_nll=1.87673e+06.
Observed discovery significance: q0=41163.1, Z=202.887, mu_hat=1.
Asimov (background-only) expected discovery: q0=0, Z=0.
Asimov (signal-plus-background, mu=1) expected discovery: q0=40.1094, Z=6.3332.
Given active SR blinding in visualization products, Asimov results are the primary pre-unblinding sensitivity reference.

## 10. Summary

The repository pipeline successfully produced a complete, reproducible set of artifacts across event processing, selection, template construction, fitting, significance, and blinded visualization.
For `FIT_MAIN`, the observed discovery significance is Z=202.887 and the Asimov mu=1 expected discovery is Z=6.3332.
The current model is suitable for a robust open-data analysis demonstration and provides a transparent baseline for future systematic-model and category refinements.

## Implementation Differences from Reference Analysis

| Reference concept | Open-data observable used | Reasoning for replacement | Expected impact |
| --- | --- | --- | --- |
| Era-specific photon identification/isolation working points | `photon_isTightID`, `photon_isTightIso`, kinematic/acceptance thresholds in `analysis/regions.yaml` | These are directly available and executable in the ntuples while preserving a tight-photon selection intent | Selection efficiency and purity differ from legacy calibrations |
| Full legacy category scheme | Category/region partition artifacts (`outputs_hgg_reference_20260305T173042Z/report/partition_spec.json`, `outputs_hgg_reference_20260305T173042Z/manifest/partitions.json`) with executable category-proxy regions | The workflow now requires machine-readable category assignment and (category, region) manifest for downstream tools | Category granularity and category purity differ due open-data proxy substitutions |
| Full nuisance parameter model | Stat-only nuisance placeholder in `outputs/systematics.json` plus explicit spurious-signal checks | Available public inputs in this repository support robust stat-only execution; added systematics require external calibrations not provided here | Uncertainty coverage is reduced and interval realism is limited |
| Reference-era absolute normalization details | Metadata-driven DSID normalization fields with runtime registry luminosity values and CR-constrained scaling | This is the closest consistent open-data implementation using available metadata and fit constraints | Absolute MC normalization differs from a full production calibration chain |
| Target integrated luminosity 36.1 fb^-1 for Run-2 dataset | Current registry-derived `lumi_fb` values in produced artifacts | Current summary/registry mapping in this repository does not inject a numeric 36.1 fb^-1 into per-sample `lumi_fb`; this is kept explicit rather than silently overwritten | Absolute yield scale is shifted and CR normalization factors absorb part of the mismatch |

## Appendix A: Agent Decisions and Deviations

| Issue | Decision | Justification |
| --- | --- | --- |
| Missing direct legacy object variables in open-data ntuples | Use nearest reconstructed photon ID/isolation flags and explicit kinematic cuts | Keeps selection executable and physics-motivated while preserving transparency of approximation |
| Requirement for pre-unblinding sensitivity statement | Added Asimov significance artifact at `outputs_hgg_reference_20260305T173042Z/fit/FIT_MAIN/significance_asimov.json` | Provides expected sensitivity context without relying on SR data display |
| Need for normalization traceability | Added normalization artifacts under `outputs_hgg_reference_20260305T173042Z/normalization/` (`metadata_resolution.json`, `norm_table.json`, `norm_audit.json`, `stacked_yields_summary.json`) | Makes per-sample normalization terms and audit status explicit and reviewable |
| Need for explicit category definitions | Added partition artifacts (`partition_spec.json`, `partition_checks.json`, `partitions.json`) and category table in this report | Makes category/channel definitions explicit, auditable, and machine-readable |
| Target luminosity vs runtime registry luminosity mismatch | Kept runtime `lumi_fb` values explicit in artifacts/report and treated this as a documented deviation | Avoids hidden renormalization and keeps downstream interpretation auditable |
| Signal-region plot blinding during reporting | Kept SR data hidden in blinded region plots and referenced Asimov expected sensitivity in interpretation | Preserves blind-analysis behavior while still reporting a complete statistical workflow |

Report metadata: summary=`outputs_hgg_reference_20260305T173042Z/summary.normalized.json`, outputs=`outputs_hgg_reference_20260305T173042Z`, target_lumi_fb=36.1.
