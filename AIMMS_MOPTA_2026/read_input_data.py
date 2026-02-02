# the AIMMS project is imported from the singleton module to ensure we instantiate it only once
from singleton import my_aimms
import pandas as pd

# Set the input file path
input_file_path = "AIMMS-MOPTA Interfor data v2.xlsx"

# Read all sheets from the input excel file
input_data = pd.read_excel(input_file_path, sheet_name=None)

# Read set of locations
my_aimms.Locations.assign(set(input_data["Locations"]['Location']))

# Assign lon and lat parameters for each location
my_aimms.LocationLon.assign({row['Location']: row['Longitude'] for _, row in input_data["Locations"].iterrows()})
my_aimms.LocationLat.assign({row['Location']: row['Latitude'] for _, row in input_data["Locations"].iterrows()})

# Assign the carrier locations
my_aimms.CarrierLocation.assign({row['Carrier Home']: row['Carrier'] for _, row in input_data["Carriers"].iterrows()})

# Assign the order number data, first convert the list to strings
my_aimms.OrderNumber.assign(list(input_data["Shipments"]['Order Number'].astype(str)))

# Assign the order due dates
my_aimms.OrderDueDate.assign({(str(row['Order Number']), row['Origin'], row['Destination']): str(row['Due Date'])
                              for _, row in input_data["Shipments"].iterrows()})

# Assign lane milage
my_aimms.LaneMileage.assign({(row['Origin'], row['Destination']): row['Mileage']
                             for _, row in input_data["Lanes"].iterrows()})

# Assign lane cost
my_aimms.LaneCost.assign({(row['Origin'], row['Destination']): row['Cost']
                             for _, row in input_data["Lanes"].iterrows()})