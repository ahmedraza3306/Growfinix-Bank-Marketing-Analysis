import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/bank-full.csv", sep=";")

print("Shape:", df.shape)

# --------------------
# Average Age
# --------------------
print("\nAverage Age:")
print(df["age"].mean())

# --------------------
# Job Distribution
# --------------------
job_counts = df["job"].value_counts()

print("\nTop Jobs:")
print(job_counts.head())

plt.figure(figsize=(10,5))
job_counts.head(10).plot(kind="bar")
plt.title("Top 10 Jobs")
plt.xlabel("Job")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("src/outputs/job_distribution.png")
plt.show()

# --------------------
# Education Distribution
# --------------------
education_counts = df["education"].value_counts()

print("\nEducation Levels:")
print(education_counts)

plt.figure(figsize=(8,5))
education_counts.plot(kind="bar")
plt.title("Education Distribution")
plt.xlabel("Education")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("src/outputs/education_distribution.png")
plt.show()

# --------------------
# Deposit Subscription
# --------------------
deposit_counts = df["y"].value_counts()

print("\nDeposit Subscription:")
print(deposit_counts)

plt.figure(figsize=(6,4))
deposit_counts.plot(kind="bar")
plt.title("Deposit Subscription")
plt.xlabel("Response")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("src/outputs/deposit_subscription.png")
plt.show()

# --------------------
# Age Distribution
# --------------------
plt.figure(figsize=(8,5))
df["age"].hist(bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("src/outputs/age_distribution.png")
plt.show()