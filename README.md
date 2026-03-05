# Skills Pack + regions.yaml

This folder contains:
- `skills/`: Markdown skills files that define an end-to-end, config-driven HEP analysis implementation pattern for a Codex coding agent.
- `analysis/regions.yaml`: an executable region-selection specification and cut flow scaffold.

Usage idea:
1) Put your structured analysis summary at `analysis/analysis.summary.json`.
2) Put your input samples under `inputs/` (or provide a path).
3) Ask Codex to implement the pipeline per `skills/00_INDEX.md` and to treat `analysis/regions.yaml` as the executable selection truth.

Note:
- Any region with `selection: "not_specified"` must cause a fail-fast error until it’s fully specified.

Package documentation:
- `analysis/README.md`: architecture and usage guide for humans and agents running the analysis package.
