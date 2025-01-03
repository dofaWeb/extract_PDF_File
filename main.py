import json
from extract import extractAusgrid as Ausgrid, extractEndeavour as Endeavour

# Residential flat Closed -> EA010
# Residential ToU -> EA025

distributor_name = "Ausgrid"
tariff_name = 'Residential Flat'
tariff_code = ""
if distributor_name == "Ausgrid":
    tariff_code = Ausgrid.get_tariff_code_by_name(tariff_name)
elif distributor_name == "Endeavour":
    tariff_code = Endeavour.get_tariff_code_by_name(tariff_name)

# Export to JSON
if tariff_code:
    with open('tariff_codes.json', 'w') as json_file:
        json.dump({"Distributor Name": distributor_name, "Tariff Name": tariff_name, "Tariff Code": tariff_code}, json_file)

print(tariff_code)  # Output: EA010