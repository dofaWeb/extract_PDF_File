import pdfplumber
import pandas as pd

# Open the PDF and extract the data
with pdfplumber.open('file/Ausgrid-Network-Price-List-2024-25.pdf') as pdf:
    tables = []
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            tables.extend(table)

# Initialize an empty list to store the extracted data
extracted_data = []

# Iterate over each row in the table
for row in tables:
    # Check if the row has enough columns to contain Tariff Code and Tariff Name
    if len(row) > 4:
        # Extract the Tariff Code (index 3) and Tariff Name (index 4)
        tariff_code = row[3]
        tariff_name = row[4]
        
        # Clean the data by removing newline characters
        tariff_code = tariff_code.replace('\n', '').strip() if tariff_code else tariff_code
        tariff_name = tariff_name.replace('\n', '').strip() if tariff_name else tariff_name
        
        # Include only valid rows where both Tariff Code and Tariff Name are not None
        if tariff_code and tariff_name:
            extracted_data.append([tariff_code, tariff_name])

# Convert to a pandas DataFrame for tabular display
df = pd.DataFrame(extracted_data, columns=["Tariff Code", "Tariff Name"])

# Display the result
# print(df)

def get_tariff_code_by_name(tariff_name):
    # Clean the input tariff name
    cleaned_name = tariff_name.replace('\n', '').strip()
    
    # Search for the cleaned tariff name in the DataFrame
    result = df[df['Tariff Name'].str.strip() == cleaned_name]
    
    # Return the corresponding Tariff Code if found, else return None
    if not result.empty:
        return result['Tariff Code'].iloc[0]
    return None