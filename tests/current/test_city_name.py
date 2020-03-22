from owm_api_tests.common import api_test


def test_city_name_happy_paths():
    test_data = {
        "apiUrl": "https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}",
        "testVectors": [
            {
                "input": {
                    "cityName": "London"
                },
                "expected": {
                    "status_code": 200,
                }
            },
            { # all caps
                "input": {
                    "cityName": "LONDON"
                },
                "expected": {
                    "status_code": 200,
                }
            },
            { # lower case
                "input": {
                    "cityName": "london"
                },
                "expected": {
                    "status_code": 200,
                }
            },
        ]
    }
    api_test.ApiTest(test_data)


def test_city_name_does_not_exist():
    test_data = {
        "apiUrl": "https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}",
        "testVectors": [
            {
                "input": {
                    "cityName": "Shambala"
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


def test_city_name_numbers():
    test_data = {
        "apiUrl": "https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}",
        "testVectors": [
            { # Arabic numbers
                "input": {
                    "cityName": "29 Palms"
                },
                "expected": {
                    "status_code": 404,
                    "text": {
                        "message": "city not found"
                    }
                }
            },
            { # Written numbers
                "input": {
                    "cityName": "Twentynine Palms"
                },
                "expected": {
                    "status_code": 200,
                }
            }
        ]
    }
    api_test.ApiTest(test_data)


def test_city_name_special_character():
    test_data = {
        "apiUrl": "https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}",
        "testVectors": [
            { # dash
                "input": {
                    "cityName": "Milton-Freewater"
                },
                "expected": {
                    "status_code": 200,
                }
            },
            { # multiple dashes
                "input": {
                    "cityName": "Stratford-upon-Avon"
                },
                "expected": {
                    "status_code": 200,
                }
            },
            { # space
                "input": {
                    "cityName": "New York"
                },
                "expected": {
                    "status_code": 200,
                }
            },
            { # multiple spaces
                "input": {
                    "cityName": "Ho Chi Minh City"
                },
                "expected": {
                    "status_code": 200,
                }
            }
        ]
    }
    api_test.ApiTest(test_data)

def test_city_name_leading_spaces():
    test_data = {
        "apiUrl": "https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}",
        "testVectors": [
            { # leading space
                "input": {
                    "cityName": " New York"
                },
                "expected": {
                    "status_code": 200,
                }
            },
            { # two leading spaces
                "input": {
                    "cityName": "  New York"
                },
                "expected": {
                    "status_code": 200,
                }
            }
        ]
    }
    api_test.ApiTest(test_data)

def test_city_name_trailing_spaces():
    test_data = {
        "apiUrl": "https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}",
        "testVectors": [
            { # trailing space
                "input": {
                    "cityName": "New York "
                },
                "expected": {
                    "status_code": 200,
                }
            },
            { # two trailing spaces
                "input": {
                    "cityName": "New York  "
                },
                "expected": {
                    "status_code": 200,
                }
            }
        ]
    }
    api_test.ApiTest(test_data)

def test_city_name_quoted():
    test_data = {
        "apiUrl": "https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}",
        "testVectors": [
            { # single quoted
                "input": {
                    "cityName": "\'New York\'"
                },
                "expected": {
                    "status_code": 404,
                }
            },
            { # double quoted
                "input": {
                    "cityName": "\"New York\""
                },
                "expected": {
                    "status_code": 404,
                }
            }
        ]
    }
    api_test.ApiTest(test_data)