import requests
import json
import os


class ApiTest(object):
    def __init__(self, test_data=None):
        if test_data is None:
            raise ValueError('No test data provided')
        else:
            self.test_data = test_data

        self._run_test()

    def _run_test(self):
        api_url = self.test_data.get('apiUrl')
        for vector in self.test_data.get('testVectors'):
            inputs = vector.get('input')
            api_call = api_url.format(
                apiKey=os.environ.get('OWM_API_KEY'),
                **inputs
            )
            res = requests.get(api_call)
            body = json.loads(res.text)
            assert (
                res.status_code == vector['expected']['status_code']
            )
            if 'text' in vector['expected']:
                for message_field in vector['expected']['text']:
                    assert (
                        body[message_field] == vector['expected']['text'][message_field]
                    )
