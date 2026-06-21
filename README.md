SOC Phishing Email Detection
Project Overview

This project is a Security Operations Center (SOC) mini project that identifies phishing emails using Machine Learning. The system analyzes email text and predicts whether an email is phishing or safe.

Objective

To automate email classification and help security analysts detect phishing attempts quickly.

Features
Email text preprocessing
Feature extraction using CountVectorizer
Email classification using Naive Bayes algorithm
Accuracy evaluation
Prediction of new emails
Technologies Used
Python
Pandas
Scikit-learn
CountVectorizer
Multinomial Naive Bayes
Project Structure
soc-phishing-email-detection/
│
├── phishing_email_detector.py
├── README.md
├── requirements.txt
└── screenshots/
Installation
pip install pandas scikit-learn
Run the Project
python phishing_email_detector.py
Sample Output
Accuracy: 1.0

Confusion Matrix:
[[1 0]
 [0 1]]

Prediction: phishing
SOC Use Case

Phishing emails are one of the most common cyberattacks. This project demonstrates how machine learning can assist SOC analysts in detecting malicious emails and improving incident response.

requirements.txt
pandas
scikit-learn
