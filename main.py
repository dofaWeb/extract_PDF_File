import json
from extract.extract import get_tariff_code_by_name

# Residential flat Closed -> EA010
# Residential ToU -> EA025

tariff_name = 'Residential flat Closed'
tariff_code = get_tariff_code_by_name(tariff_name)

# Export to JSON
if tariff_code:
    with open('tariff_codes.json', 'w') as json_file:
        json.dump({"Tariff Name": tariff_name, "Tariff Code": tariff_code}, json_file)

print(tariff_code)  # Output: EA010