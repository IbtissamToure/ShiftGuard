import argparse
import pandas as pd
from anlyzer import calculate_rest_hours, calculate_risk_score, suggest_replacement
def print_report(employee_name, rest_df):
    employee_data = rest_df[rest_df["Employee"] == employee_name]
    if len(employee_data) == 0:
        print(f"Employee '{employee_name}' is not found")
        return
    row = employee_data.iloc[0]
    risk_emoji = "🔴 DANGEROUS" if row["Is dangerous"] else "🟢 SAFE"

    print("==========================================")
    print("     ShiftGuard 🛡️  Safety Report")
    print("==========================================")
    print(f"Employee   : {row['Employee']}")
    print(f"Rest Hours : {row['Rest Hours']} hours")
    print(f"Risk Score : {row['Risk Score']} / 100 {risk_emoji}")
    print("------------------------------------------")
    suggestion = suggest_replacement(rest_df, employee_name)
    print(f"💡 {suggestion}")
    print("==========================================")

def main():
    parser = argparse.ArgumentParser(description="ShiftGuard Safety Checker")
    parser.add_argument("--employee", type=str, required=True)
    args = parser.parse_args()
    
    df = pd.read_csv("data/shifts.csv")
    df["shift_start"] = pd.to_datetime(df["shift_start"])
    df["shift_end"] = pd.to_datetime(df["shift_end"])
    
    rest_df = calculate_rest_hours(df)
    
    print_report(args.employee, rest_df)
if __name__ == "__main__":
    main()    


