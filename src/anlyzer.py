import pandas as pd
df = pd.read_csv("data/Shifts.csv")
df["shift_start"] = pd.to_datetime(df["shift_start"])
df["shift_end"] = pd.to_datetime(df["shift_end"])
def calculate_rest_hours(df):
    results = []
    for employee, shifts in df.groupby("employee_name"):
        shifts = shifts.sort_values("shift_start") #sort the values تصاعديا

        for i in range(len(shifts) - 1):
            current_end = shifts.iloc[i]["shift_end"]
            next_start = shifts.iloc[i + 1]["shift_start"]

            rest_hours = (next_start - current_end).total_seconds() /3600
            results.append({"Employee" : employee, "Rest Hours": rest_hours,"Is dangerous" : rest_hours < 11})
    return pd.DataFrame(results)
rest_def = calculate_rest_hours(df)
print(rest_def)