import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

print("Preview of the dataset:")
print(df.head())

print("\nDescriptive statistics:")
print(df.describe())

plt.figure(figsize=(8, 5))
plt.plot(df["Month"], df["Sales"], marker="o", linestyle="-", color="b")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
