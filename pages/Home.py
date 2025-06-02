import streamlit as st
import pandas as pd
import subprocess

if st.sidebar.button("Logout"):
        # Clear session state and reload login page
        # subprocess.Popen(["streamlit", "run", "login.py"], shell=True)
        st.switch_page("login.py")
        st.rerun()

def main():
    st.subheader("Disease Prediction and Drug Recommendation System", anchor=False, divider="rainbow")
    
    st.markdown("""
                This web application is designed to predict diseases based on patient symptoms and recommend appropriate drugs. This Web app also provides: 
                - Dataset Details
                - Data Visualizations
                - Prediction
                - Model Evaluation
                
                ---

                ## Dataset Details

                The dataset used in this project includes patient symptoms such as itching, skin rash, nodal skin eruptions, continuous sneezing, shivering, chills, joint pain, stomach pain, acidity, ulcers on tongue, and many others. The prognosis column indicates the diagnosed disease. This dataset provides valuable insights into the factors influencing disease diagnosis and drug recommendations.

                ---

                ## Data Visualizations

                To gain a better understanding of the dataset, we've created several visualizations:

                - **Symptom Frequency**: A count chart showing the frequency of each symptom in the dataset.
                - **Disease Distribution**: A count chart showing the distribution of different diseases in the dataset.
                - **Symptom Co-occurrence**: A heatmap showing how symptoms co-occur in patients.

                ---

                ## Prediction

                You can predict the disease a patient might have by providing their symptoms. Simply fill out the form with the required information, and our model will provide a prediction based on historical data.

                ---

                ## Model Evaluation

                We've evaluated the prediction model using the following metrics:

                - **Accuracy**: The percentage of correctly predicted outcomes.
                - **Precision**: The proportion of true positive predictions out of all positive predictions.
                - **Recall**: The proportion of true positive predictions out of all actual positive cases.
                - **F1-score**: The harmonic mean of precision and recall, providing a balanced measure of model performance.

                ---

                ### Conclusion and Recommendations

                Based on the evaluation, we conclude that our model performs well in diagnosing diseases based on patient symptoms. However, continuous monitoring and validation are recommended to ensure the model's accuracy on new data.

                ---

               

                **Disclaimer**: This application is for educational and informational purposes only. The recommendations made by the model are based on historical data and should not be used for making real-world medical decisions without consulting a healthcare professional.
            """)


if __name__ == "__main__":
    main()
