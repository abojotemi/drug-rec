import streamlit as st
import pandas as pd
import random
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Step 1: List of 50 drug names
drug_names = [
    "Acetaminophen", "Ibuprofen", "Amoxicillin", "Metformin", "Atorvastatin",
    "Lisinopril", "Amlodipine", "Albuterol", "Prednisone", "Omeprazole",
    "Gabapentin", "Hydrochlorothiazide", "Furosemide", "Simvastatin", "Losartan",
    "Levothyroxine", "Clopidogrel", "Azithromycin", "Tramadol", "Citalopram",
    "Sertraline", "Rosuvastatin", "Ciprofloxacin", "Warfarin", "Montelukast",
    "Pantoprazole", "Escitalopram", "Bupropion", "Doxycycline", "Ranitidine",
    "Tamsulosin", "Naproxen", "Clonazepam", "Fluoxetine", "Meloxicam",
    "Metoprolol", "Valsartan", "Celecoxib", "Digoxin", "Atenolol",
    "Sulfamethoxazole", "Clindamycin", "Allopurinol", "Diltiazem", "Cetirizine",
    "Zolpidem", "Labetalol", "Propranolol", "Spironolactone", "Loratadine"
]

# Step 2: Simulate a population of 180 drug occurrences
drug_population = [random.choice(drug_names) for _ in range(180)]

# Step 3: Create a DataFrame for drug occurrences
drug_df = pd.DataFrame(drug_population, columns=["Drug"])

# Step 4: Filter only the first 50 unique drugs based on occurrences
filtered_drugs = drug_df[drug_df["Drug"].isin(drug_names[:50])]

# Step 5: Create a count plot using Seaborn with a better color palette
st.title("Drug Frequency Count Plot")

# Create the plot with Seaborn
plt.figure(figsize=(10, 8))
sns.countplot(
    data=filtered_drugs, 
    y="Drug", 
    palette="viridis", 
    order=filtered_drugs["Drug"].value_counts().index
)

# Step 6: Adjust plot aesthetics
plt.title("Frequency of Drug Names (Top 50)", fontsize=16)
plt.xlabel("Count", fontsize=12)
plt.ylabel("Drug Names", fontsize=12)
plt.tight_layout()

# Step 7: Display the plot in Streamlit
st.pyplot(plt)




# Disease visualization
diseases = [
    "Hypertension", "Diabetes", "Asthma", "HIV/AIDS", "Tuberculosis",
    "Malaria", "Pneumonia", "Influenza", "Hepatitis B", "Dengue Fever",
    "Cholera", "Measles", "Ebola", "Zika Virus", "Covid-19",
    "Cancer", "Heart Disease", "Arthritis", "Alzheimer's", "Stroke"
]

# Step 2: Generate random frequencies for these diseases
np.random.seed(42)  # For reproducibility
frequencies = np.random.randint(50, 200, size=len(diseases))

# Step 3: Create a DataFrame for the diseases and their frequencies
disease_df = pd.DataFrame({
    "Disease": diseases,
    "Frequency": frequencies
})

# Step 4: Plot a pie chart with a shadow and a nice color map
st.title("Disease Frequency Distribution")

# Create the pie chart
plt.figure(figsize=(8, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(diseases)))  # Using 'viridis' colormap for smooth color transition

plt.pie(
    disease_df["Frequency"],
    labels=disease_df["Disease"],
    autopct='%1.1f%%',
    startangle=140,
    shadow=True,
    colors=colors
)

# Adding a title and ensure the plot is a circle
plt.title("Distribution of Disease Frequencies", fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.

# Step 5: Displaying the plot in Streamlit
st.pyplot(plt)


# using barplot for Disease visualization
diseases = [
    "Hypertension", "Diabetes", "Asthma", "HIV/AIDS", "Tuberculosis",
    "Malaria", "Pneumonia", "Influenza", "Hepatitis B", "Dengue Fever",
    "Cholera", "Measles", "Ebola", "Zika Virus", "Covid-19",
    "Cancer", "Heart Disease", "Arthritis", "Alzheimer's", "Stroke"
]

# Step 2: Generate random frequencies for these diseases
np.random.seed(42)  # For reproducibility
frequencies = np.random.randint(50, 180, size=len(diseases))

# Step 3: Create a DataFrame for the diseases with repeated values according to their frequencies
disease_data = []
for disease, freq in zip(diseases, frequencies):
    disease_data.extend([disease] * freq)

# Create DataFrame
disease_df = pd.DataFrame(disease_data, columns=["Disease"])

# Step 4: Plot a vertical countplot using Seaborn
st.title("Disease Frequency Distribution")

# Set the figure size and custom color palette
plt.figure(figsize=(12, 6))
palette = sns.color_palette("tab20", len(diseases))  # Use 'tab20' for diverse colors

# Create the countplot
sns.countplot(
    x="Disease",
    data=disease_df,
    palette=palette
)

# Step 5: Format the x-ticks and add labels
plt.xticks(rotation=45, ha='right', fontsize=10)  # Rotate and format the x-ticks
plt.title("Frequency of Diseases", fontsize=16)
plt.xlabel("Disease", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.tight_layout()

# Step 6: Display the plot in Streamlit
st.pyplot(plt)
