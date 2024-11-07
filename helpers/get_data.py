import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def get_trafikverket_data():
    url = 'https://api.trafikinfo.trafikverket.se/v2/data.json'
    payload = f"""
    <REQUEST>
        <LOGIN authenticationkey='5c341f5a9438482ca26b412a7c146cea' />
        <QUERY objecttype='Situation' schemaversion='1.5'>
            <INCLUDE>Deviation</INCLUDE>
        </QUERY>
    </REQUEST>
    """
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'})

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Fel vid hämtning av data: {response.status_code}")
        return None
