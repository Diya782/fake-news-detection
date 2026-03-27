import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from preprocess import preprocess

# Load datasets
fake = pd.read_csv("../data/Fake.csv")
true = pd.read_csv("../data/True.csv")

# Add labels
fake["class"] = 0
true["class"] = 1

# Combine
data = pd.concat([fake, true])

# Shuffle
data = data.sample(frac=1).reset_index(drop=True)

# Apply preprocessing
data["text"] = data["text"].apply(preprocess)

# Features + labels
X = data["text"]
y = data["class"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Vectorization
vectorizer = TfidfVectorizer()
Xv_train = vectorizer.fit_transform(X_train)

# Model
model = LogisticRegression()
model.fit(Xv_train, y_train)

# Save model + vectorizer
pickle.dump(model, open("../model/model.pkl", "wb"))
pickle.dump(vectorizer, open("../model/vectorizer.pkl", "wb"))

print("✅ Training complete & model saved!")