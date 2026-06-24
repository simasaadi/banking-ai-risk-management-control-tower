# AI Incident Response Workflow

## Purpose

This workflow defines how AI-related incidents are identified, triaged, escalated, remediated, and closed.

## Incident categories

- Hallucination incident
- PII leakage
- Biased or discriminatory output
- Unauthorized agent action
- Failed control
- Model drift
- Vendor issue
- Customer harm event
- Security event involving AI system

## Severity levels

| Severity | Description | Required action |
|---|---|---|
| Low | Limited internal issue with no customer impact | Log and remediate through normal process |
| Medium | Operational issue or control gap with limited impact | Assign owner and due date |
| High | Potential customer, privacy, fairness, regulatory, or operational harm | Escalate to risk owner |
| Critical | Confirmed material harm, unauthorized action, major privacy issue, or systemic failure | Activate incident response and notify committee |

## General workflow

1. Identify the incident or control failure.
2. Create an issue in the AI issue log.
3. Assign severity.
4. Assign accountable owner.
5. Preserve relevant evidence.
6. Stop, restrict, or roll back the AI use case if needed.
7. Notify business, technology, risk, privacy, security, and vendor owners as applicable.
8. Define remediation action.
9. Track remediation to closure.
10. Validate closure evidence.
11. Update controls, monitoring, and risk assessment.
12. Report material incidents to the AI Risk Committee.

## Specific workflows

### Hallucination incident

Capture prompt, response, timestamp, system version, and user path. Assess impact, restrict the response category if needed, update grounding or refusal logic, retest guardrails, and document closure evidence.

### PII leakage

Contain exposure, notify privacy lead, preserve logs, assess affected data, remove exposed information, update masking and access controls, and document closure.

### Biased output

Pause use if harm is plausible, validate the output, perform segmented analysis, review features and proxy variables, define mitigation, and obtain approval before restart.

### Unauthorized agent action

Disable agent tool access, preserve tool call logs, notify security and AI risk, assess impact, update permission matrix, add human confirmation, retest tool boundaries, and obtain approval before reactivation.

### Model drift

Validate drift signal, assess business impact, increase monitoring, recalibrate or roll back, document decision, and update model card and risk assessment.

### Vendor issue

Notify third-party risk, assess contractual obligations, restrict data sharing if needed, request root-cause analysis, document remediation, and escalate unresolved high-risk vendor gaps.
