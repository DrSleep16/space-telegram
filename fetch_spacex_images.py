import requests
import os
from urllib.parse import urlparse


def fetch_spacex_last_launch(url, save_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)


def get_latest_launch_photos(folder_name, id='launches/5eb87d47ffd86e000604b38a'):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    url = f'https://api.spacexdata.com/v4/{id}'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    photos = data['links']['flickr']['original']
    i = 0
    for photo in photos:
        i+=1
        extension = get_file_extension(photo)
        fetch_spacex_last_launch(photo,f'{folder_name}/image_{i}{extension}')


def get_file_extension(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    extension = os.path.splitext(path)[1]
    return extension
