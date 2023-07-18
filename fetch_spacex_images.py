import requests
import os
from urllib.parse import urlparse


def save_latest_launch_photo(url, save_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        file.write(response.content)


def get_latest_launch_photos(id='launches/5eb87d47ffd86e000604b38a'):
    os.mkdir('images')
    url = f'https://api.spacexdata.com/v4/{id}'
    response = requests.get(url)
    response.raise_for_status()
    latest_photo = response.json()
    photos = latest_photo['links']['flickr']['original']
    for i, photo in enumerate(photos, start=1):
        extension = get_file_extension(photo)
        save_latest_launch_photo(photo, f'images/image_{i}{extension}')


def get_file_extension(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    extension = os.path.splitext(path)[1]
    return extension


if __name__ == '__main__':
    get_latest_launch_photos()