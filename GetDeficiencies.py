from zeep import Client

wsdl_url = 'https://cgmix.uscg.mil/xml/PSIXData.asmx?WSDL'
client = Client(wsdl=wsdl_url)

activity_number = REPLACE_WITH_INT  # Get VesselID using https://cgmix.uscg.mil/PSIX/PSIXSearch.aspx and search the vessel in question with the Activity Number here. This will show the VesselID to use in GetCases.py

try:
    response = client.service.getVesselDeficienciesXMLString(ActivityNumber=activity_number)
    print(response)
except Exception as e:
    print(f"Error calling service: {e}")
