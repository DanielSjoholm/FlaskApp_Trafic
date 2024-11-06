from datetime import datetime, timedelta
from collections import Counter
import requests

def _get_trafikverket_data(start_time=None):
    url = 'https://api.trafikinfo.trafikverket.se/v2/data.json'

    if start_time:
        start_time = datetime.strptime(start_time, "%Y-%m-%d")

    payload = """
    <REQUEST>
        <LOGIN authenticationkey='5c341f5a9438482ca26b412a7c146cea' />
        <QUERY objecttype='Situation' schemaversion='1.5'>
            <INCLUDE>Deviation</INCLUDE>
        </QUERY>
    </REQUEST>
    """
    
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'})

    if response.status_code == 200:
        filtered_data = []
        data = response.json()

        total_situations = 0
        message_type_counter = Counter()

        for result in data['RESPONSE']['RESULT']:
            for situation in result.get('Situation', []):
                for deviation in situation.get('Deviation', []):
                    deviation_start_time_str = deviation.get("StartTime", "")
                    if deviation_start_time_str:
                        deviation_start_time = datetime.strptime(deviation_start_time_str, "%Y-%m-%dT%H:%M:%S.%f%z").replace(tzinfo=None)
                        if start_time and deviation_start_time >= start_time:
                            filtered_data.append(deviation)
                            total_situations += 1
                            message_type_counter[deviation.get("MessageType", "Okänd")] += 1
        return {
            "filtered_data": filtered_data,
            "total_situations": total_situations,
            "message_type_counts": message_type_counter
        }
    else:
        print(f"Fel vid hämtning av data: {response.status_code}")
        return None