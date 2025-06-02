import streamlit as st
import numpy as np
import pickle
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import subprocess

if st.sidebar.button("Logout"):
        # Clear session state and reload login page
        subprocess.Popen(["streamlit", "run", "login.py"], shell=True)
        st.experimental_rerun()

# Load your trained model
with open('Recommendation_model.sav', 'rb') as file:
    model1 = pickle.load(file)

X_test =pd.read_csv('X_test (3).csv', encoding='ISO-8859-1', index_col=False )
y_test =pd.read_csv('y_test (4).csv', encoding='ISO-8859-1', index_col=False )

st.title("Model Evaluation")
# Evaluate the model on the test set
y_pred = model1.predict(X_test)

# Generate the classification report
report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()

st.subheader("Classification Report")
st.dataframe(report_df)

st.subheader("Report Explanation")
st.markdown("""
        **Precision**: This is the ratio of correctly predicted positive observations to the total predicted positives. Precision = TP/(TP+FP)

        **Recall (Sensitivity)**: This is the ratio of correctly predicted positive observations to the all observations in actual class. Recall = TP/(TP+FN)

        **F1 Score**: This is the weighted average of Precision and Recall. Therefore, this score takes both false positives and false negatives into account. F1 Score = 2*(Recall * Precision) / (Recall + Precision)

        **Support**: The number of actual occurrences of the class in the specified dataset.
        """)
        


