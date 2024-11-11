import pytest
from unittest.mock import patch, MagicMock
from helpers.get_data import get_trafikverket_data
from helpers.filter_data import filter_trafikverket_data


@pytest.fixture
def mock_api_response():
    return {
        "RESPONSE": {
            "RESULT": [
                {
                    "Situation": [
                        {
                            "Deviation": [
                                {
                                    "StartTime": "2024-02-20T11:39:08.000+01:00",
                                    "MessageType": "Färjor",
                                },
                                {
                                    "StartTime": "2024-02-27T20:00:16.000+01:00",
                                    "MessageType": "Vägarbete",
                                },
                                {
                                    "StartTime": "2024-03-27T20:00:16.000+01:00",
                                    "MessageType": "Vägarbete",
                                },
                                {
                                    "StartTime": "2024-10-27T20:00:16.000+01:00",
                                    "MessageType": "Vägarbete",
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }


@patch("requests.post")
def test_filter_trafikverket_data(mock_post, mock_api_response):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_api_response
    mock_post.return_value = mock_response

    raw_data = get_trafikverket_data()
    assert raw_data is not None

    start_time = "2024-01-01"
    result = filter_trafikverket_data(raw_data, start_time=start_time)
    assert result is not None
    assert result["total_situations"] == 4
    assert result["message_type_counts"]["Färjor"] == 1
    assert result["message_type_counts"]["Vägarbete"] == 3

    start_time = "2024-10-01"
    result = filter_trafikverket_data(raw_data, start_time=start_time)
    assert result is not None
    assert result["total_situations"] == 1
    assert result["message_type_counts"]["Vägarbete"] == 1
