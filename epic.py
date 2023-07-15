import requests
import os


def download_epic_images(count):
    if not os.path.exists('images'):
        os.makedirs('images')
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    api_key = 'ZDFKgbARwUMVX1fy9enCi2CF8Feli4ewqJFYGasS'
    params = {
        'api_key': api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    images = data[:count]

    for item in images:
        image_name = item['image']
        image_date = item['date'].split()[0].replace('-', '/')
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png'
        image_filename = f'{image_name}.png'
        save_path = os.path.join('images', image_filename)
        response = requests.get(image_url, params=params)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            file.write(response.content)
