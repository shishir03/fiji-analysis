import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_excel("Fiji combined 2012-2023.xlsx")
df = df[df["Boat owner"] != "N/A"]
df = df[df["Trip cost ($FJD)"] != "N/A"]

df["Year"] = df["Date"].apply(lambda x : x.year)
df["Month"] = df["Date"].apply(lambda x : x.month)

df["year_month"] = df["Date"].dt.to_period('M')
monthly_avg = df.groupby("year_month")["Fish size"].mean()

monthly_avg.index = monthly_avg.index.to_timestamp()

print(df)
if not Path("fiji_combined.csv").is_file():
    print("Outputting csv...")
    df.to_csv("fiji_combined.csv")

plt.figure(figsize=(10, 5))
plt.plot(monthly_avg.index, monthly_avg.values, marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Average Value')
plt.title('Monthly Averages Over Time')
plt.grid()
plt.show()
