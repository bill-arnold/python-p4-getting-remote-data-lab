# lib/get_requester.py
import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        print(response.content)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)

# Uncomment the following lines to run the tests
if __name__ == '__main__':
    url_to_test = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
    requester = GetRequester(url_to_test)

    # Print response body
    print("Response Body:")
    requester.get_response_body()

    # Print JSON data
    print("\nJSON Data:")
    json_data = requester.load_json()
    print(json_data)
