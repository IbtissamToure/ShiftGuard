import pandas as pd
df = pd.read_csv("data/Shifts.csv")
df["shift_start"] = pd.to_datetime(df["shift_start"])
df["shift_end"] = pd.to_datetime(df["shift_end"])
print(df)