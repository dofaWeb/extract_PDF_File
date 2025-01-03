import pdfplumber
import pandas as pd

# Open the PDF and extract the data
with pdfplumber.open('file/Endeavour_NUOS-Price-List-202425-v1.0.pdf') as pdf:
    tables = []
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            tables.extend(table)

# Initialize an empty list to store the extracted data
extracted_data = []

# Iterate over each row in the table
for row in tables:
    # Check if the row has enough columns to contain the data of interest
    if len(row) > 2:  # Adjust column index based on your PDF's structure
        # Extract the first two columns (adjust indices as needed)
        column_1 = row[0]  # First column
        column_2 = row[1]  # Second column
        
        # Clean the data by removing newline characters
        column_1 = column_1.replace('\n', '').strip() if column_1 else column_1
        column_2 = column_2.replace('\n', '').strip() if column_2 else column_2
        
        # Include only valid rows where both columns are not None
        if column_1 and column_2:
            extracted_data.append([column_1, column_2])

# Convert to a pandas DataFrame for tabular display
df = pd.DataFrame(extracted_data, columns=["Tariff Code", "Tariff Name"])  # Adjust column names as needed

# Define a function to search for a value in the second column and return the corresponding first column
def get_tariff_code_by_name(column_2_value):
    # Clean the input value
    cleaned_value = column_2_value.replace('\n', '').strip().lower()
    
    # Search for the cleaned value in the DataFrame
    result = df[df['Tariff Name'].str.strip().str.lower() == cleaned_value]
    
    # Return the corresponding first column value if found, else return None
    if not result.empty:
        return result['Tariff Code'].iloc[0]
    return None
