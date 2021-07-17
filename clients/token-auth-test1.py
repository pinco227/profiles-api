import requests


def client():
    # credentials = {"username": "pinco", "password": "#######"}

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
    #                          data=credentials)

    token_h = 'Token 48f7a69ffe8827f52982fd9b3b5c114d98e8ce55'
    headers = {'Authorization': token_h}

    response = requests.get('http://127.0.0.1:8000/api/profiles/',
                            headers=headers)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
