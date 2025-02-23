import pandas as pd
import matplotlib.pyplot as plt

# TODO: Load dataset; replace this csv to your file
df = pd.read_csv("data/US_Accidents_March23.csv")

# Step 1: Handling the format
# TODO: Remove extra precision if exists

# TODO: Extract relevant time-based features

# TODO: Fix missing values for numerical columns
# TODO: Ensure Severity is numeric
df['Severity'] = pd.to_numeric(df['Severity'], errors='coerce')



# Pie Charts
# severity_counts = df['Severity'].value_counts(normalize=True) * 100
# plt.pie(severity_counts)
# plt.title("Pie Chart of Severity")
# # plt.show()

# Road conditions presence
# road_conditions = ['Crossing', 'Traffic_Signal', 'Junction']
# for condition in road_conditions:
    

# Bar Plots
# Accident Cases vs Hours
# hourly_counts = df['Hour'].value_counts().sort_index()

severity_counts = df['Severity'].value_counts(normalize=True) * 100
plt.bar(severity_counts, height=len(df))
plt.title("bar Chart of Severity")
plt.show()


# Accident Cases vs Months


# Accident Cases vs Different Temperature


# Accident Cases vs Different Humidity


# Accident Cases vs Wind Speed
