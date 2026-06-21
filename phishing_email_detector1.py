import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Sample Dataset
data = {
    "email": [
        "Congratulations! You won $1000. Click here now",
        "Verify your bank account immediately",
        "Meeting scheduled for tomorrow",
        "Project report attached",
        "Claim your free gift card now",
        "Team meeting at 10 AM",
        "Update your password urgently",
        "Lunch discussion today"
    ],
    "label": [
        "phishing",
        "phishing",
        "safe",
        "safe",
        "phishing",
        "safe",
        "phishing",
        "safe"
    ]
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["email"])
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Test Email
email = ["Click here to verify your account and claim reward"]
email_vector = vectorizer.transform(email)

prediction = model.predict(email_vector)

print("\nPrediction:", prediction[0])