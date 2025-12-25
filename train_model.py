import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# 1️⃣ Load dataset
df = pd.read_csv("fake_job_postings.csv")

# 2️⃣ Keep only required columns
df = df[['description', 'fraudulent']]

# 3️⃣ Remove missing values
df = df.dropna()

# 4️⃣ Check class balance (IMPORTANT)
print(df['fraudulent'].value_counts())

# 5️⃣ Features & labels
from sklearn.utils import resample

# Separate classes
df_real = df[df["fraudulent"] == 0]
df_fake = df[df["fraudulent"] == 1]

# Downsample majority class (real jobs)
df_real_downsampled = resample(
    df_real,
    replace=False,
    n_samples=len(df_fake),
    random_state=42
)

# Combine balanced data
df_balanced = pd.concat([df_real_downsampled, df_fake])

# Features and labels
X = df_balanced["description"].fillna("")
y = df_balanced["fraudulent"]
