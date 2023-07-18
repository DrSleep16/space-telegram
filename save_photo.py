import requests


def save_photo(url, save_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        file.write(response.content)