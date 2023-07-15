import requests
import os

def download_apod_images(count):
    if not os.path.exists('images'):
        os.makedirs('images')
    url = 'https://api.nasa.gov/planetary/apod'
    api_key = 'ZDFKgbARwUMVX1fy9enCi2CF8Feli4ewqJFYGasS'
    params = {
        'api_key': api_key,
        'count': count
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    for item in data:
        image_url = item['url']
        image_filename = os.path.basename(image_url)
        save_path = os.path.join('images/', image_filename)
        response = requests.get(image_url)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            file.write(response.content)
