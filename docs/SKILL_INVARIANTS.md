# Skill Building Invariants

These invariants are mandatory for every skill in this repository.

## 1. Three-Layer Structure Is Required
Every skill must contain exactly these layers:
- Layer 1 — Physics Policy
- Layer 2 — Workflow Contract
- Layer 3 — Example Implementation (optional in content, but section must exist)

## 2. Physics Policy Must Be Software-Independent
Layer 1 must encode scientific and methodological rules only.
It must not depend on a specific codebase, module name, command, or path.

## 3. Workflow Contract Must Use Logical Artifacts
Layer 2 must describe required outputs as logical artifacts, not hardcoded directory paths.
Examples: fit result artifact, blinding summary artifact, validation table artifact.

## 4. Acceptance Checks Must Be Machine-Verifiable
Layer 2 acceptance checks must be objective and automatable.
Each check must be testable using artifact content or artifact presence/counts.

## 5. Tool Binding Must Be Replaceable
Layer 3 may provide implementation examples (commands, module names, paths),
but replacing Layer 3 must not require changes to Layer 1 or Layer 2.

## 6. Describe WHAT Before HOW
Skills must specify required scientific outcomes and contracts first.
Implementation details are secondary and belong only to Layer 3.

## 7. Autonomous-Agent Usability Is Mandatory
A skill must be executable by an autonomous agent without relying on implicit
human interpretation of missing rules.

## 8. No Directory Layout Assumptions in Core Contracts
Layers 1 and 2 must avoid assumptions about repository structure or filesystem layout.
Directory and filename choices belong only to Layer 3 examples.

## 9. Explicit Success Conditions Are Mandatory
Every skill must define clear completion conditions through acceptance checks.
A stage is incomplete if acceptance checks are not satisfiable.

## 10. Scientific Correctness and Reproducibility Must Be Preserved
Skills must preserve valid HEP methodology, statistical correctness, and reproducible
execution semantics across runs.

## Authoring Template
Use this skeleton for all new skills:

```markdown
# Skill: <skill name>

## Layer 1 — Physics Policy
<software-independent scientific and methodological rules>

## Layer 2 — Workflow Contract
### Required Artifacts
<logical artifacts only>

### Acceptance Checks
<machine-verifiable checks>

## Layer 3 — Example Implementation
<optional implementation examples: commands, modules, paths>
```
