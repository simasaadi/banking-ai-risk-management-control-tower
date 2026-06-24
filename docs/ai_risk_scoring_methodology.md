# AI Risk Scoring Methodology

## Purpose

This document defines the risk scoring approach used in the Banking AI Risk Management Control Tower.

## Inherent risk

Inherent risk is the level of risk before considering the strength of existing controls.

It reflects the potential impact and likelihood of harm based on the AI use case, business context, data sensitivity, customer impact, decision impact, regulatory exposure, and operational complexity.

## Residual risk

Residual risk is the level of risk remaining after considering existing controls.

Residual risk should reflect whether controls are designed properly, implemented, tested, evidenced, and operating effectively.

## Impact scale

| Score | Rating | Description |
|---:|---|---|
| 1 | Minimal | Limited internal impact, no customer harm, no sensitive data exposure |
| 2 | Minor | Small operational impact, limited rework, low stakeholder exposure |
| 3 | Moderate | Customer inconvenience, internal control gap, or moderate compliance concern |
| 4 | Major | Material customer impact, significant regulatory concern, or major operational disruption |
| 5 | Severe | Potential customer harm, discrimination, confidential data exposure, regulatory breach, or enterprise-level impact |

## Likelihood scale

| Score | Rating | Description |
|---:|---|---|
| 1 | Rare | Highly unlikely based on design, control strength, and history |
| 2 | Unlikely | Possible but not expected under normal conditions |
| 3 | Possible | Could occur under realistic operating conditions |
| 4 | Likely | Expected to occur without strong controls |
| 5 | Almost certain | Expected frequently or already observed |

## Risk score calculation

Risk score = impact x likelihood

## Risk rating thresholds

| Score | Rating | Expected action |
|---:|---|---|
| 1 to 5 | Low | Accept with normal monitoring |
| 6 to 12 | Medium | Mitigate through standard controls and monitoring |
| 13 to 19 | High | Mitigation plan required; risk owner approval required |
| 20 to 25 | Critical | Escalate to AI Risk Committee; no production use until treatment is approved |

## Control effectiveness scale

| Rating | Meaning |
|---|---|
| Weak | Control is informal, untested, incomplete, or lacks evidence |
| Moderate | Control is defined and partly evidenced but may not fully reduce the risk |
| Strong | Control is implemented, tested, owned, evidenced, and monitored |

## Risk acceptance requirements

High or critical residual risks require documented risk acceptance or mitigation approval.

A risk acceptance memo should include use case name, owner, risk description, inherent and residual score, existing controls, known gaps, rationale, expiry date, accountable approver, monitoring requirements, and re-approval conditions.

## Escalation triggers

Escalation is required when residual risk is high or critical, customer harm is plausible, privacy leakage is possible or confirmed, bias is detected, GenAI outputs are unsupported, an agentic workflow can trigger unauthorized action, vendor transparency is insufficient, required evidence is missing, or monitoring thresholds are breached.
