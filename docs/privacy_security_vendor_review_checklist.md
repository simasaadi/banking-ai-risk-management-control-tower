# Privacy, Security, and Vendor AI Review Checklist

## Purpose

This checklist supports review of AI systems involving personal information, confidential banking data, third-party vendors, cloud services, generative AI, or agentic workflows.

## Personal information and confidential data

- Does the use case process personal information?
- Does the use case process sensitive personal information?
- Does the use case process confidential banking data?
- Has the business purpose been documented?
- Has data minimization been applied?
- Are unnecessary fields excluded?
- Are protected or proxy variables reviewed?
- Is data lineage documented?
- Is data retention defined?

## Consent and purpose

- Is the use consistent with the original purpose of collection?
- Is consent required?
- Are consent flags available and reliable?
- Are opt-outs respected?
- Is the use case clearly explained where required?

## Data residency and transfer

- Where is data stored?
- Where is data processed?
- Are cross-border transfers involved?
- Are contractual protections documented?
- Are data residency requirements satisfied?

## Access control

- Is access role-based?
- Is least privilege applied?
- Are privileged users reviewed?
- Are service accounts controlled?
- Are access reviews scheduled?
- Are user activities logged?

## Encryption and safeguards

- Is data encrypted in transit?
- Is data encrypted at rest?
- Are secrets managed securely?
- Are API keys protected?
- Are logs protected?
- Are vulnerability scans completed?

## Vendor AI risk

- Is a vendor involved?
- Has the vendor disclosed the AI system type?
- Has the vendor disclosed data handling practices?
- Is customer data used for vendor model training?
- Are audit rights included?
- Are incident notification requirements included?
- Are subcontractors disclosed?
- Is model performance documentation available?

## Generative AI controls

- Is the system grounded in approved knowledge sources?
- Are unsupported responses blocked or escalated?
- Is prompt injection testing completed?
- Are hallucination tests completed?
- Is human escalation available?
- Are prohibited inputs and outputs documented?

## Agentic AI controls

- Are tools and actions explicitly approved?
- Is least-privilege tool access enforced?
- Are material actions blocked without human approval?
- Are transaction limits defined?
- Are agentic actions logged?
- Is emergency shutdown documented?

## Review decision

| Decision | Meaning |
|---|---|
| Approved | Review complete and no blocking gaps remain |
| Approved with conditions | Use may proceed only with documented conditions |
| Pending evidence | Review cannot close until evidence is provided |
| Escalated | Senior risk or committee decision required |
| Rejected | Use case should not proceed in current form |
