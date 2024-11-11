from helpers.get_data import get_trafikverket_data


def test_api_integration():
    result = get_trafikverket_data()
    
    assert result is not None