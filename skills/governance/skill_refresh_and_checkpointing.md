---
skill_type: governance
domain: hep_analysis
stage: governance
original_id: "32"
original_filename: "32_SKILL_REFRESH_AND_CHECKPOINTING.md"
---

# Skill: Skill Refresh and Checkpointing

## Layer 1 — Physics Policy
Long, multi-stage analysis runs can drift away from required skill constraints. Skill-policy compliance must therefore be re-validated during execution, not only at run start.

Policy requirements:
- initialize a run-scoped refresh/checkpoint plan before large-scale execution
- re-open relevant skill files at deterministic phase boundaries
- re-open relevant skill files when a fixed elapsed-time interval is exceeded
- re-open relevant skill files after any failure before resuming execution
- emit machine-readable refresh/checkpoint artifacts for every production run
- treat missing refresh/checkpoint artifacts as handoff blockers
- never mark a run handoff-ready when skill checkpoint status is failing or missing

## Layer 2 — Workflow Contract
### Inputs
- active task objective and selected analysis JSON
- list of skills used in the run
- canonical phase boundaries
- execution timeline and failure/recovery events
- required output-artifact matrix for each phase

### Definitions
- refresh event: re-open and re-check the skill files relevant to the next execution phase
- checkpoint: a refresh event plus an artifact-completeness assertion for that phase

### Required Triggers
1. `run_start`:
   - create plan artifact and first refresh entry
2. `phase_boundary`:
   - refresh before entering each major phase
3. `elapsed_interval`:
   - refresh when elapsed time since previous refresh exceeds policy interval (default 20 minutes)
4. `failure_recovery`:
   - refresh immediately after a technical failure and before resuming
5. `pre_handoff_gate`:
   - refresh and run final compliance assertion before handoff classification

### Required Artifacts
- `outputs/report/skill_refresh_plan.json`:
  - `policy_version`
  - `refresh_interval_minutes`
  - `checkpoint_ids` (ordered list)
  - `checkpoint_requirements` (mapping: checkpoint -> skills + required artifacts)
  - `status`
- `outputs/report/skill_refresh_log.jsonl`:
  - one JSON object per line with:
    - `timestamp_utc`
    - `checkpoint_id`
    - `trigger`
    - `skills_reloaded` (list of paths)
    - `required_artifacts_checked` (list)
    - `decision` (`pass`, `warn`, or `fail`)
    - `notes`
- `outputs/report/skill_checkpoint_status.json`:
  - `status` (`pass` or `fail`)
  - `checkpoints` (list of per-checkpoint results)
  - `missing_artifacts` (list)
  - `interval_violations` (list)
  - `recovery_refresh_violations` (list)
  - `handoff_blocker` (bool)
  - `notes`

### Minimum Checkpoint IDs
- `preflight_ready`
- `summary_validated`
- `execution_contract_recorded`
- `selection_hist_complete`
- `fit_complete`
- `report_complete`
- `handoff_gate`

### Decision Logic
1. Build checkpoint plan:
   - map each checkpoint ID to required skills and required output artifacts
2. At each trigger:
   - re-open the mapped skills
   - record a refresh event in `skill_refresh_log.jsonl`
3. For each checkpoint:
   - assert required artifacts exist and are readable
   - record pass/fail outcome
4. After failures:
   - require a `failure_recovery` refresh event before any resumed stage output is accepted
5. Finalize status:
   - if any mandatory checkpoint fails, set `status = fail` and `handoff_blocker = true`

### Acceptance Checks
- all three refresh artifacts exist and are readable
- plan declares all minimum checkpoint IDs
- each minimum checkpoint ID appears in both refresh log and status artifact
- no elapsed interval violations unless explicitly justified in `notes`
- every failure event has a subsequent `failure_recovery` refresh before resumed stage completion
- final handoff review includes skill-refresh gate result from `skill_checkpoint_status.json`
- if `skill_checkpoint_status.json.status != pass`, run must be classified as not handoff-ready

## Layer 3 — Example Implementation
### Suggested `skill_refresh_plan.json` Skeleton
```json
{
  "policy_version": "1.0",
  "refresh_interval_minutes": 20,
  "checkpoint_ids": [
    "preflight_ready",
    "summary_validated",
    "execution_contract_recorded",
    "selection_hist_complete",
    "fit_complete",
    "report_complete",
    "handoff_gate"
  ],
  "checkpoint_requirements": {
    "preflight_ready": {
      "skills": [
        "governance/agent_pre_flight_fact_check.md",
        "governance/skill_refresh_and_checkpointing.md"
      ],
      "artifacts": [
        "outputs/report/preflight_fact_check.json"
      ]
    }
  },
  "status": "active"
}
```

### Related Skills
- `governance/agent_pre_flight_fact_check.md`
- `interfaces/json_spec_driven_execution.md`
- `infrastructure/smoke_tests_and_reproducibility.md`
- `core_pipeline/final_report_review_and_handoff.md`

