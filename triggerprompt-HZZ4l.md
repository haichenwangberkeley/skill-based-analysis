You are a Codex analysis agent working in the current workspace

Follow below instruction to complete a Higgs to four-lepton search using the 2012 ATLAS open data samples (7 TeV and 8 TeV, combined)

What is available
- Skills pack: skills/*.md (start with skills/00_INDEX.md and follow all skill contracts)
- Example placeholder region selections: analysis/regions.yaml
- Structured analysis summary (authoritative reproduction target): analysis/ATLAS_2012_HZZ4l_discovery.analysis.jsonl
- Input ROOT ntuples (symlinks to open data): input-data/data and input-data/MC
- Repo docs: README.md


Hard constraints
- Do NOT quote or copy raw text from analysis/ATLAS_2012_HZZ4l_discovery.analysis.jsonl verbatim in the final report.
- You MUST use analysis/ATLAS_2012_HZZ4l_discovery.analysis.jsonl as the primary implementation target and
  implement the analysis to closely reproduce it with available open-data observables.
- Lepton identification, impact-parameter, and isolation variables may differ from the reference analysis era. You must inspect the
  actual branches present in the ROOT ntuples and determine the closest usable equivalents.
- If anything in analysis/ATLAS_2012_HZZ4l_discovery.analysis.jsonl is inconsistent with what is available
  in the open data samples (missing variables, different definitions, unavailable observables, etc.), you are allowed
  to substitute the closest feasible replacement that exists in the dataset.

Compatibility rule
- Any substitutions or approximations must be explicitly documented.
- The justification must be written in a dedicated section of the final report titled:

  "Implementation Differences from Reference Analysis"

- For each substitution include:
  - the reference concept (without quoting the JSONL)
  - the observable available in the open data
  - the reasoning for the replacement
  - the expected impact on the analysis if relevant

Mission
Complete the analysis. Implement and execute an end-to-end H→ZZ(*)→4l analysis pipeline from input-data/ to outputs/, fully reproducible and CLI-driven,
guided by the skills pack and analysis/ATLAS_2012_HZZ4l_discovery.analysis.jsonl as the reference target.
analysis/regions.yaml is a placeholder example and should be updated/replaced as needed to achieve close reproduction.
Run this over all samples.

Definition of done:

The analysis must be completed. All data is processed, expected discovery significance shall be determined, a paper quality report is written.
