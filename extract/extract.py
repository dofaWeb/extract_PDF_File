import pdfplumber

with pdfplumber.open('file/Ausgrid-Network-Price-List-2024-25.pdf') as pdf:
    for page in pdf.pages:
        print(page.extract_table())