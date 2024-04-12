# This script gets a full list of cases for a vessel using the VesselID

from zeep import Client

wsdl_url = 'https://cgmix.uscg.mil/xml/PSIXData.asmx?WSDL'
client = Client(wsdl=wsdl_url)

VesselID = REPLACE_WITH_INT # Use GetDeficiencies.py to get the VesselID 

try:
    response = client.service.getVesselCases(VesselID)
    print(response)
except Exception as e:
    print(f"Error calling service: {e}")