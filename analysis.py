import pandas as pd

df = pd.read_excel("Fiji combined 2012-2023.xlsx")
df = df[df["Boat owner"] != "N/A"]
df = df[df["Trip cost ($FJD)"] != "N/A"]

df["Year"] = df["Date"].apply(lambda x : x.year)
df["Month"] = df["Date"].apply(lambda x : x.month)

print(df)