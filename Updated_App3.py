import os
import pandas as pd
from faker import Faker
import random

# Initialize Faker instance
fake = Faker()

# Function to generate dummy data for a missing file
def generate_dummy_data(num_rows):
    data = {
        "S_No": [i+1 for i in range(num_rows)],
        "Criteria_No_Name": [fake.sentence(nb_words=3) for _ in range(num_rows)],
        "Date": [fake.date_this_decade() for _ in range(num_rows)],
        "Department": [fake.word() for _ in range(num_rows)],
        "Programme_Type": [random.choice(['Workshop', 'Seminar', 'Conference']) for _ in range(num_rows)],
        "Programme_Title": [fake.sentence(nb_words=4) for _ in range(num_rows)],
        "Level": [random.choice(['Undergraduate', 'Postgraduate', 'Doctoral']) for _ in range(num_rows)],
        "From_Date": [fake.date_this_decade() for _ in range(num_rows)],
        "To_Date": [fake.date_this_decade() for _ in range(num_rows)],
        "Days": [random.randint(1, 10) for _ in range(num_rows)],
        "Faculty_Coordinator": [fake.name() for _ in range(num_rows)],
        "Employee_Code": [fake.random_number(digits=5) for _ in range(num_rows)],
        "No._of_Participants": [random.randint(10, 500) for _ in range(num_rows)],
        "Resource_Person_Details": [fake.name() for _ in range(num_rows)],
        "Is_Resource_Person_Alumni": [random.choice(['Yes', 'No']) for _ in range(num_rows)],
        "External_Agency": [random.choice(['Yes', 'No']) for _ in range(num_rows)],
        "External_Agency_Name_Address": [fake.address() for _ in range(num_rows)],
        "File_Name": [f'{fake.word()}_{random.randint(1, 100)}.pdf' for _ in range(num_rows)],
    }
    return pd.DataFrame(data)

# Define the base folder where the monthly folders are located
base_folder = 'C:/Users/SV/Downloads/Externship_7thSem'  # Update with your actual base folder path

# List of months (folder names)
months = ['January 2024', 'February 2024', 'March 2024', 'May 2024', 'July 2024', 'August 2024',
          'September 2024', 'October 2024', 'November 2024', 'December 2024']

# List of all the filenames (e.g., 1.1, 1.2,... 1.54)
file_names = [f'1.{i}' for i in range(1, 55)]  # Assuming files are named as 1.1 to 1.54

# Dictionary to store combined DataFrames for each file
combined_data = {}

# Iterate over each file
for file in file_names:
    # List to store data from all months for the current file
    file_data = []
    
    # Iterate over each month folder
    for month in months:
        file_path = os.path.join(base_folder, month, f'{file}.csv')
        
        # Check if the file exists in the month folder
        if os.path.exists(file_path):
            # Read the CSV file and add a 'Month' column to indicate the month it belongs to
            df = pd.read_csv(file_path)
            df['Month'] = month
            file_data.append(df)
        else:
            # If the file doesn't exist, generate dummy data and add it
            print(f"File {file_path} does not exist, generating dummy data...")
            dummy_data = generate_dummy_data(100)  # Generate 100 rows of dummy data
            dummy_data['Month'] = month
            file_data.append(dummy_data)
    
    # Combine all data for the current file
    if file_data:
        combined_data[file] = pd.concat(file_data, ignore_index=True)

# Output the combined data for each file
output_folder = 'C:/Users/SV/Downloads/Externship/Output'  # Update with your desired output folder path
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Write the combined data to output files
for file, df in combined_data.items():
    output_file_path = os.path.join(output_folder, f'{file}_combined.csv')
    df.to_csv(output_file_path, index=False)
    
    print(f"Combined data for {file} written to {output_file_path}")
