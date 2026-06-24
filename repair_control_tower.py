from pathlib import Path
import csv
import textwrap

ROOT = Path.cwd()

def write_text(path, content):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")

def write_csv(path, fieldnames, rows):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

for folder in ["data", "docs", "dashboard", "scripts", "assets"]:
    (ROOT / folder).mkdir(exist_ok=True)

# ----------------------------
# DATA FILES
# ----------------------------

use_cases = [
    ["UC-001","Credit pre-screening model","Retail Lending","Customer decision support","Supervised ML classification","No","No","Director, Retail Credit Strategy","Manager, Decisioning Platforms","Senior Manager, Model Risk","Lead, Credit Bureau Data","No","High","Influences credit eligibility routing and pre-screening","Pilot","Conditional approval","2026-01-15","2026-05-10"],
    ["UC-002","Fraud detection model","Fraud Operations","Transaction monitoring","Anomaly detection and supervised ML","No","No","Director, Fraud Operations","Manager, Fraud Analytics Engineering","Senior Manager, Operational Risk","Lead, Transaction Data","No","High","Flags transactions for review or temporary blocking","Production","Approved with monitoring","2025-11-20","2026-05-28"],
    ["UC-003","Customer service GenAI chatbot","Digital Banking","Customer interaction","Generative AI large language model","Yes","No","Director, Digital Client Experience","Manager, Conversational AI","Senior Manager, AI Governance","Lead, Customer Interaction Data","Yes","High","Provides banking guidance and routes service requests","Controlled pilot","Pending risk committee approval","2026-02-05","2026-06-01"],
    ["UC-004","Call summarization tool","Contact Centre","Employee productivity","Generative AI summarization","Yes","No","Senior Manager, Contact Centre Operations","Lead, Speech Analytics Platform","Manager, Records and Operational Risk","Lead, Voice and Transcript Data","Yes","Medium","Creates call records used for follow-up and audit review","Pilot","Conditional approval","2026-02-18","2026-05-21"],
    ["UC-005","Marketing personalization model","Marketing Analytics","Personalization and targeting","Propensity model","No","No","Director, Marketing Strategy","Manager, Customer Analytics","Senior Manager, Privacy Risk","Lead, Customer Profile Data","No","Medium","Personalizes offers and campaign prioritization","Production","Approved with conditions","2025-12-03","2026-05-17"],
    ["UC-006","Collections prioritization model","Collections","Customer treatment prioritization","Predictive scoring model","No","No","Director, Collections Strategy","Manager, Collections Platforms","Senior Manager, Conduct Risk","Lead, Delinquency Data","No","High","Prioritizes collections outreach and treatment paths","Assessment","Not approved","2026-03-04","2026-06-05"],
    ["UC-007","Internal HR resume screening tool","Human Resources","Internal decision support","NLP classifier","No","No","Director, Talent Acquisition","Manager, HR Systems","Senior Manager, Employment Risk","Lead, HR Data","Yes","Low","Ranks applicants for recruiter review","Intake","Pending assessment","2026-04-02","2026-05-30"],
    ["UC-008","AI coding assistant","Technology","Developer productivity","Generative AI code assistant","Yes","No","Director, Software Engineering","Lead, Developer Platforms","Senior Manager, Technology Risk","Lead, Source Code Governance","Yes","Low","Suggests code and documentation for developer review","Production","Approved with guardrails","2025-10-12","2026-05-24"],
    ["UC-009","Agentic customer complaint triage workflow","Client Care","Agentic workflow","GenAI agent with workflow tools","Yes","Yes","Director, Client Care","Manager, Workflow Automation","Senior Manager, AI Governance","Lead, Complaint Management Data","Yes","High","Classifies complaints, drafts responses, and routes escalations","Design review","Risk review required","2026-04-16","2026-06-10"],
    ["UC-010","Vendor AI document extraction tool","Commercial Banking Operations","Document processing","Vendor OCR and ML extraction","No","No","Director, Commercial Operations","Manager, Document Platforms","Senior Manager, Third-Party Risk","Lead, Commercial Document Data","Yes","Medium","Extracts fields from customer documents for operations review","Production","Approved with vendor monitoring","2025-09-25","2026-05-19"],
]

use_case_fields = [
    "use_case_id","use_case_name","business_unit","use_case_type","ai_type","genai_flag","agentic_ai_flag",
    "business_owner","technology_owner","risk_owner","data_owner","vendor_involved","customer_impact",
    "decision_impact","lifecycle_stage","approval_status","date_submitted","last_review_date"
]
write_csv("data/ai_use_case_register.csv", use_case_fields, [dict(zip(use_case_fields, r)) for r in use_cases])

risk_raw = [
    ["UC-001","Fairness and bias","Credit pre-screening may produce disparate outcomes across protected or proxy demographic groups.",5,4,"Initial bias review, feature review, adverse impact testing","Moderate",4,3,"Mitigate"],
    ["UC-001","Explainability","Applicants and reviewers may not receive clear reasons for model-influenced routing decisions.",4,4,"Model documentation and reason code design","Moderate",3,3,"Mitigate"],
    ["UC-002","Customer harm","Fraud false positives may block legitimate transactions and create customer disruption.",5,4,"Human review queue and customer dispute process","Strong",3,3,"Mitigate"],
    ["UC-002","Model drift","Fraud patterns may shift, reducing detection accuracy or increasing false positives.",4,5,"Monthly performance monitoring","Moderate",3,3,"Mitigate"],
    ["UC-003","Hallucination","Chatbot may generate inaccurate banking information or unsupported product guidance.",5,4,"Retrieval grounding and restricted response policy","Moderate",4,3,"Mitigate"],
    ["UC-003","Prompt injection","User input may manipulate the model into bypassing instructions or exposing restricted content.",5,4,"Prompt filtering and red-team testing","Weak",4,4,"Escalate"],
    ["UC-004","Data privacy","Call summaries may retain personal information not required for the business purpose.",5,3,"PII minimization checklist","Moderate",3,3,"Mitigate"],
    ["UC-004","Data quality","Generated summaries may omit key facts or introduce inaccurate records.",4,4,"Sample QA review","Moderate",3,3,"Mitigate"],
    ["UC-005","Data privacy","Personalization may use customer data without clear consent or purpose alignment.",5,3,"Consent flag validation","Strong",3,2,"Mitigate"],
    ["UC-005","Fairness and bias","Campaign targeting may exclude or over-target customer segments unfairly.",4,3,"Segment outcome review","Moderate",3,2,"Mitigate"],
    ["UC-006","Customer harm","Collections prioritization may intensify collections contact for customers in hardship.",5,4,"Conduct risk review","Moderate",4,3,"Escalate"],
    ["UC-006","Fairness and bias","Collections prioritization may create unequal treatment or hardship for vulnerable customers.",5,4,"Manual review and vulnerable customer policy","Moderate",4,3,"Mitigate"],
    ["UC-007","Fairness and bias","Resume screening may disadvantage candidates based on proxies for protected characteristics.",5,4,"Vendor fairness questionnaire","Weak",4,4,"Escalate"],
    ["UC-007","Third-party/vendor risk","Vendor model details and training data may not be sufficiently transparent.",4,4,"Third-party intake","Moderate",3,3,"Mitigate"],
    ["UC-008","Security","Generated code may introduce insecure patterns or dependency vulnerabilities.",5,4,"Secure coding review and SAST scanning","Strong",3,3,"Mitigate"],
    ["UC-008","Data privacy","Developers may paste confidential code, credentials, or customer data into the tool.",5,3,"Usage policy and DLP monitoring","Moderate",4,2,"Mitigate"],
    ["UC-009","Unauthorized agent action","Agent may trigger workflow actions without sufficient authorization or human approval.",5,5,"Tool permission design","Weak",5,4,"Escalate"],
    ["UC-009","Prompt injection","External complaint text may manipulate the agent into unsafe workflow behavior.",5,4,"Prompt injection test suite","Weak",4,4,"Escalate"],
    ["UC-009","Human oversight","Complaint decisions may be finalized without appropriate escalation.",5,4,"Human-in-the-loop design","Moderate",4,3,"Mitigate"],
    ["UC-010","Third-party/vendor risk","Vendor extraction model may not meet internal AI governance and audit expectations.",4,4,"Vendor AI review and contract clauses","Moderate",3,3,"Mitigate"],
    ["UC-010","Data quality","Incorrect extraction may create processing errors or downstream reporting issues.",4,4,"Sampling QA and exception queue","Moderate",3,3,"Mitigate"],
]

def rating(score):
    if score >= 20:
        return "Critical"
    if score >= 13:
        return "High"
    if score >= 6:
        return "Medium"
    return "Low"

risk_fields = [
    "risk_id","assessment_id","use_case_id","risk_category","risk_description","inherent_impact",
    "inherent_likelihood","inherent_risk_score","existing_controls","control_effectiveness",
    "residual_impact","residual_likelihood","residual_risk_score","residual_risk_rating",
    "risk_decision","reviewer","review_date"
]

risk_rows = []
for i, r in enumerate(risk_raw, 1):
    uc, cat, desc, ii, il, controls, eff, ri, rl, decision = r
    residual_score = ri * rl
    risk_rows.append({
        "risk_id": f"RISK-{i:03d}",
        "assessment_id": f"ASM-{i:03d}",
        "use_case_id": uc,
        "risk_category": cat,
        "risk_description": desc,
        "inherent_impact": ii,
        "inherent_likelihood": il,
        "inherent_risk_score": ii * il,
        "existing_controls": controls,
        "control_effectiveness": eff,
        "residual_impact": ri,
        "residual_likelihood": rl,
        "residual_risk_score": residual_score,
        "residual_risk_rating": rating(residual_score),
        "risk_decision": decision,
        "reviewer": "AI Risk Management Office",
        "review_date": "2026-06-12"
    })
write_csv("data/ai_risk_assessment.csv", risk_fields, risk_rows)

controls_raw = [
    ["CTRL-001","AI use-case intake approval","Ensure every AI use case is inventoried, risk-ranked, owned, and approved before development or deployment.","Process control","Governance","Mandatory intake form, ownership assignment, preliminary risk tiering, and approval routing.","Completed intake record and approval decision","Per use case and annual refresh","AI Risk Management Office","NIST AI RMF Govern; ISO/IEC 42001 Planning"],
    ["CTRL-002","Data quality review","Confirm that data is complete, accurate, representative, traceable, and fit for intended AI use.","Preventive","Data quality","Data profiling, lineage review, missingness checks, outlier analysis, and data quality issue logging.","Data quality report and issue resolution evidence","Before launch and quarterly","Data Owner","NIST AI RMF Map; ISO/IEC 23894 Risk Identification"],
    ["CTRL-003","Privacy impact review","Assess privacy, consent, data minimization, purpose limitation, retention, and disclosure risks.","Preventive","Data privacy","Privacy checklist and impact assessment for use cases involving personal information.","Privacy checklist or privacy impact assessment","Before launch and material change","Privacy Reviewer","Privacy/security controls; ISO/IEC 42001 Support"],
    ["CTRL-004","Security review","Validate secure architecture, access control, encryption, logging, vulnerability management, and threat model coverage.","Preventive","Security","Security-by-design review for AI systems, integrations, APIs, and vendor connections.","Security assessment and remediation record","Before launch and annual","Security Reviewer","NIST AI RMF Govern; ISO/IEC 42001 Operation"],
    ["CTRL-005","Vendor AI review","Assess third-party AI governance, data handling, explainability, contractual protections, and audit rights.","Preventive","Third-party/vendor risk","Vendor questionnaire, model transparency review, data residency confirmation, and contractual control mapping.","Vendor review record and contract control evidence","Before onboarding and annual","Third-Party Risk Reviewer","ISO/IEC 42001 Supplier Management; ISO/IEC 23894 Risk Treatment"],
    ["CTRL-006","Bias/fairness review","Identify and mitigate potential unfair outcomes or disparate impact.","Preventive","Fairness and bias","Fairness metric selection, protected/proxy variable review, segmented testing, and mitigation plan.","Fairness test results and mitigation sign-off","Before launch and quarterly","Model Risk Reviewer","NIST AI RMF Measure; ISO/IEC 23894 Risk Analysis"],
    ["CTRL-007","Explainability documentation","Document model purpose, drivers, limitations, interpretability approach, and user-facing explanation requirements.","Process control","Explainability","Model card or system card with intended use, limitations, feature drivers, and explanation design.","Approved model card or system card","Before launch and annual","Model Owner","NIST AI RMF Map and Measure; ISO/IEC 42001 Documentation"],
    ["CTRL-008","Human oversight checkpoint","Ensure high-risk outputs are reviewed, overridden, or escalated by accountable humans.","Human-in-the-loop","Human oversight","Defined review thresholds, escalation paths, override procedures, and decision logging.","Oversight SOP and sample decision logs","Before launch and monthly sample","Business Owner","NIST AI RMF Manage; ISO/IEC 23894 Risk Treatment"],
    ["CTRL-009","Model monitoring","Detect performance degradation, exception trends, and control failures after deployment.","Detective","Model performance","Ongoing review of model metrics, false positive/negative rates, exceptions, and complaints.","Monitoring dashboard and monthly report","Monthly","Technology Owner","NIST AI RMF Measure and Manage"],
    ["CTRL-010","Drift monitoring","Identify changes in data distribution, population, behavior, or model output patterns.","Detective","Model drift","Population stability, feature drift, prediction drift, and alert thresholds.","Drift report and escalation record","Monthly or real-time for high-risk systems","Model Owner","NIST AI RMF Measure; ISO/IEC 23894 Monitoring"],
    ["CTRL-011","GenAI guardrail testing","Validate that GenAI outputs follow policy, remain grounded, and avoid unsafe guidance.","Technical guardrail","Hallucination","Red-team testing, refusal behavior testing, grounding checks, and unsafe content evaluation.","Guardrail test results and defect log","Before launch and monthly","AI Product Owner","NIST AI RMF Measure and Manage; ISO/IEC 42001 Operation"],
    ["CTRL-012","Prompt injection testing","Assess whether malicious or manipulative prompts can bypass system instructions or access restricted data.","Technical guardrail","Prompt injection","Prompt injection test suite covering direct, indirect, jailbreak, and tool manipulation patterns.","Prompt injection test report","Before launch and monthly","Security Reviewer","NIST AI RMF Measure; Security controls"],
    ["CTRL-013","Audit logging","Maintain traceable records of AI inputs, outputs, decisions, overrides, approvals, and exceptions.","Detective","Operational risk","Logging standard covering system events, human decisions, escalations, and evidence retention.","Audit log sample and retention configuration","Continuous with quarterly testing","Technology Owner","ISO/IEC 42001 Documentation and Operation"],
    ["CTRL-014","Residual risk approval","Ensure residual risks are explicitly accepted, mitigated, transferred, or escalated by accountable owners.","Process control","Governance","Risk decision workflow, approval authority, risk acceptance memo, and expiry date.","Risk acceptance memo or committee decision","Per material risk and annual refresh","Risk Owner","NIST AI RMF Govern and Manage; ISO/IEC 23894 Risk Treatment"],
    ["CTRL-015","Issue escalation","Ensure AI issues are logged, assigned, remediated, escalated, and closed with evidence.","Corrective","Operational risk","Severity matrix, SLA, escalation trigger, owner assignment, and closure evidence requirement.","Issue log and closure evidence","Weekly for open high/critical issues","AI Risk Management Office","NIST AI RMF Manage; ISO/IEC 42001 Improvement"],
    ["CTRL-016","Agent tool permission control","Restrict agentic AI systems to approved tools, approved data, and approved action boundaries.","Technical guardrail","Unauthorized agent action","Least-privilege tool access, transaction limits, confirmation requirements, and blocked action categories.","Tool permission matrix and test evidence","Before launch and monthly","Technology Owner","NIST AI RMF Manage; ISO/IEC 42001 Operation"]
]
control_fields = ["control_id","control_name","control_objective","control_type","risk_category","control_description","evidence_required","testing_frequency","control_owner","mapped_framework"]
write_csv("data/control_library.csv", control_fields, [dict(zip(control_fields, r)) for r in controls_raw])

mitigation_fields = ["mitigation_id","use_case_id","risk_id","mitigation_action","control_type","control_owner","target_completion_date","implementation_status","residual_risk_after_mitigation","evidence_required","escalation_required"]
mitigation_rows = []
for i, r in enumerate(risk_rows, 1):
    high = r["residual_risk_rating"] in ["High","Critical"] or r["risk_decision"] == "Escalate"
    mitigation_rows.append({
        "mitigation_id": f"MIT-{i:03d}",
        "use_case_id": r["use_case_id"],
        "risk_id": r["risk_id"],
        "mitigation_action": f"Implement documented mitigation for {r['risk_category']} risk, including assigned owner, control test, and evidence before approval.",
        "control_type": "Technical guardrail" if r["risk_category"] in ["Prompt injection","Unauthorized agent action","Hallucination","Security"] else "Process control",
        "control_owner": "AI Risk Management Office" if high else "Use Case Owner",
        "target_completion_date": "2026-07-31" if high else "2026-08-30",
        "implementation_status": "In progress" if high else "Planned",
        "residual_risk_after_mitigation": "Medium" if high else r["residual_risk_rating"],
        "evidence_required": "Testing results, approval record, monitoring evidence, and updated model/system card",
        "escalation_required": "Yes" if high else "No"
    })
write_csv("data/risk_mitigation_plan.csv", mitigation_fields, mitigation_rows)

evidence_raw = [
    ["EV-001","UC-001","CTRL-006","Credit pre-screening fairness test results","Test results","Model Risk Reviewer","Received","2026-05-08","2026-08-08","Yes","Initial fairness test completed."],
    ["EV-002","UC-001","CTRL-007","Credit model card","Model card","Model Owner","Received","2026-05-09","2027-05-09","Yes","Includes intended use and limitations."],
    ["EV-003","UC-003","CTRL-011","Chatbot GenAI guardrail test results","Test results","AI Product Owner","Pending","","2026-07-05","No","Required before approval."],
    ["EV-004","UC-003","CTRL-012","Chatbot prompt injection test report","Test results","Security Reviewer","Missing","","2026-07-05","No","Critical evidence gap."],
    ["EV-005","UC-004","CTRL-003","Call summarization privacy impact review","Privacy impact assessment","Privacy Reviewer","Received","2026-05-20","2026-11-20","Yes","Retention rule reviewed."],
    ["EV-006","UC-006","CTRL-014","Collections risk committee decision","Committee decision","Risk Owner","Missing","","2026-07-12","No","Escalated due to customer harm risk."],
    ["EV-007","UC-007","CTRL-006","HR adverse impact analysis","Test results","Employment Risk Reviewer","Missing","","2026-07-25","No","Required before pilot."],
    ["EV-008","UC-008","CTRL-004","AI coding assistant security review","Security assessment","Security Reviewer","Received","2026-05-22","2026-11-22","Yes","Includes SAST requirements."],
    ["EV-009","UC-009","CTRL-016","Agent tool permission matrix","Technical design evidence","Technology Owner","Pending","","2026-07-02","No","Critical evidence before pilot."],
    ["EV-010","UC-009","CTRL-012","Agent prompt injection and tool abuse test report","Test results","Security Reviewer","Missing","","2026-07-02","No","Escalated to AI risk committee."],
    ["EV-011","UC-010","CTRL-005","Vendor document extraction AI review","Vendor review","Third-Party Risk Reviewer","Received","2026-05-18","2026-11-18","Yes","Vendor contract includes audit rights."]
]
evidence_fields = ["evidence_id","use_case_id","control_id","evidence_name","evidence_type","evidence_owner","evidence_status","date_received","expiry_or_review_date","audit_ready_flag","notes"]
write_csv("data/evidence_register.csv", evidence_fields, [dict(zip(evidence_fields, r)) for r in evidence_raw])

issue_raw = [
    ["ISS-001","UC-003","Prompt injection testing evidence is missing for customer service GenAI chatbot.","Prompt injection","High","2026-06-03","Security Reviewer","Complete test suite and remediate failed cases before approval.","2026-07-05","Open","Escalated to AI Risk Committee","Pending"],
    ["ISS-002","UC-009","Agentic workflow lacks final approved tool permission matrix.","Unauthorized agent action","Critical","2026-06-06","Technology Owner","Define least-privilege tool access and human confirmation points.","2026-07-02","Open","Escalated to AI Risk Committee","Pending"],
    ["ISS-003","UC-006","Collections model may increase outreach intensity for vulnerable customers.","Customer harm","High","2026-06-04","Conduct Risk Reviewer","Complete vulnerable customer review and adjust treatment strategy.","2026-07-12","Open","Escalated to Conduct Risk","Pending"],
    ["ISS-004","UC-007","Vendor resume screening tool has incomplete adverse impact documentation.","Fairness and bias","High","2026-06-01","Employment Risk Reviewer","Obtain vendor documentation and complete independent adverse impact analysis.","2026-07-25","Open","Escalated to HR Risk","Pending"],
    ["ISS-005","UC-008","Developer pasted internal API details into AI coding assistant during pilot sample.","Data privacy","Medium","2026-05-18","Technology Owner","Refresh developer training and strengthen DLP rule.","2026-06-20","Closed","Not escalated","Training record and DLP rule update"]
]
issue_fields = ["issue_id","use_case_id","issue_description","issue_category","severity","date_identified","owner","remediation_action","due_date","status","escalation_status","closure_evidence"]
write_csv("data/ai_issue_log.csv", issue_fields, [dict(zip(issue_fields, r)) for r in issue_raw])

raci_fields = ["use_case_id","business_owner","technology_owner","risk_owner","data_owner","privacy_reviewer","security_reviewer","vendor_reviewer","model_reviewer","final_approver"]
raci_rows = []
for r in use_cases:
    d = dict(zip(use_case_fields, r))
    raci_rows.append({
        "use_case_id": d["use_case_id"],
        "business_owner": d["business_owner"],
        "technology_owner": d["technology_owner"],
        "risk_owner": d["risk_owner"],
        "data_owner": d["data_owner"],
        "privacy_reviewer": "Privacy Office",
        "security_reviewer": "Cybersecurity Risk",
        "vendor_reviewer": "Third-Party Risk" if d["vendor_involved"] == "Yes" else "Not applicable",
        "model_reviewer": "Model Risk Management",
        "final_approver": "AI Risk Committee" if d["customer_impact"] == "High" or d["genai_flag"] == "Yes" else "Business Risk Owner"
    })
write_csv("data/ai_governance_raci.csv", raci_fields, raci_rows)

mapping_raw = [
    ["NIST AI RMF","Govern","AI governance structures, policies, accountability, and risk management processes are established.","CTRL-001","Completed intake record and approval decision","data/ai_use_case_register.csv"],
    ["NIST AI RMF","Map","AI context, intended use, stakeholders, benefits, and risks are documented.","CTRL-007","Approved model card or system card","docs/model_card_template.md"],
    ["NIST AI RMF","Measure","Risks are analyzed using repeatable metrics and test methods.","CTRL-006","Fairness test results","data/ai_risk_assessment.csv"],
    ["NIST AI RMF","Manage","Risks are prioritized, treated, monitored, and escalated.","CTRL-014","Risk decision and mitigation plan","data/risk_mitigation_plan.csv"],
    ["ISO/IEC 23894","Risk Identification","AI risks are identified across lifecycle, data, model, operations, and stakeholders.","CTRL-001","Risk assessment record","data/ai_risk_assessment.csv"],
    ["ISO/IEC 23894","Risk Analysis","Impact and likelihood are assessed to estimate risk level.","CTRL-014","Risk scoring methodology","docs/ai_risk_scoring_methodology.md"],
    ["ISO/IEC 23894","Risk Treatment","Controls and mitigation actions are selected, owned, and tracked.","CTRL-015","Mitigation plan","data/risk_mitigation_plan.csv"],
    ["ISO/IEC 42001","Context and Scope","AI management system scope and use-case inventory are maintained.","CTRL-001","AI inventory","data/ai_use_case_register.csv"],
    ["ISO/IEC 42001","Leadership and Accountability","Accountable owners and approvers are assigned.","CTRL-001","RACI and final approval","data/ai_governance_raci.csv"],
    ["ISO/IEC 42001","Operation","Operational controls are implemented for AI systems.","CTRL-008","Human oversight SOP","docs/human_oversight_sop.md"],
    ["Model risk governance concepts","Ongoing monitoring","Production models are monitored for performance, drift, exceptions, and issues.","CTRL-009","Monitoring report","data/model_monitoring_plan.csv"],
    ["Privacy/security controls","Privacy by design","Personal information use is minimized, justified, consent-aligned, and reviewed.","CTRL-003","Privacy checklist","docs/privacy_security_vendor_review_checklist.md"],
    ["Privacy/security controls","Third-party risk","Vendor AI systems are reviewed for data handling, auditability, security, and contractual controls.","CTRL-005","Vendor review","docs/privacy_security_vendor_review_checklist.md"]
]
mapping_fields = ["framework","framework_domain","requirement_or_principle","internal_control_id","evidence_required","repo_artifact"]
write_csv("data/framework_mapping.csv", mapping_fields, [dict(zip(mapping_fields, r)) for r in mapping_raw])

monitoring_raw = [
    ["UC-001","Approval rate disparity ratio","No segment below 0.80 relative selection ratio without documented justification","Quarterly","Model Risk Reviewer","Threshold breach or unexplained segment gap","Model Risk -> AI Risk Committee","2026-05-10","Active"],
    ["UC-002","False positive rate","Segment-level false positive rate does not exceed approved tolerance","Monthly","Fraud Analytics Lead","Threshold breach for any monitored segment","Fraud Ops -> Operational Risk","2026-06-01","Active"],
    ["UC-002","Model drift","Population stability index below approved threshold","Monthly","Model Owner","PSI exceeds threshold","Model Owner -> Model Risk","2026-06-01","Active"],
    ["UC-003","Unsupported GenAI response rate","Less than 2 percent in controlled sample","Weekly during pilot","AI Product Owner","Unsupported response rate above threshold","AI Product Owner -> AI Risk Committee","2026-06-01","Pending"],
    ["UC-003","Privacy leakage incidents","Zero confirmed leakage incidents","Continuous","Privacy Reviewer","Any confirmed leakage","Privacy -> Incident Response","2026-06-01","Pending"],
    ["UC-004","Summary accuracy QA score","Minimum 95 percent key fact accuracy in sample","Weekly during pilot","Contact Centre QA Lead","QA score below threshold","Contact Centre -> Operational Risk","2026-05-21","Active"],
    ["UC-005","Consent rule exception rate","Zero campaigns using records without valid consent","Per campaign","Data Owner","Any consent exception","Privacy -> Marketing Risk","2026-05-17","Active"],
    ["UC-006","Vulnerable customer outreach rate","No unexplained increase relative to approved treatment strategy","Monthly","Conduct Risk Reviewer","Threshold breach","Conduct Risk -> AI Risk Committee","2026-06-05","Pending"],
    ["UC-007","Adverse impact ratio","No monitored group below approved threshold without documented mitigation","Before pilot and quarterly","Employment Risk Reviewer","Threshold breach","HR Risk -> Legal/Risk Committee","2026-05-30","Pending"],
    ["UC-008","Sensitive data DLP alerts","Zero high-severity confidential data paste events","Continuous","Technology Owner","High severity DLP alert","Technology Risk -> Security","2026-05-24","Active"],
    ["UC-009","Unauthorized tool action attempts","Zero successful unauthorized actions","Continuous during pilot","Technology Owner","Any successful unauthorized action","Incident Response -> AI Risk Committee","2026-06-10","Pending"],
    ["UC-009","Prompt injection pass rate","100 percent of critical test cases blocked","Before pilot and monthly","Security Reviewer","Any critical failure","Security -> AI Risk Committee","2026-06-10","Pending"],
    ["UC-010","Extraction field accuracy","Minimum 98 percent accuracy for critical fields","Monthly","Commercial Operations Owner","Accuracy below threshold","Operations -> Vendor Risk","2026-05-19","Active"]
]
monitoring_fields = ["use_case_id","monitoring_metric","threshold","monitoring_frequency","owner","alert_trigger","escalation_path","last_review_date","status"]
write_csv("data/model_monitoring_plan.csv", monitoring_fields, [dict(zip(monitoring_fields, r)) for r in monitoring_raw])

# ----------------------------
# DOCS
# ----------------------------

write_text("README.md", """
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
""")

write_text("docs/ai_risk_scoring_methodology.md", """
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
""")

write_text("docs/model_card_template.md", """
# Model/System Card Template

## 1. Model or system overview

- Use case ID:
- Use case name:
- Business unit:
- Business owner:
- Technology owner:
- Risk owner:
- Data owner:
- Vendor involved:
- GenAI flag:
- Agentic AI flag:
- Lifecycle stage:
- Approval status:

## 2. Intended use

Describe the approved business purpose of the AI system, target users, supported decisions, expected benefits, and approved operating context.

## 3. Prohibited use

Examples:

- Fully automated adverse customer decisions without approval
- Use outside approved data sources
- Use for protected-class inference
- Use without required human review
- Use for legal, financial, or product advice beyond approved scope
- Use with confidential data in unapproved vendor tools

## 4. Data used

Document input datasets, data owners, personal information, confidential banking data, refresh frequency, retention, quality checks, limitations, excluded variables, and proxy variable assessment.

## 5. Model or system approach

Document AI type, model class or system design, vendor details, training or configuration approach, prompt strategy, retrieval grounding, and agentic tool permissions.

## 6. Limitations

Document weaker performance areas, data quality limitations, unsupported uses, operational constraints, and conditions requiring human review.

## 7. Fairness considerations

Document fairness risks, tested segments, metrics, results, mitigation actions, monitoring plan, and reviewer approval.

## 8. Explainability

Document explanation method, reason codes, user-facing explanation requirements, business reviewer documentation, and limitations.

## 9. Privacy and security

Document personal information, data minimization, access controls, encryption, logging, retention, data residency, vendor handling, privacy assessment status, and security assessment status.

## 10. Human oversight

Document human review points, approval thresholds, override rights, escalation path, exception logging, and decision documentation requirements.

## 11. Monitoring

Document monitoring metrics, thresholds, frequency, owner, alert trigger, escalation path, and retraining or rollback conditions.

## 12. Residual risks

| Risk | Residual rating | Decision | Owner | Review date |
|---|---|---|---|---|

## 13. Evidence

| Evidence | Owner | Status | Review date |
|---|---|---|---|

## 14. Approvals

| Role | Name or function | Decision | Date |
|---|---|---|---|
| Business owner | | | |
| Technology owner | | | |
| Risk owner | | | |
| Privacy reviewer | | | |
| Security reviewer | | | |
| Model reviewer | | | |
| Final approver | | | |
""")

write_text("docs/human_oversight_sop.md", """
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
""")

write_text("docs/privacy_security_vendor_review_checklist.md", """
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
""")

write_text("docs/ai_incident_response_workflow.md", """
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
""")

write_text("docs/ai_risk_committee_report_template.md", """
# AI Risk Committee Report Template

## Reporting period

- Month:
- Prepared by:
- Date:
- Committee meeting date:

## Executive summary

Summarize key AI risk themes, decisions required, escalations, unresolved issues, and material changes since the prior report.

## Portfolio overview

| Metric | Current period | Prior period | Direction |
|---|---:|---:|---|
| Total AI use cases | | | |
| High-risk AI use cases | | | |
| Critical-risk AI use cases | | | |
| GenAI use cases | | | |
| Agentic AI use cases | | | |
| Vendor AI use cases | | | |
| Use cases pending approval | | | |
| Use cases with overdue review | | | |

## High-risk and critical use cases

| Use case | Residual rating | Main risk | Owner | Decision required |
|---|---|---|---|---|

## Missing evidence

| Use case | Missing evidence | Control | Owner | Due date | Escalation |
|---|---|---|---|---|---|

## Open issues

| Issue | Use case | Severity | Owner | Due date | Status | Escalation |
|---|---|---|---|---|---|---|

## Accepted residual risks

| Use case | Risk | Rating | Acceptance owner | Expiry date | Monitoring condition |
|---|---|---|---|---|---|

## GenAI and agentic AI focus

Include GenAI use cases, agentic AI workflows, hallucination test results, prompt injection test results, unsupported response rate, PII leakage incidents, unauthorized tool action attempts, and human escalation effectiveness.

## Decisions required

| Decision | Use case | Recommendation | Required approver |
|---|---|---|---|

## Management actions

| Action | Owner | Due date | Status |
|---|---|---|---|
""")

# ----------------------------
# DASHBOARD
# ----------------------------

write_text("dashboard/app.py", """
from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

st.set_page_config(
    page_title="Banking AI Risk Management Control Tower",
    page_icon="🏦",
    layout="wide",
)

@st.cache_data
def load_csv(name):
    return pd.read_csv(DATA_DIR / name)

use_cases = load_csv("ai_use_case_register.csv")
risks = load_csv("ai_risk_assessment.csv")
controls = load_csv("control_library.csv")
evidence = load_csv("evidence_register.csv")
issues = load_csv("ai_issue_log.csv")
raci = load_csv("ai_governance_raci.csv")
mapping = load_csv("framework_mapping.csv")
monitoring = load_csv("model_monitoring_plan.csv")

st.title("Banking AI Risk Management Control Tower")
st.caption("Synthetic portfolio dashboard for AI inventory, risk assessment, controls, evidence, issues, ownership, monitoring, and framework mapping.")

page = st.sidebar.radio(
    "Dashboard pages",
    [
        "Executive summary",
        "AI use-case inventory",
        "Inherent vs residual risk",
        "Control coverage",
        "Missing evidence",
        "High-risk GenAI use cases",
        "Open issues",
        "Ownership and RACI",
        "NIST and ISO mapping",
        "Committee reporting",
    ],
)

risk_with_uc = risks.merge(
    use_cases[["use_case_id", "use_case_name", "business_unit", "genai_flag", "agentic_ai_flag"]],
    on="use_case_id",
    how="left"
)

evidence_with_control = evidence.merge(
    controls[["control_id", "control_name", "risk_category"]],
    on="control_id",
    how="left"
)

issues_with_uc = issues.merge(
    use_cases[["use_case_id", "use_case_name", "business_unit"]],
    on="use_case_id",
    how="left"
)

if page == "Executive summary":
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total AI use cases", len(use_cases))
    c2.metric("GenAI use cases", int((use_cases["genai_flag"] == "Yes").sum()))
    c3.metric("Agentic AI use cases", int((use_cases["agentic_ai_flag"] == "Yes").sum()))
    c4.metric("Open issues", int((issues["status"] != "Closed").sum()))

    c5, c6, c7, c8 = st.columns(4)
    c5.metric("High residual risks", int((risks["residual_risk_rating"] == "High").sum()))
    c6.metric("Critical residual risks", int((risks["residual_risk_rating"] == "Critical").sum()))
    c7.metric("Missing evidence", int((evidence["evidence_status"] == "Missing").sum()))
    c8.metric("Escalated issues", int(issues["escalation_status"].str.contains("Escalated", case=False, na=False).sum()))

    st.subheader("Average residual risk by use case")
    avg_risk = risk_with_uc.groupby("use_case_name", as_index=False)["residual_risk_score"].mean().sort_values("residual_risk_score", ascending=False)
    st.plotly_chart(px.bar(avg_risk, x="use_case_name", y="residual_risk_score"), use_container_width=True)

    st.subheader("Evidence status")
    st.plotly_chart(px.pie(evidence, names="evidence_status"), use_container_width=True)

elif page == "AI use-case inventory":
    st.subheader("AI use-case inventory")
    st.dataframe(use_cases, use_container_width=True)

elif page == "Inherent vs residual risk":
    st.subheader("Inherent vs residual risk")
    st.dataframe(risk_with_uc[[
        "use_case_id", "use_case_name", "risk_category", "inherent_risk_score",
        "residual_risk_score", "residual_risk_rating", "risk_decision"
    ]], use_container_width=True)

    st.plotly_chart(
        px.scatter(
            risk_with_uc,
            x="inherent_risk_score",
            y="residual_risk_score",
            color="residual_risk_rating",
            size="residual_risk_score",
            hover_data=["use_case_name", "risk_category", "risk_decision"],
        ),
        use_container_width=True,
    )

elif page == "Control coverage":
    st.subheader("Control library")
    st.dataframe(controls, use_container_width=True)

    st.subheader("Controls by risk category")
    counts = controls["risk_category"].value_counts().reset_index()
    counts.columns = ["risk_category", "control_count"]
    st.plotly_chart(px.bar(counts, x="risk_category", y="control_count"), use_container_width=True)

    st.subheader("Evidence linked to controls")
    st.dataframe(evidence_with_control, use_container_width=True)

elif page == "Missing evidence":
    st.subheader("Missing or pending evidence")
    missing = evidence_with_control[evidence_with_control["evidence_status"].isin(["Missing", "Pending"])]
    st.dataframe(missing, use_container_width=True)

elif page == "High-risk GenAI use cases":
    st.subheader("High-risk GenAI and agentic AI use cases")
    df = risk_with_uc[
        ((risk_with_uc["genai_flag"] == "Yes") | (risk_with_uc["agentic_ai_flag"] == "Yes"))
        & (risk_with_uc["residual_risk_rating"].isin(["High", "Critical"]))
    ]
    st.dataframe(df, use_container_width=True)

elif page == "Open issues":
    st.subheader("Open AI issues")
    open_issues = issues_with_uc[issues_with_uc["status"] != "Closed"]
    st.dataframe(open_issues, use_container_width=True)

    counts = open_issues["severity"].value_counts().reset_index()
    counts.columns = ["severity", "count"]
    st.plotly_chart(px.bar(counts, x="severity", y="count"), use_container_width=True)

elif page == "Ownership and RACI":
    st.subheader("Governance RACI")
    st.dataframe(raci.merge(use_cases[["use_case_id", "use_case_name", "business_unit"]], on="use_case_id", how="left"), use_container_width=True)

elif page == "NIST and ISO mapping":
    st.subheader("Framework mapping")
    st.dataframe(mapping, use_container_width=True)

    counts = mapping["framework"].value_counts().reset_index()
    counts.columns = ["framework", "mapped_items"]
    st.plotly_chart(px.bar(counts, x="framework", y="mapped_items"), use_container_width=True)

elif page == "Committee reporting":
    st.subheader("AI risk committee reporting view")
    high_risk = risk_with_uc[risk_with_uc["residual_risk_rating"].isin(["High", "Critical"])]
    missing = evidence_with_control[evidence_with_control["evidence_status"].isin(["Missing", "Pending"])]
    open_issues = issues_with_uc[issues_with_uc["status"] != "Closed"]

    c1, c2, c3 = st.columns(3)
    c1.metric("High/Critical residual risks", len(high_risk))
    c2.metric("Missing/Pending evidence items", len(missing))
    c3.metric("Open issues", len(open_issues))

    st.subheader("Decisions or escalations required")
    st.dataframe(high_risk[["use_case_id", "use_case_name", "risk_category", "residual_risk_score", "residual_risk_rating", "risk_decision"]], use_container_width=True)

    st.subheader("Monitoring plan")
    st.dataframe(monitoring, use_container_width=True)
""")

# ----------------------------
# VALIDATION SCRIPT
# ----------------------------

write_text("scripts/validate_data.py", """
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

required_files = [
    "ai_use_case_register.csv",
    "ai_risk_assessment.csv",
    "risk_mitigation_plan.csv",
    "control_library.csv",
    "evidence_register.csv",
    "ai_issue_log.csv",
    "ai_governance_raci.csv",
    "framework_mapping.csv",
    "model_monitoring_plan.csv",
]

def expected_rating(score):
    if score >= 20:
        return "Critical"
    if score >= 13:
        return "High"
    if score >= 6:
        return "Medium"
    return "Low"

def main():
    frames = {}
    for file in required_files:
        path = DATA / file
        if not path.exists():
            raise FileNotFoundError(f"Missing required file: {file}")
        frames[file] = pd.read_csv(path)

    use_case_ids = set(frames["ai_use_case_register.csv"]["use_case_id"])
    risk_ids = set(frames["ai_risk_assessment.csv"]["risk_id"])
    control_ids = set(frames["control_library.csv"]["control_id"])

    for file in [
        "ai_risk_assessment.csv",
        "risk_mitigation_plan.csv",
        "evidence_register.csv",
        "ai_issue_log.csv",
        "ai_governance_raci.csv",
        "model_monitoring_plan.csv",
    ]:
        unknown = set(frames[file]["use_case_id"]) - use_case_ids
        if unknown:
            raise ValueError(f"{file} has unknown use_case_id values: {sorted(unknown)}")

    unknown_risks = set(frames["risk_mitigation_plan.csv"]["risk_id"]) - risk_ids
    if unknown_risks:
        raise ValueError(f"risk_mitigation_plan.csv has unknown risk_id values: {sorted(unknown_risks)}")

    unknown_evidence_controls = set(frames["evidence_register.csv"]["control_id"]) - control_ids
    if unknown_evidence_controls:
        raise ValueError(f"evidence_register.csv has unknown control_id values: {sorted(unknown_evidence_controls)}")

    unknown_mapping_controls = set(frames["framework_mapping.csv"]["internal_control_id"]) - control_ids
    if unknown_mapping_controls:
        raise ValueError(f"framework_mapping.csv has unknown internal_control_id values: {sorted(unknown_mapping_controls)}")

    risks = frames["ai_risk_assessment.csv"]
    for _, row in risks.iterrows():
        inherent = int(row["inherent_impact"]) * int(row["inherent_likelihood"])
        residual = int(row["residual_impact"]) * int(row["residual_likelihood"])

        if inherent != int(row["inherent_risk_score"]):
            raise ValueError(f"Inherent score mismatch for {row['risk_id']}")

        if residual != int(row["residual_risk_score"]):
            raise ValueError(f"Residual score mismatch for {row['risk_id']}")

        if expected_rating(residual) != row["residual_risk_rating"]:
            raise ValueError(f"Residual rating mismatch for {row['risk_id']}")

    print("Validation passed.")
    print(f"Use cases: {len(frames['ai_use_case_register.csv'])}")
    print(f"Risk records: {len(frames['ai_risk_assessment.csv'])}")
    print(f"Controls: {len(frames['control_library.csv'])}")
    print(f"Evidence records: {len(frames['evidence_register.csv'])}")
    print(f"Issues: {len(frames['ai_issue_log.csv'])}")
    print(f"Framework mappings: {len(frames['framework_mapping.csv'])}")

if __name__ == "__main__":
    main()
""")

write_text("requirements.txt", """
pandas>=2.2.0
streamlit>=1.36.0
plotly>=5.22.0
""")

write_text(".gitignore", """
__pycache__/
*.py[cod]
.venv/
venv/
env/
.streamlit/secrets.toml
.DS_Store
Thumbs.db
*.log
""")

write_text("assets/.gitkeep", "")

print("All repository files created or repaired successfully.")
