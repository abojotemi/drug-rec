import streamlit as st
import numpy as np
import pickle
import pandas as pd
#import subprocess
#if st.sidebar.button("Logout"):
    # Clear session state and reload login page
    #subprocess.Popen(["streamlit", "run", "login.py"], shell=True)
    #st.experimental_rerun()

# Load your trained models

with open('Recommendation_model.sav', 'rb') as file:
    model1 = pickle.load(file) 

# This line loads the image 
import base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Path to the local image
image_path = 'drug-img.jpg'
try:
    # Convert the image to base64
    image_base64 = get_base64_of_bin_file(image_path)

    # Display the image using st.markdown with base64
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100px; margin-bottom:40px">
            <img style="border-radius:60%" src="data:image/jpeg;base64,{image_base64}" width="200">
        </div>
        """,
        unsafe_allow_html=True
    )
except FileNotFoundError:
    st.error(f"File {image_path} not found. Please ensure the file is in the correct location.")
# This is where the image loading script ends


# Define the columns in the dataset excluding 'prognosis'
columns = [
    'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering',
    'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'vomiting',
    'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss',
    'restlessness', 'lethargy', 'patches_in_throat'
]

def predict_disease(data):
    # Convert the input data to a DataFrame
    data_df = pd.DataFrame(data, index=[0])
    
    # Predict the outcome for the new data point
    prediction = model1.predict(data_df)
    
    return prediction[0]  # Extracting the single prediction value

def main():
    st.subheader("Tell me how you are feeling")

    # Creating columns for inputs
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    input_features = {}

    options = {"Yes": 1, "No": 0}

    with col1:
        for column in columns[:5]:
            input_features[column] = st.selectbox(f'Do you have {column}', options.keys(), index=1)
            input_features[column] = options[input_features[column]]
    
    with col2:
        for column in columns[5:10]:
            input_features[column] = st.selectbox(f'Do you have {column}', options.keys(), index=1)
            input_features[column] = options[input_features[column]]
    
    with col3:
        for column in columns[10:15]:
            input_features[column] = st.selectbox(f'Do you have {column}', options.keys(), index=1)
            input_features[column] = options[input_features[column]]
    
    with col4:
        for column in columns[15:]:
            input_features[column] = st.selectbox(f'Do you have {column}', options.keys(), index=1)
            input_features[column] = options[input_features[column]]

    # Creating a GUI button for prediction at the bottom
    if st.button('Predict'):
        prediction = predict_disease(input_features)
        
        with st.expander("Prediction Result", expanded=True):
            if prediction == 0:
                st.info('The disease diagnosed is [(vertigo) Paroymsal Positional Vertigo]')
                st.info('The following drugs are recommended for the treatment:')
                st.write('Drugs: 25 mg of pentylenetetrazol, 50 mg of nicotinic acid, 50 mg meclizine')
                st.write('Dosage: Pentylenetetrazol: 25 mg once daily. Nicotinic acid: 50 mg once daily. Meclizine: 25-50 mg once daily as needed.')
                st.write('Diet: Take meclizine with or without food. Avoid alcohol.')
                st.write('Warnings: :red[ay cause drowsiness; avoid driving or operating heavy machinery.]')
                st.error('Possible side effects: Drowsiness, dry mouth, headache.]')

            elif prediction == 1:
                st.info('The disease diagnosed is [AIDS]')
                st.info('The treatment of AIDS (Acquired Immune Deficiency Syndrome) primarily involves the use of antiretroviral therapy (ART), which is a combination of several antiretroviral drugs.')
                st.subheader('Recommended Drugs', divider=True)
                st.write('Drugs: Biktarvy (Bictegravir, Emtricitabine, Tenofovir alafenamide), Genvoya, Atripla, Triumeq, Dovato')
                st.write('Dosage: Biktarvy: one tablet (50 mg Bictegravir, 200 mg Emtricitabine, 25 mg Tenofovir alafenamide) once daily. Follow similar dosage for other ART medications.')
                st.write('Diet: Take with or without food.')
                st.write('Warnings :red[Do not stop taking without consulting your doctor. Regular blood tests are required.]')
                st.error("Possible side effects: Nausea, headache, fatigue, diarrhea.")
                                  
            elif prediction == 2:
                st.info('The disease diagnosed is [Acne]')
                st.info('Acne is a very common skin condition that causes pimples.')
                st.write('Drugs: Benzoyl Peroxide and Clindamycin Topical Gel')
                st.write('Dosage: Clindamycin: 1% (10 mg/g), Benzoyl Peroxide: 5% (50 mg/g). Apply a thin layer to the affected area(s) of the skin twice daily, in the morning and evening.')
                st.write('Diet: No specific dietary restrictions.')
                st.write('Warnings: :red[Avoid contact with eyes, mouth, and mucous membranes.]')
                st.error('Possible side effects: Dry skin, redness, peeling.')

            elif prediction == 3:
                st.info('The disease diagnosed is [Alcoholic hepatitis]')
                st.info('Alcoholic hepatitis is a severe liver inflammation caused by excessive alcohol consumption, characterized by jaundice, abdominal pain, and elevated liver enzymes, often leading to serious health complications and requiring medical intervention.')
                st.write('Drugs: Corticosteroids, Antioxidants, and Pentoxifylline')
                st.write('Dosage: Corticosteroids (Prednisolone): 40 mg orally daily for 4 weeks. Pentoxifylline: 400 mg orally three times a day.')
                st.write('Diet: Take with food to reduce stomach upset. Avoid alcohol.')
                st.write('Warnings: :red[Long-term use of corticosteroids can lead to serious side effects.]')
                st.error('Possible side effects: Weight gain, high blood pressure, mood swings.')

            elif prediction == 4:
                st.info('The disease diagnosed is [Allergy]')
                st.info('Allergies occur when the immune system reacts to a foreign substance such as pollen, bee venom, or pet dander.')
                st.write('Drugs: Antihistamines, Corticosteroids, Decongestants')
                st.write('Dosage: Antihistamines (Cetirizine): 10 mg once daily. Corticosteroids (Prednisone): 5-60 mg daily. Decongestants (Pseudoephedrine): 60 mg every 4-6 hours.')
                st.write('Diet: Take antihistamines with or without food. Avoid alcohol.')
                st.write('Warnings: :red[May cause drowsiness; avoid driving or operating heavy machinery.]')
                st.error('Possible side effects: Drowsiness, dry mouth, dizziness.')

            elif prediction == 5:
                st.info('The disease diagnosed is [Arthritis]')
                st.info('Arthritis is the swelling and tenderness of one or more of your joints.')
                st.write('Drugs: NSAIDs, Steroids, Analgesics')
                st.write('Dosage: NSAIDs (Ibuprofen): 200-400 mg every 4-6 hours. Steroids (Prednisone): 5-60 mg daily. Analgesics (Acetaminophen): 500 mg every 4-6 hours.')
                st.write('Diet: Take NSAIDs with food or milk to reduce stomach upset.')
                st.write('Warnings: :red[Long-term use of NSAIDs can cause stomach ulcers and bleeding.]')
                st.error('Possible side effects: Stomach pain, nausea, dizziness.')

            elif prediction == 6:
                st.info('The disease diagnosed is [Bronchial Asthma]')
                st.info('Asthma is a condition in which your airways narrow and swell and produce extra mucus.')
                st.write('Drugs: Inhaled corticosteroids, Long-acting beta agonists')
                st.write('Dosage: Inhaled corticosteroids (Fluticasone): 100-250 mcg twice daily. Long-acting beta agonists (Salmeterol): 50 mcg twice daily.')
                st.write('Diet: No specific dietary restrictions.')
                st.write('Warnings: :red[Rinse mouth after using inhaler to prevent oral thrush.]')
                st.error('Possible side effects: Hoarseness, throat irritation, headache.')

            elif prediction == 7:
                st.info('The disease diagnosed is [Cervical spondylosis]')
                st.info('Cervical spondylosis is a general term for age-related wear and tear affecting the spinal disks in your neck.')
                st.write('Drugs: NSAIDs, Muscle relaxants, Corticosteroids')
                st.write('Dosage: NSAIDs (Ibuprofen): 200-400 mg every 4-6 hours. Muscle relaxants (Cyclobenzaprine): 5-10 mg three times daily. Corticosteroids (Prednisone): 5-60 mg daily.')
                st.write('Diet: Take NSAIDs with food or milk to reduce stomach upset.')
                st.write('Warnings: :red[May cause drowsiness; avoid driving or operating heavy machinery.]')
                st.error('Possible side effects: Drowsiness, dry mouth, dizziness.')

            elif prediction == 8:
                st.info('The disease diagnosed is [Chicken pox]')
                st.info('Chickenpox is an infection caused by the varicella-zoster virus.')
                st.write('Drugs: Antihistamines, Acetaminophen')
                st.write('Dosage: Antihistamines (Diphenhydramine): 25-50 mg every 6-8 hours. Acetaminophen: 500 mg every 4-6 hours.')
                st.write('Diet: No specific dietary restrictions.')
                st.write('Warnings: :red[Do not use aspirin in children with chickenpox due to the risk of Reye’s syndrome.]')
                st.error('Possible side effects: Drowsiness, dry mouth, dizziness.')

            elif prediction == 9:
                st.info('The disease diagnosed is [Chronic cholestasis]')
                st.info('Chronic cholestasis is a long-term condition where the flow of bile from the liver is reduced.')
                st.write('Drugs: Ursodeoxycholic acid, Cholestyramine')
                st.write('Dosage: Ursodeoxycholic acid: 13-15 mg/kg/day divided into 2-4 doses. Cholestyramine: 4 g orally once or twice daily.')
                st.write('Diet: Take Ursodeoxycholic acid with food.')
                st.write('Warnings: :red[Cholestyramine may interfere with the absorption of other medications.]')
                st.error('Possible side effects: Diarrhea, constipation, stomach pain.')

            elif prediction == 10:
                st.info('The disease diagnosed is [Common Cold]')
                st.info('The common cold is a viral infection of your nose and throat.')
                
                st.write('Drugs: Decongestants, Antihistamines, Pain relievers')
                st.write('Dosage: Decongestants (Pseudoephedrine): 60 mg every 4-6 hours. Antihistamines (Cetirizine): 10 mg once daily. Pain relievers (Acetaminophen): 500 mg every 4-6 hours.')
                st.write('Diet: No specific dietary restrictions.')
                st.write('Warnings: :red[Decongestants may increase blood pressure; use with caution in patients with hypertension.]')
                st.error('Possible side effects: Drowsiness, dry mouth, dizziness.')

            elif prediction == 11:
                st.info('The disease diagnosed is [Dengue]')
                st.info('Dengue is a mosquito-borne viral infection.')
                st.write('Drugs: Acetaminophen, Rehydration therapy')
                st.write('Dosage: Acetaminophen: 500 mg every 4-6 hours. Rehydration therapy: Follow instructions for oral rehydration solutions.')
                st.write('Diet: No specific dietary restrictions.')
                st.write('Warnings: :red[Avoid aspirin and NSAIDs due to the risk of bleeding.]')
                st.error('Possible side effects: Nausea, stomach pain, dizziness.')

            elif prediction == 12:
                st.info('The disease diagnosed is [Diabetes]')
                st.info('Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high.')
                st.write('Drugs: Insulin, Metformin, Sulfonylureas')
                st.write('Dosage: Insulin: Dosage varies based on individual needs. Metformin: 500 mg twice daily. Sulfonylureas (Glipizide): 5 mg once daily.')
                st.write('Diet: Take Metformin with meals to reduce stomach upset.')
                st.write('Warnings: :ed[Monitor blood sugar levels regularly.]')
                st.error('Possible side effects: Hypoglycemia, nausea, stomach upset.')

            elif prediction == 13:
                st.info('The disease diagnosed is [Dimorphic hemorrhoids (piles)]')
                st.info('Hemorrhoids, also called piles, are swollen veins in your anus and lower rectum, similar to varicose veins.')
                st.write('Drugs: Topical treatments, Pain relievers')
                st.write('Dosage: Topical treatments (Hydrocortisone cream): Apply twice daily. Pain relievers (Acetaminophen): 500 mg every 4-6 hours.')
                st.write('Diet: Increase fiber intake and stay hydrated.')
                st.write('Warnings: :red[Do not use hydrocortisone cream for more than 7 days without consulting a doctor.]')
                st.error('Possible side effects: Skin irritation, dryness.')

            elif prediction == 14:
                st.success('The disease diagnosed is [Drug Reaction]')
                st.info('A drug reaction is an unintended side effect of a medication.')
                st.write('Drugs: Antihistamines, Corticosteroids')
                st.write('Dosage: Antihistamines (Diphenhydramine): 25-50 mg every 6-8 hours. Corticosteroids (Prednisone): 5-60 mg daily.')
                st.write('Diet: Take corticosteroids with food to reduce stomach upset.')
                st.write('Warnings: :red[May cause drowsiness; avoid driving or operating heavy machinery.]')
                st.error('Possible side effects: Drowsiness, dry mouth, dizziness.')

            elif prediction == 15:
                st.success('The disease diagnosed is [Fungal infection]')
                st.info('A fungal infection, also called mycosis, is a skin disease caused by a fungus.')
                st.info('Drugs: Antifungal medications')
                st.write('Dosage: Antifungal medications (Clotrimazole): Apply twice daily for 2-4 weeks.')
                st.write('Diet: No specific dietary restrictions.')
                st.write('Warnings: :red[Avoid contact with eyes, mouth, and mucous membranes.]')
                st.error('Possible side effects: Skin irritation, redness, burning sensation.')

            elif prediction == 16:
                st.success('The disease diagnosed is [GERD]')
                st.info('Gastroesophageal reflux disease (GERD) occurs when stomach acid frequently flows back into the tube connecting your mouth and stomach.')
                st.info('Drugs: Antacids, H-2-receptor blockers, Proton pump inhibitors')
                st.write('Dosage: Antacids: 1-2 tablets as needed after meals. H-2-receptor blockers (Ranitidine): 150 mg twice daily. Proton pump inhibitors (Omeprazole): 20 mg once daily.')
                st.write('Diet: Avoid spicy, fatty, and acidic foods. Eat smaller meals more frequently.')
                st.write('Warnings: :red[Long-term use of proton pump inhibitors may increase the risk of bone fractures.]')
                st.error('Possible side effects: Headache, diarrhea, stomach pain.')

            elif prediction == 17:
                st.success('The disease diagnosed is [Gastroenteritis]')
                st.info('Gastroenteritis is an inflammation of the stomach and intestines, typically resulting from bacterial toxins or viral infection.')
                st.info('Drugs: Rehydration solutions, Antidiarrheals')
                st.write('Dosage: Rehydration solutions: Follow instructions for oral rehydration solutions. Antidiarrheals (Loperamide): 4 mg initially, then 2 mg after each loose stool.')
                st.write('Diet: Stay hydrated. Eat bland foods like rice, bananas, and toast.')
                st.write('Warnings: :red[Do not use antidiarrheals if you have a high fever or blood in your stool.]')
                st.error('Possible side effects: Constipation, dizziness, nausea.')

            elif prediction == 18:
                st.success('The disease diagnosed is [Heart attack]')
                st.info('A heart attack occurs when the flow of blood to the heart is blocked.')
                st.info('Drugs: Aspirin, Thrombolytics, Antiplatelet agents')
                st.write('Dosage: Aspirin: 300 mg immediately. Thrombolytics: Follow doctor’s instructions. Antiplatelet agents (Clopidogrel): 75 mg once daily.')
                st.write('Diet: Take aspirin with food to reduce stomach upset.')
                st.write('Warnings: :red[Aspirin can increase the risk of bleeding. Consult your doctor before use.]')
                st.error('Possible side effects: Stomach pain, heartburn, dizziness.')

            elif prediction == 19:
                st.success('The disease diagnosed is [Hepatitis B]')
                st.info('Hepatitis B is a serious liver infection caused by the hepatitis B virus.')
                st.info('Drugs: Antiviral medications, Interferon injections')
                st.write('Dosage: Antiviral medications (Tenofovir): 300 mg once daily. Interferon injections: Follow doctor’s instructions.')
                st.write('Diet: Take antiviral medications with or without food.')
                st.write('Warnings: :red[Regular monitoring of liver function is required.]')
                st.error('Possible side effects: Nausea, headache, fatigue.')

            elif prediction == 20:
                st.success('The disease diagnosed is [Hepatitis C]')
                st.info('Hepatitis C is a viral infection that causes liver inflammation, sometimes leading to serious liver damage.')
                st.info('Drugs: Antiviral medications')
                st.write('Dosage: Antiviral medications (Sofosbuvir): 400 mg once daily.')
                st.write('Diet: Take antiviral medications with or without food.')
                st.write('Warnings: :red[Regular monitoring of liver function is required.]')
                st.error('Possible side effects: Fatigue, headache, nausea.')

            elif prediction == 21:
                st.success('The disease diagnosed is [Hepatitis D]')
                st.info('Hepatitis D is a serious liver disease caused by the hepatitis D virus, a small virus that requires hepatitis B virus to replicate.')
                st.info('Drugs: Interferon alfa')
                st.write('Dosage: Interferon alfa: 9 million units three times weekly for 48 weeks.')
                st.write('Diet: Take with or without food.')
                st.write('Warnings: :red[Regular monitoring of liver function is required.]')
                st.error('Possible side effects: Flu-like symptoms, fatigue, depression.')

            elif prediction == 22:
                st.success('The disease diagnosed is [Hepatitis E]')
                st.info('Hepatitis E is a liver disease caused by the hepatitis E virus.')
                st.write('Drugs: Ribavirin, Interferon alfa-2a')
                st.write('Dosage: Ribavirin: 1000-1200 mg daily. Interferon alfa-2a: Follow doctor’s instructions.')
                st.write('Diet: Take Ribavirin with food.')
                st.write('Warnings: Ribavirin can cause birth defects; avoid use during pregnancy.')
                st.write('Possible side effects: Anemia, fatigue, nausea.')

            elif prediction == 23:
                st.success('The disease diagnosed is [Hypertension]')
                st.info('Hypertension, also known as high blood pressure, is a long-term medical condition in which the blood pressure in the arteries is persistently elevated.')
                st.info('Drugs: ACE inhibitors, Beta blockers, Diuretics')
                st.write('Dosage: ACE inhibitors (Lisinopril): 10-40 mg daily. Beta blockers (Atenolol): 50-100 mg daily. Diuretics (Hydrochlorothiazide): 25 mg once daily.')
                st.write('Diet: Reduce salt intake. Eat a diet rich in fruits, vegetables, and low-fat dairy products.')
                st.write('Warnings: :red[Monitor blood pressure regularly.]')
                st.error('Possible side effects: Dizziness, fatigue, dry cough.')

            elif prediction == 24:
                st.success('The disease diagnosed is [Hyperthyroidism]')
                st.info('Hyperthyroidism occurs when your thyroid gland produces too much of the hormone thyroxine.')
                st.info('Drugs: Antithyroid medications, Beta blockers')
                st.write('Dosage: Antithyroid medications (Methimazole): 15-60 mg daily. Beta blockers (Propranolol): 10-40 mg three times daily.')
                st.write('Diet: No specific dietary restrictions.')
                st.write('Warnings: :red[Regular monitoring of thyroid function is required.]')
                st.error('Possible side effects: Rash, joint pain, liver toxicity.')

            elif prediction == 25:
                st.success('The disease diagnosed is [Hypoglycemia]')
                st.info('Hypoglycemia is a condition in which your blood sugar (glucose) level is lower than normal.')
                st.info('Drugs: Glucose tablets, Glucagon injection')
                st.write('Dosage: Glucose tablets: 15-20 grams orally. Glucagon injection: 1 mg intramuscularly or subcutaneously.')
                st.write('Diet: Eat a balanced diet with regular meals and snacks.')
                st.write('Warnings: :red[Monitor blood sugar levels regularly.]')
                st.error('Possible side effects: Nausea, vomiting, headache.')

            elif prediction == 26:
                st.success('The disease diagnosed is [Hypothyroidism]')
                st.info('Hypothyroidism, also called underactive thyroid, is a condition in which your thyroid gland doesn’t produce enough of certain crucial hormones.')
                st.info('Drugs: Levothyroxine')
                st.write('Dosage: Levothyroxine: 1.6 mcg/kg/day orally.')
                st.write('Diet: Take on an empty stomach, 30 minutes before breakfast.')
                st.write('Warnings: :red[Regular monitoring of thyroid function is required.]')
                st.error('Possible side effects: Palpitations, insomnia, weight loss.')

            elif prediction == 27:
                st.success('The disease diagnosed is [Impetigo]')
                st.info('Impetigo is a common and highly contagious skin infection that mainly affects infants and children.')
                st.info('Drugs: Antibiotic ointment or cream, Oral antibiotics')
                st.write('Dosage: Antibiotic ointment (Mupirocin): Apply three times daily. Oral antibiotics (Cephalexin): 250-500 mg four times daily.')
                st.write('Diet: No specific dietary restrictions.')
                st.write('Warnings: :red[Complete the full course of antibiotics to prevent resistance.]')
                st.error('Possible side effects: Skin irritation, nausea, diarrhea.')

            elif prediction == 28:
                st.success('The disease diagnosed is [Jaundice]')
                st.info('Jaundice is a condition in which the skin, whites of the eyes, and mucous membranes turn yellow because of a high level of bilirubin.')
                st.info('Drugs: Depends on underlying cause, consult a doctor')
                st.write('Dosage: Follow your doctor’s instructions for specific medications.')
                st.write('Diet: Eat a balanced diet with adequate hydration.')
                st.write('Warnings: :red[Monitor liver function regularly.]')
                st.error('Possible side effects: Depends on specific medications.')

            elif prediction == 29:
                st.success('The disease diagnosed is [Malaria]')
                st.info('Malaria is a disease caused by a plasmodium parasite, transmitted by the bite of infected mosquitoes.')
                st.info('Drugs: Chloroquine, Artemisinin-based combination therapies')
                st.write('Dosage: Chloroquine: 600 mg initially, then 300 mg after 6-8 hours, then 300 mg once daily for 2 days. Artemisinin-based combination therapies: Follow the specific treatment regimen prescribed.')
                st.write('Diet: Take with food to reduce stomach upset.')
                st.write('Warnings: :red[Chloroquine can cause vision changes; report any changes to your doctor.]')
                st.error('Possible side effects: Nausea, vomiting, headache.')

            elif prediction == 30:
                st.success('The disease diagnosed is [Migraine]')
                st.info('A migraine can cause severe throbbing pain or a pulsing sensation, usually on one side of the head.')
                st.info('Drugs: Pain relievers, Triptans, Antiemetics')
                st.write('Dosage: Pain relievers (Ibuprofen): 200-400 mg every 4-6 hours. Triptans (Sumatriptan): 50-100 mg at onset of migraine, may repeat after 2 hours. Antiemetics (Metoclopramide): 10 mg at onset of migraine.')
                st.write('Diet: Take with or without food.')
                st.write('Warnings: :red[Triptans may cause dizziness; avoid driving or operating heavy machinery.]')
                st.error('Possible side effects: Dizziness, drowsiness, nausea.')

            elif prediction == 31:
                st.success('The disease diagnosed is [Osteoarthritis]')
                st.info('Osteoarthritis is the most common form of arthritis, affecting millions of people worldwide.')
                st.info('Drugs: Acetaminophen, NSAIDs, Duloxetine')
                st.write('Dosage: Acetaminophen: 500 mg every 4-6 hours. NSAIDs (Ibuprofen): 200-400 mg every 4-6 hours. Duloxetine: 60 mg once daily.')
                st.write('Diet: Take NSAIDs with food or milk to reduce stomach upset.')
                st.write('Warnings: :red[Long-term use of NSAIDs can cause stomach ulcers and bleeding.]')
                st.error('Possible side effects: Stomach pain, nausea, dizziness.')

            elif prediction == 32:
                st.success('The disease diagnosed is [Paralysis (brain hemorrhage)]')
                st.info('Paralysis is the loss of muscle function in part of your body.')
                st.info('Drugs: Depends on the cause and extent of paralysis, consult a doctor')
                st.write('Dosage: Follow your doctor’s instructions for specific medications.')
                st.write('Diet: Eat a balanced diet with adequate hydration.')
                st.write('Warnings: :red[Monitor for any changes in symptoms and report to your doctor.]')
                st.error('Possible side effects: Depends on specific medications.')

            elif prediction == 33:
                st.success('The disease diagnosed is [Peptic ulcer disease]')
                st.info('Peptic ulcer disease occurs when open sores, or ulcers, form in the stomach or first part of the small intestine.')
                st.info('Drugs: Proton pump inhibitors, H2-receptor antagonists, Antibiotics')
                st.write('Dosage: Proton pump inhibitors (Omeprazole): 20 mg once daily. H2-receptor antagonists (Ranitidine): 150 mg twice daily. Antibiotics: Follow the specific treatment regimen prescribed.')
                st.write('Diet: Avoid spicy, fatty, and acidic foods. Eat smaller meals more frequently.')
                st.write('Warnings: :red[Long-term use of proton pump inhibitors may increase the risk of bone fractures.]')
                st.error('Possible side effects: Headache, diarrhea, stomach pain.')

            elif prediction == 34:
                st.success('The disease diagnosed is [Pneumonia]')
                st.info('Pneumonia is an infection that inflames the air sacs in one or both lungs.')
                st.info('Drugs: Antibiotics, Cough medicine, Pain relievers')
                st.write('Dosage: Antibiotics (Amoxicillin): 500 mg three times daily. Cough medicine (Dextromethorphan): 10-20 mg every 4 hours. Pain relievers (Acetaminophen): 500 mg every 4-6 hours.')
                st.write('Diet: No specific dietary restrictions.')
                st.write('Warnings: :red[ Complete the full course of antibiotics to prevent resistance.]')
                st.error('Possible side effects: Nausea, diarrhea, stomach pain.')

            elif prediction == 35:
                st.success('The disease diagnosed is [Psoriasis]')
                st.info('Psoriasis is a skin disease that causes red, itchy scaly patches, most commonly on the knees, elbows, trunk, and scalp.')
                st.info('Drugs: Topical treatments, Light therapy, Systemic medications')
                st.write('Dosage: Topical treatments (Calcipotriene): Apply twice daily. Light therapy: Follow dermatologist’s instructions. Systemic medications (Methotrexate): 10-25 mg once weekly.')
                st.write('Diet: No specific dietary restrictions.')
                st.write('Warnings: :red[Monitor for signs of infection and report to your doctor.]')
                st.error('Possible side effects: Skin irritation, redness, dryness.')

            elif prediction == 36:
                st.success('The disease diagnosed is [Tuberculosis]')
                st.info('Tuberculosis (TB) is a potentially serious infectious disease that mainly affects your lungs.')
                st.info('Drugs: Isoniazid, Rifampin, Ethambutol')
                st.write('Dosage: Isoniazid: 5 mg/kg (up to 300 mg) once daily. Rifampin: 10 mg/kg (up to 600 mg) once daily. Ethambutol: 15-25 mg/kg once daily.')
                st.write('Diet: Take with or without food.')
                st.write('Warnings: :red[Monitor liver function regularly.]')
                st.error('Possible side effects: Nausea, vomiting, joint pain.')

            elif prediction == 37:
                st.success('The disease diagnosed is [Typhoid]')
                st.info('Typhoid fever is a bacterial infection that can spread throughout the body, affecting many organs.')
                st.info('Drugs: Antibiotics such as Ciprofloxacin or Azithromycin')
                st.write('Dosage: Ciprofloxacin: 500 mg twice daily for 7-14 days. Azithromycin: 500 mg once daily for 7 days.')
                st.write('Diet: Take with or without food.')
                st.write('Warnings: :red[Complete the full course of antibiotics to prevent resistance.]')
                st.error('Possible side effects: Nausea, diarrhea, stomach pain.')

            elif prediction == 38:
                st.success('The disease diagnosed is [Urinary tract infection]')
                st.info('A urinary tract infection (UTI) is an infection in any part of your urinary system.')
                st.info('Drugs: Antibiotics such as Trimethoprim/Sulfamethoxazole, Fosfomycin, Nitrofurantoin')
                st.write('Dosage: Trimethoprim/Sulfamethoxazole: 160/800 mg every 12 hours for 3 days. Fosfomycin: 3 g orally once. Nitrofurantoin: 100 mg twice daily for 5 days.')
                st.write('Diet: Take Nitrofurantoin with food to increase absorption and reduce stomach upset.')
                st.write('Warnings: :red[Increase fluid intake to help flush the bacteria from your urinary tract.]')
                st.error('Possible side effects: Nausea, diarrhea, headache.')

            elif prediction == 39:
                st.success('The disease diagnosed is [Varicose veins]')
                st.info('Varicose veins are gnarled, enlarged veins, most commonly appearing in the legs and feet.')
                st.info('Drugs: Compression stockings, Sclerotherapy, Laser treatment')
                st.write('Dosage: Compression stockings: Wear as directed. Sclerotherapy: Follow doctor’s instructions for injection sessions. Laser treatment: Follow doctor’s instructions for treatment sessions.')
                st.write('Diet: No specific dietary restrictions.')
                st.write('Warnings: :red[Monitor for signs of infection or complications.]')
                st.error('Possible side effects: Skin irritation, bruising, swelling.')

            elif prediction == 40:
                st.success('The disease diagnosed is [Hepatitis A]')
                st.info('Hepatitis A is a highly contagious liver infection caused by the hepatitis A virus.')
                st.info('Drugs: No specific treatment, focus on supportive care')
                st.write('Dosage: Rest, hydration, and adequate nutrition. Follow doctor’s instructions for supportive care.')
                st.write('Diet: Avoid alcohol and maintain a balanced diet.')
                st.write('Warnings: :red[Maintain good hygiene to prevent spreading the virus.]')
                st.error('Possible side effects: Fatigue, nausea, stomach pain.')

            else:
                st.warning('Other disease detected')

if __name__ == '__main__':
    main()
