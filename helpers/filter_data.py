from datetime import datetime
from collections import Counter


def filter_trafikverket_data(data, start_time=None):
    if start_time:
        start_time = datetime.strptime(start_time, "%Y-%m-%d")

    filtered_data = []
    total_situations = 0
    message_type_counter = Counter()

    for result in data.get('RESPONSE', {}).get('RESULT', []):
        for situation in result.get('Situation', []):
            for deviation in situation.get('Deviation', []):
                deviation_start_time_str = deviation.get("StartTime", "")
                if deviation_start_time_str:
                    deviation_start_time = datetime.strptime(
                        deviation_start_time_str, "%Y-%m-%dT%H:%M:%S.%f%z"
                    ).replace(tzinfo=None)

                    if start_time is None or deviation_start_time >= start_time:
                        filtered_data.append(deviation)
                        total_situations += 1
                        message_type_counter[deviation.get("MessageType", "Okänd")] += 1

    return {
        "filtered_data": filtered_data,
        "total_situations": total_situations,
        "message_type_counts": message_type_counter
    }
