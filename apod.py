import requests
import os
from save_photo import save_photo


def download_apod_images(api_key, count=5):
    os.makedirs('images')
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': count
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    apod_images = response.json()

    for apod_image in apod_images:
        image_url = apod_image['url']
        image_filename = os.path.basename(image_url)
        image_path = os.path.join('images/', image_filename)
        save_photo(image_url, image_path)


if __name__ == '__main__':
    download_count = 5
    download_apod_images(download_count)