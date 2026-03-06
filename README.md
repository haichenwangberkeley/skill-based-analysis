# Skill-Based Analysis Repository

This repository is designed to be run through an agent-first workflow.  
The expected usage model is: describe the analysis goal to the agent, and let the agent execute the full pipeline end-to-end.

## Agent-First Philosophy

- No manual step-by-step operation is required from users.
- The agent reads repository instructions and skills, executes the workflow, validates outputs, and writes reports.
- Configuration and analysis intent are treated as executable artifacts rather than prose-only notes.

## What This Repository Contains

- `analysis/`
  - Diphoton analysis implementation, including ingestion, object building, region selection, histogramming, fit, significance, plotting, and reporting stages.
- `skills/`
  - Agent workflow contracts and acceptance checks (starting from `skills/00_INDEX.md`).
- `input-data/`
  - ROOT ntuple inputs (`data/` and `MC/`).
- `outputs*/`
  - Generated artifacts from completed runs.
- `reports/`
  - Final and intermediate report documents.
- `tests/`
  - Smoke and unit coverage for core workflow modules.

Detailed package structure and module-level behavior are documented in [analysis/README.md](/global/homes/h/haichen/disk/skill-based-analysis/analysis/README.md).

## How To Run This Framework

Use the agent as the execution interface.

Typical user request pattern:

1. Provide the objective (for example: full diphoton analysis over all samples, significance extraction, and final report generation).
2. Point the agent to the trigger/instruction file if needed (for example `triggerprompt.md`).
3. Ask the agent to complete the workflow and summarize output locations.

The agent is expected to:

- validate the structured analysis definition
- ensure executable regions/categories
- process all samples
- run fit and significance stages
- produce blinded visualization products
- generate a publication-style final report
- document implementation differences from the reference analysis

## Current Run Tracking

The latest full output directory is tracked in:

- [latest_hgg_reference_outdir.txt](/global/homes/h/haichen/disk/skill-based-analysis/reports/latest_hgg_reference_outdir.txt)

Current pointer value:

- `outputs_hgg_reference_20260305T173042Z`

## Reports

Main report index for this repository:

- [reports/README.md](/global/homes/h/haichen/disk/skill-based-analysis/reports/README.md)

Latest publication-style report artifact:

- [final_analysis_report_hgg_reference_20260305.md](/global/homes/h/haichen/disk/skill-based-analysis/reports/final_analysis_report_hgg_reference_20260305.md)
