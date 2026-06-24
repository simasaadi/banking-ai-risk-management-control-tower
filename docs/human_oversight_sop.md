# Human Oversight SOP

## Purpose

This SOP defines when human review is required for AI-assisted decisions, outputs, escalations, and exceptions.

## Scope

This SOP applies to customer-impacting AI use cases, credit, fraud, collections, complaints, marketing models, generative AI tools, agentic AI workflows, vendor AI tools, and internal HR AI tools.

## When human review is required

Human review is required when:

- The use case has high or critical residual risk
- The AI output affects customer eligibility, access, treatment, or prioritization
- The AI output may create financial, reputational, privacy, conduct, or regulatory harm
- The model confidence is below an approved threshold
- The output involves vulnerable customers
- The output involves complaints, disputes, fraud, collections, or employment screening
- A GenAI response is unsupported by approved knowledge sources
- An agentic workflow proposes a material action
- Monitoring thresholds are breached
- Required evidence is missing or expired

## Escalation triggers

Escalate when residual risk is high or critical, customer harm is suspected, biased output is detected, personal information is exposed, a vendor incident is reported, an agent attempts an unauthorized action, GenAI produces unsafe output, a production control fails, or monitoring detects drift.

## Human reviewer responsibilities

The reviewer must verify the AI output, consider customer context and policy requirements, approve or override the output, document rationale, log exceptions, and report recurring issues.

## Approval authority

| Scenario | Required approver |
|---|---|
| Low-risk internal productivity output | Business owner or delegate |
| Medium-risk operational output | Business owner and risk owner |
| High-risk customer-impacting output | Risk owner and appropriate governance forum |
| Critical residual risk | AI Risk Committee |
| Agentic AI material action | Human approver before execution |
| Privacy or security incident | Privacy or security incident response lead |

## Exception logging

Each exception must include use case ID, date, AI output summary, reason, human decision, reviewer, impact, remediation action, escalation status, and closure evidence.
