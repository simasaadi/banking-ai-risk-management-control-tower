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
