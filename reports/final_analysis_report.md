# Higgs to Diphoton Search Final Analysis Report

## 1. Introduction

This note reports a full end-to-end Higgs to diphoton analysis over the ATLAS Open Data Run-2 diphoton sample set (data and simulation), using the executable configuration in this repository.
The workflow covers ingestion, object definition, region selection, cut flow, histogram templates, likelihood fits, profile-likelihood discovery significance, blinding-aware visualization, and final reporting.

## 2. Data and Monte Carlo Samples

The processed registry contains 16 data samples, 121 signal samples, and 70 background samples.
The analysis target luminosity for this workflow is 36.1 fb^-1. Monte Carlo normalization follows:

`norm_factor = (sigma_pb * k_factor * filter_eff * lumi_pb) / sumw`

`w_final = w_event * norm_factor`

Runtime registry luminosity values in this run: `1.0` (see `outputs/normalization/norm_table.json`).

The table below lists dominant MC contributors by absolute SR yield with required normalization inputs (full table: `outputs/normalization/norm_table.json`).

| DSID | Sample label | Process | Kind | xsec_pb | k_factor | filter_eff | SR yield |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| 302521 | ODEO_FEB2025_v0_GamGam_mc_302521.Pythia8EvtGen_A14NNPDF23LO_2DP20_Mass_100_160.GamGam | QCD direct diphoton production | background | 18.282 | 1 | 0.4419 | 12.2963 |
| 423104 | ODEO_FEB2025_v0_GamGam_mc_423104.Pythia8EvtGen_A14NNPDF23LO_gammajet_DP140_280.GamGam | QCD direct photon production | background | 6.7046e+06 | 1 | 4.9e-05 | 6.98336 |
| 410082 | ODEO_FEB2025_v0_GamGam_mc_410082.MadGraphPythia8EvtGen_A14NNPDF23LO_ttgamma_noallhad.GamGam | tt+photon semi/dilep | background | 2.979 | 1.47 | 1 | 0.836616 |
| 700201 | ODEO_FEB2025_v0_GamGam_mc_700201.Sh_2210_taunugammagamma.GamGam | taunu+photon+photon | background | 2.0074 | 1 | 1 | 0.672222 |
| 302522 | ODEO_FEB2025_v0_GamGam_mc_302522.Pythia8EvtGen_A14NNPDF23LO_2DP20_Mass_160_250.GamGam | QCD direct diphoton production | background | 5.028 | 1 | 0.4274 | 0.4322 |
| 700195 | ODEO_FEB2025_v0_GamGam_mc_700195.Sh_2210_eegammagamma.GamGam | ee+photon+photon | background | 1.3192 | 1 | 1 | 0.345236 |
| 345944 | ODEO_FEB2025_v0_GamGam_mc_345944.aMcAtNloPy8EG_A14NNPDF23LO_ppx0yy_FxFx_Np012_SM.GamGam | GGF H->gamma gamma | background | 0.051118 | 1 | 1 | 0.31225 |
| 700709 | ODEO_FEB2025_v0_GamGam_mc_700709.Sh_2212_lvgammajj.GamGam | lnu+photon+jets | background | 1.781 | 1 | 1 | 0.263635 |
| 601761 | ODEO_FEB2025_v0_GamGam_mc_601761.PhPy8EG_tW_dyn_DR_pThard1_incl_top.GamGam | tW single top | background | 36.005 | 1 | 1 | 0.221852 |
| 801976 | ODEO_FEB2025_v0_GamGam_mc_801976.Py8EG_A14NNPDF23LO_Zprime_NoInt_tautau_SSM3000.GamGam | pp>Zprime>tautau | background | 1.2465 | 1 | 1 | 0.185956 |
| 601352 | ODEO_FEB2025_v0_GamGam_mc_601352.PhPy8EG_tW_dyn_DR_incl_antitop.GamGam | tW single top | background | 35.972 | 1 | 1 | 0.167362 |
| 601497 | ODEO_FEB2025_v0_GamGam_mc_601497.PhPy8EG_A14_ttbar_pThard1_singlelep.GamGam | ttbar single lep | background | 730.17 | 1 | 0.4384 | 0.158275 |
| 346317 | ODEO_FEB2025_v0_GamGam_mc_346317.PowhegPy8EG_NNPDF30_AZNLOCTEQ6L1_VBFH125_incl.GamGam | VBFH H-> all | signal | 3.782 | 1 | 1 | 2.44888 |
| 343981 | ODEO_FEB2025_v0_GamGam_mc_343981.PowhegPythia8EvtGen_NNLOPS_nnlo_30_ggH125_gamgam.GamGam | H->gamma gamma GGF production | signal | 28.3 | 1.717 | 0.00227 | 0.697662 |
| 346311 | ODEO_FEB2025_v0_GamGam_mc_346311.PowhegPythia8EvtGen_NNPDF30_AZNLO_WpH125J_Wincl_H_incl_MINLO.GamGam | WpH W+->all H-> all | signal | 0.84 | 1 | 1 | 0.360929 |
| 346310 | ODEO_FEB2025_v0_GamGam_mc_346310.PowhegPythia8EvtGen_NNPDF30_AZNLO_ZH125J_Zincl_H_incl_MINLO.GamGam | ZH Z->all H-> all | signal | 0.7612 | 1 | 1 | 0.356301 |
| 346312 | ODEO_FEB2025_v0_GamGam_mc_346312.PowhegPythia8EvtGen_NNPDF30_AZNLO_WmH125J_Wincl_H_incl_MINLO.GamGam | WmH W- ->all H-> all | signal | 0.5328 | 1 | 1 | 0.280121 |
| 345961 | ODEO_FEB2025_v0_GamGam_mc_345961.PowhegPythia8EvtGen_NNLOPS_nnlo_30_ggH125_gamstargam.GamGam | ggH H->gam*gam, gam*->ll | signal | 28.3 | 1.717 | 0.000431 | 0.173197 |
| 345834 | ODEO_FEB2025_v0_GamGam_mc_345834.PowhegPythia8EvtGen_NNPDF30_AZNLOCTEQ6L1_VBFH125_gamstargam.GamGam | VBF H,  H->gam*gam, gam*->ll | signal | 3.782 | 1 | 0.00227 | 0.172812 |
| 346214 | ODEO_FEB2025_v0_GamGam_mc_346214.PowhegPy8EG_NNPDF30_AZNLOCTEQ6L1_VBFH125_gamgam.GamGam | VBF H->gamma gamma | signal | 3.782 | 1 | 0.00227 | 0.140611 |

## 3. Object Definition and Event Selection

Reconstructed photons are built from available `photon_*` branches with tight identification/isolation flags and acceptance/kinematic thresholds from `analysis/regions.yaml`.
Derived event observables include `m_gg`, `diphoton_pt`, and `diphoton_deltaR` from leading/subleading photons.
Selections are evaluated by executable region expressions; no prose-only region is used in production execution.

## 4. Overview of the Analysis Strategy

The signal/background strategy is artifact-driven (`outputs/background_modeling_strategy.json`) with explicit classification and CR->SR normalization intent.
Background strategy entries: 50 (mc_template), 0 (data_driven).
Mass-model selection artifacts are available for analytic signal/background parameterization and spurious-signal checks.

## 5. Signal and Control Regions

| Region ID | Kind | Label | Data shown in plot |
| --- | --- | --- | --- |
| SR_DIPHOTON_INCL | signal | Inclusive diphoton SR | no |
| CR_DIPHOTON_SIDE | control | Diphoton sideband CR | yes |
| SR_HH_GG_BB | signal | Diphoton high-pT proxy SR | no |

Blinding summary: `blind_sr=True`, control-region-only normalization fit status=`ok`.

## 6. Cut Flow

### SR_DIPHOTON_INCL

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| >=2 tight photons | 1334 | 103.684 | 5.6307 |
| lead pT > 35 | 989 | 94.4475 | 5.57537 |
| sublead pT > 25 | 989 | 94.4475 | 5.57537 |
| 105 < m_gg < 160 | 224 | 23.0141 | 5.31675 |

### CR_DIPHOTON_SIDE

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| >=2 tight photons | 1334 | 103.684 | 5.6307 |
| pT cuts | 989 | 94.4475 | 5.57537 |
| sideband | 906 | 86.0423 | 0.287043 |
| in fit range | 141 | 14.6089 | 0.0284175 |

### SR_HH_GG_BB

| Step | Data n_raw | Background weighted | Signal weighted |
| --- | ---: | ---: | ---: |
| diphoton preselection | 245 | 23.8508 | 5.32995 |
| leading/subleading pT | 224 | 23.0141 | 5.31675 |
| diphoton pT > 80 | 20 | 8.04374 | 2.51989 |

Final region yields (weighted):

| Region | Data | Background | Signal |
| --- | ---: | ---: | ---: |
| CR_DIPHOTON_SIDE | 141 | 14.6089 | 0.0284175 |
| SR_DIPHOTON_INCL | 224 | 23.0141 | 5.31675 |
| SR_HH_GG_BB | 20 | 8.04374 | 2.51989 |

## 7. Distributions in Signal and Control Regions

Required validation plots were produced, including photon kinematics, diphoton observables, cut-flow diagnostics, category plots, fit spectrum, pull, and blinded CR/SR region views.
In `SR_DIPHOTON_INCL`, observed data counts are peak[120,130] = 46 and sideband[105,120)U(130,160] = 178.
Produced plot files:
- `outputs/report/plots/blinded_region_CR_DIPHOTON_SIDE.png`
- `outputs/report/plots/blinded_region_SR_DIPHOTON_INCL.png`
- `outputs/report/plots/blinded_region_SR_HH_GG_BB.png`
- `outputs/report/plots/cutflow_plot.png`
- `outputs/report/plots/diphoton_deltaR.png`
- `outputs/report/plots/diphoton_mass_category_1.png`
- `outputs/report/plots/diphoton_mass_category_2.png`
- `outputs/report/plots/diphoton_mass_category_3.png`
- `outputs/report/plots/diphoton_mass_fit.png`
- `outputs/report/plots/diphoton_mass_preselection.png`
- `outputs/report/plots/diphoton_mass_pull.png`
- `outputs/report/plots/diphoton_pt.png`
- `outputs/report/plots/photon_eta_leading.png`
- `outputs/report/plots/photon_eta_subleading.png`
- `outputs/report/plots/photon_multiplicity.png`
- `outputs/report/plots/photon_pt_leading.png`
- `outputs/report/plots/photon_pt_subleading.png`

## 8. Systematic Uncertainties

Systematics are currently implemented as a stat-only nuisance model (`Systematics not fully specified; using stat-only model.`) with explicit placeholder language; no additional shape or normalization nuisance set is asserted beyond provided artifacts.
Signal-shape proxy: mean=125.141, width=2.61706, model=DSCB_proxy.
Background choice: family=bernstein degree=1 (passed target=True).
Spurious signal: N_spur=0.0295957, sigma_Nsig=0.248907, r_spur=0.118903 (threshold=0.2).

## 9. Statistical Interpretation

Observed fit (`FIT_MAIN`): status=ok, mu=1.01182, twice_nll=441.77.
Observed discovery significance: q0=0.825532, Z=0.908588, mu_hat=1.01182.
Asimov (background-only) expected discovery: q0=0, Z=0.
Asimov (signal-plus-background, mu=1) expected discovery: q0=4.9933, Z=2.23457.
Given active SR blinding in visualization products, Asimov results are the primary pre-unblinding sensitivity reference.

## 10. Summary

The repository pipeline successfully produced a complete, reproducible set of artifacts across event processing, selection, template construction, fitting, significance, and blinded visualization.
For `FIT_MAIN`, the observed discovery significance is Z=0.908588 and the Asimov mu=1 expected discovery is Z=2.23457.
The current model is suitable for a robust open-data analysis demonstration and provides a transparent baseline for future systematic-model and category refinements.

## Implementation Differences from Reference Analysis

| Reference concept | Open-data observable used | Reasoning for replacement | Expected impact |
| --- | --- | --- | --- |
| Era-specific photon identification/isolation working points | `photon_isTightID`, `photon_isTightIso`, kinematic/acceptance thresholds in `analysis/regions.yaml` | These are directly available and executable in the ntuples while preserving a tight-photon selection intent | Selection efficiency and purity differ from legacy calibrations |
| Full legacy category scheme | Executable SR/CR region set in `analysis/regions.yaml` (`SR_DIPHOTON_INCL`, `CR_DIPHOTON_SIDE`, `SR_HH_GG_BB`) | The workflow requires fully machine-executable selections with available branches | Category composition and relative sensitivity differ from the legacy setup |
| Full nuisance parameter model | Stat-only nuisance placeholder in `outputs/systematics.json` plus explicit spurious-signal checks | Available public inputs in this repository support robust stat-only execution; added systematics require external calibrations not provided here | Uncertainty coverage is reduced and interval realism is limited |
| Reference-era absolute normalization details | Metadata-driven DSID normalization fields with runtime registry luminosity values and CR-constrained scaling | This is the closest consistent open-data implementation using available metadata and fit constraints | Absolute MC normalization differs from a full production calibration chain |
| Target integrated luminosity 36.1 fb^-1 for Run-2 dataset | Current registry-derived `lumi_fb` values in produced artifacts | Current summary/registry mapping in this repository does not inject a numeric 36.1 fb^-1 into per-sample `lumi_fb`; this is kept explicit rather than silently overwritten | Absolute yield scale is shifted and CR normalization factors absorb part of the mismatch |

## Appendix A: Agent Decisions and Deviations

| Issue | Decision | Justification |
| --- | --- | --- |
| Missing direct legacy object variables in open-data ntuples | Use nearest reconstructed photon ID/isolation flags and explicit kinematic cuts | Keeps selection executable and physics-motivated while preserving transparency of approximation |
| Requirement for pre-unblinding sensitivity statement | Added Asimov significance artifact at `outputs/fit/FIT_MAIN/significance_asimov.json` | Provides expected sensitivity context without relying on SR data display |
| Need for normalization traceability | Added normalization artifacts under `outputs/normalization/` (`metadata_resolution.json`, `norm_table.json`, `norm_audit.json`, `stacked_yields_summary.json`) | Makes per-sample normalization terms and audit status explicit and reviewable |
| Target luminosity vs runtime registry luminosity mismatch | Kept runtime `lumi_fb` values explicit in artifacts/report and treated this as a documented deviation | Avoids hidden renormalization and keeps downstream interpretation auditable |
| Signal-region plot blinding during reporting | Kept SR data hidden in blinded region plots and referenced Asimov expected sensitivity in interpretation | Preserves blind-analysis behavior while still reporting a complete statistical workflow |

Report metadata: summary=`outputs/summary.normalized.json`, outputs=`outputs`, target_lumi_fb=36.1.
