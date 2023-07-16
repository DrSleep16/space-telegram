import requests
import os

def download_apod_images(api_key, count=5):
    os.makedirs('images')
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': count
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    apod_images_data = response.json()

    for apod_image in apod_images_data:
        image_url = apod_image['url']
        image_filename = os.path.basename(image_url)
        save_path = os.path.join('images/', image_filename)
        response = requests.get(image_url)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    download_count = 5
    download_apod_images(download_count)