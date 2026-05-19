import pandas as pd

data = {"name": ["Ahmed", "AboNe3ma", "Mohamed"], "salary": [5000, 7000, 6000]}

df = pd.DataFrame(data)
df["salary_after_tax"] = df["salary"] * 0.9
df.to_csv("output.csv", index=False)
print("Etl process completed")
