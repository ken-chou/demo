from owm_api_tests.common import api_test


def test_zip_code_happy_path():
    test_data = {
        "apiUrl": "https://api.openweathermap.org/data/2.5/weather?zip={zipCode},{countryCode}&appid={apiKey}",
        "testVectors": [
            { # with lowercase country code
                "input": {
                    "zipCode": "94040",
                    "countryCode": "us"
                },
                "expected": {
                    "status_code": 200,
                }
            }, # no country code
            {
                "input": {
                    "zipCode": "94040",
                    "countryCode": ""
                },
                "expected": {
                    "status_code": 200,
                }
            },
            { # with uppercase country code
                "input": {
                    "zipCode": "94040",
                    "countryCode": "US"
                },
                "expected": {
                    "status_code": 200,
                }
            },
            { # with CamelCase country code
                "input": {
                    "zipCode": "94040",
                    "countryCode": "Us"
                },
                "expected": {
                    "status_code": 200,
                }
            }
        ]
    }
    api_test.ApiTest(test_data)

def test_zip_code_invalid():
    test_data = {
        "apiUrl": "https://api.openweathermap.org/data/2.5/weather?zip={zipCode},{countryCode}&appid={apiKey}",
        "testVectors": [
            { # invalid zip code with country code
                "input": {
                    "zipCode": "c4f3b4b3",
                    "countryCode": "us"
                },
                "expected": {
                    "status_code": 404,
                    "text": {
                        "message": "city not found"
                    }
                }
            },
            { # invalid zip code with no country code
                "input": {
                    "zipCode": "c4f3b4b3",
                    "countryCode": ""
                },
                "expected": {
                    "status_code": 404,
                    "text": {
                        "message": "city not found"
                    }
                }
            }
        ]
    }
    api_test.ApiTest(test_data)
