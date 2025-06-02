import streamlit as st
import pandas as pd
import subprocess


if st.sidebar.button("Logout"):
        # Clear session state and reload login page
        subprocess.Popen(["streamlit", "run", "login.py"], shell=True)
        st.experimental_rerun()



st.subheader("Dataset", divider='rainbow')

@st.cache_data
def load_data():
    data =pd.read_csv('Reduced_Training.csv', encoding='ISO-8859-1', index_col=False )
    st.write(data)

    # Displying the dataset
load_data()

st.write("""
    #### Column Descriptions

    - **itching:** Sensation that causes the desire to scratch.
    - **skin_rash:** Red, irritated skin.
    - **nodal_skin_eruptions:** Small lumps on the skin.
    - **continuous_sneezing:** Repeated sneezing.
    - **shivering:** Shaking of the body.
    - **chills:** Feeling cold with shivering.
    - **joint_pain:** Pain in the joints.
    - **stomach_pain:** Pain in the stomach.
    - **acidity:** Excess acid in the stomach.
    - **ulcers_on_tongue:** Sores on the tongue.
    - **vomiting:** Ejecting stomach contents through the mouth.
    - **fatigue:** Extreme tiredness.
    - **weight_gain:** Increase in body weight.
    - **anxiety:** Feeling of worry or fear.
    - **cold_hands_and_feets:** Feeling cold in hands and feet.
    - **mood_swings:** Rapid changes in mood.
    - **weight_loss:** Decrease in body weight.
    - **restlessness:** Inability to rest or relax.
    - **lethargy:** Lack of energy.
    - **patches_in_throat:** Spots or patches in the throat.
    - **prognosis:** The likely course of a disease or ailment.
    """)