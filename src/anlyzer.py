import pandas as pd
df = pd.read_csv("data/Shifts.csv")
df["shift_start"] = pd.to_datetime(df["shift_start"])
df["shift_end"] = pd.to_datetime(df["shift_end"])
def calculate_risk_score(rest_hours):
    score = 100 - ((rest_hours / 24) *100)
    return round(max(0,min(100, score)),1)

def calculate_rest_hours(df):
    results = []
    for employee, shifts in df.groupby("employee_name"):
        shifts = shifts.sort_values("shift_start") #sort the values تصاعديا

        for i in range(len(shifts) - 1):
            current_end = shifts.iloc[i]["shift_end"]
            next_start = shifts.iloc[i + 1]["shift_start"]

            rest_hours = (next_start - current_end).total_seconds() /3600
            results.append({"Employee" : employee, "Rest Hours": rest_hours,"Is dangerous" : rest_hours < 11, "Risk Score" : calculate_risk_score(rest_hours)})
    return pd.DataFrame(results)
rest_df = calculate_rest_hours(df)

def suggest_replacement(rest_df,employee_to_replace):
    safe_employees = rest_df[rest_df["Is dangerous"] == False]
    safe_employees = safe_employees.sort_values("Rest Hours", ascending = False)
    safe_employees = safe_employees[safe_employees["Employee"] != employee_to_replace]
    if len(safe_employees) == 0 :
        return "لا يوجد موظف آمن متاح"
    best = safe_employees.iloc[0]
    return f"الاقتراح:{ best['Employee']} - راحة: {best['Rest Hours']} ساعة"

def calculate_risk_score(rest_hours):
    score = 100 - ((rest_hours / 24) *100)
    return round(max(0,min(100, score)),1)
print(calculate_rest_hours(df))
 