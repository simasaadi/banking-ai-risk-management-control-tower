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
