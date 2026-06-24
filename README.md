# Banking AI Risk Management Control Tower

This repository is a synthetic portfolio project showing how AI governance can be translated from policy language into practical, auditable controls for a banking environment.

It demonstrates how an enterprise AI risk function could track AI use cases, assess risk, assign accountable owners, define mitigation plans, monitor controls, collect evidence, escalate issues, and report to a risk committee.

All data in this repository is synthetic and created for portfolio demonstration. No real bank, customer, employee, vendor, or production data is used.

## Why this project matters

Banks are adopting machine learning, generative AI, vendor AI tools, and agentic workflows across credit, fraud, operations, customer service, technology, HR, and marketing.

Governance teams need practical operating artifacts that show:

- What AI use cases exist
- Who owns them
- Which use cases are GenAI or agentic AI
- Which risks are inherent versus residual
- Which controls apply
- Which evidence is missing
- Which issues require escalation
- Which framework obligations are covered
- Which risks need committee decisions

## Synthetic AI use cases

| Use case | Main risk angle |
|---|---|
| Credit pre-screening model | Fairness, explainability, model risk, regulatory risk |
| Fraud detection model | False positives, monitoring, drift, customer harm |
| Customer service GenAI chatbot | Hallucination, privacy, prompt injection, escalation |
| Call summarization tool | PII leakage, record accuracy, operational reliance |
| Marketing personalization model | Consent, bias, explainability |
| Collections prioritization model | Fairness, customer harm, conduct risk |
| Internal HR resume screening tool | Discrimination, transparency, vendor risk |
| AI coding assistant | Code security, confidentiality, IP risk |
| Agentic customer complaint triage workflow | Autonomy, tool use, unauthorized action, escalation |
| Vendor AI document extraction tool | Third-party risk, data handling, extraction accuracy |

## Repository structure

- data: synthetic AI inventory, risk, controls, evidence, issues, RACI, framework mapping, and monitoring data
- docs: governance methodology, templates, SOPs, review checklists, incident workflow, and committee report template
- dashboard: Streamlit dashboard
- scripts: data validation script

## Core artifacts

| Artifact | What it demonstrates |
|---|---|
| data/ai_use_case_register.csv | AI inventory, intake, ownership, lifecycle stage, GenAI and agentic AI flagging |
| data/ai_risk_assessment.csv | Structured inherent and residual AI risk assessment |
| data/risk_mitigation_plan.csv | Mitigation planning, control ownership, evidence requirements, escalation |
| data/control_library.csv | Reusable AI governance controls and testing expectations |
| data/evidence_register.csv | Audit-ready evidence tracking |
| data/ai_issue_log.csv | AI issue management, remediation, escalation, closure evidence |
| data/ai_governance_raci.csv | Business, technology, risk, data, privacy, security, vendor, and model ownership |
| data/framework_mapping.csv | Mapping to NIST AI RMF, ISO/IEC 23894, ISO/IEC 42001, model risk, privacy, and security concepts |
| data/model_monitoring_plan.csv | Production monitoring metrics, thresholds, alert triggers, and escalation paths |

## Dashboard pages

- Executive summary
- AI use-case inventory
- Inherent vs residual risk
- Control coverage
- Missing evidence
- High-risk GenAI use cases
- Open issues
- Ownership and RACI
- NIST and ISO mapping
- Committee reporting

## Run locally

Install requirements:

    pip install -r requirements.txt

Run the dashboard:

    streamlit run dashboard/app.py

Run validation:

    python scripts/validate_data.py

## Risk scoring summary

Risk score = impact x likelihood

| Score | Rating |
|---:|---|
| 1 to 5 | Low |
| 6 to 12 | Medium |
| 13 to 19 | High |
| 20 to 25 | Critical |

Residual risk reflects the remaining risk after existing controls are considered.

## Portfolio positioning

This project is designed to show practical experience with:

- AI governance operations
- AI risk assessments
- GenAI and agentic AI risk controls
- Model risk and operational risk concepts
- Control design and testing
- Evidence and audit readiness
- Issue escalation
- Committee reporting
- NIST AI RMF, ISO/IEC 23894, and ISO/IEC 42001 mapping
- Banking use cases involving credit, fraud, customer service, marketing, collections, HR, engineering, and vendor tools

## Disclaimer

This repository is for learning and portfolio demonstration only. The synthetic data and examples do not represent any actual financial institution, customer, employee, vendor, model, risk decision, or control environment.
