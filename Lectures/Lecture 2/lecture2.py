
import requests
from requests.exceptions import HTTPError


def get_response_example():
    response = requests.get('https://api.github.com/helloworld')

    print(response.status_code)

    if response.status_code == 200:
        print("Success!")
    if response.status_code == 404:
        print("Not found!")

    if response.status_code:
        print("Success!")
    else:
        print("Error!")


def bool_values():
    class MyClass:
        def __init__(self, value: int = 0):
            self.value = value

        def __bool__(self):
            return self.value != 0


    m = MyClass(5)
    print(m.value)

    if m:
        print("Value is set")
    else:
        print("Value is not set")


def request_exceptions():
    try:
        response = requests.get('https://api.github.com/')

        # Om response var "successful", gör inget. Annars raise exception
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print(f'Success! {response.status_code}')
        data = response.json()  # Avkoda dokumentet som JSON. Sparas som en Python-dict
        print(response.headers['content-type'])  # Inspektera data i headern
        print(response.encoding)  # Encoding som kommer från content-type


def request_with_params_and_headers():
    response = requests.get('https://api.github.com/search/repositories',
                            params={'q': 'requests+language:python'},
                            headers={'Accept': 'application/vnd.github.v3.text-match+json'})

    data = response.json()
    first_hit = data['items'][0]
    print(first_hit['name'])
    print(first_hit['description'])
    print(first_hit['text_matches'])


def request_with_other_methods():
    response = requests.head('https://httpbin.org/get')
    print(response.headers['Content-Type'])
    print(response.text)

    response = requests.delete('https://httpbin.org/delete')
    print(response.status_code)
    print(response.text)

    response = requests.post('https://httpbin.org/post', json={'key': 'value'})
    # application/x-www-form-urlencoded
    print(response.status_code)

    # Inspektera hur vår fråga såg ut
    print(response.request.url)


def requests_with_auth():
    # Rätt login ger 200 OK, fel ger 401
    request = requests.get('https://httpbin.org/basic-auth/kyhtest/abcde', auth=('kyhtest', 'hemligt'))
    print('Response code', request.status_code)
    print('Response content:\n', request.text)
