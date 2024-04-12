#This script is similar to GetDeficiencies, however outputs all data into a CSV file.

from zeep import Client
from zeep.helpers import serialize_object
import csv
import datetime

from Full_VesselID_List import VesselID_list

wsdl_url = 'https://cgmix.uscg.mil/xml/PSIXData.asmx?WSDL'
client = Client(wsdl=wsdl_url)

def format_datetime(dt):
    """Format datetime with timezone into a string."""
    if dt:
        return dt.strftime('%Y-%m-%d %H:%M:%S %z')
    return 'None'

def parse_and_extract_data(data):
    """Parse the given response data and extract necessary fields."""
    extracted_data = []
    for case_dict in data['_value_1']['_value_1']:
        case = serialize_object(case_dict['VesselCases'])
        # Verify fields exist with One Off/GetDeficiencies.py and add them here
        extracted_data.append([
            case['VesselId'],
            case['ActivityId'],
            case.get('CasesId', 'None'),  # Now safe to use .get()
            format_datetime(case['StartDtTm']),
            case['TypeLookupName'],
            case['ProcessStatusSubTypeLookupName'],
            case['ProcessStatusTypeLookupName'],
            case['USCGZonePort']
        ])
    return extracted_data

output_file = 'vessel_data.csv'
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['VesselId', 'ActivityId', 'CasesId', 'StartDtTm', 'TypeLookupName', 'ProcessStatusSubTypeLookupName', 'ProcessStatusTypeLookupName', 'USCGZonePort'])

    try:
        for VesselID in VesselID_list:
            response = client.service.getVesselCases(VesselID)
            data_to_write = parse_and_extract_data(response)
            for item in data_to_write:
                writer.writerow(item)

    except Exception as e:
        print(f"Error calling service: {e}")

print(f"Data written to {output_file}")