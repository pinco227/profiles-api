import requests


def client():
    data = {
        "username": "new_user",
        "email": "test@rest.com",
        "password1": "changeme123",
        "password2": "changeme123",
    }

    response = requests.post(
        "http://127.0.0.1:8000/api/rest-auth/registration/",
        data=data)

    # token_h = 'Token dfb13715c492cde0d9d8cba4b921ad91271ceb79'
    # headers = {'Authorization': token_h}

    # response = requests.get('http://127.0.0.1:8000/api/profiles/',
    #                         headers=headers)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
