import requests
import os
from save_photo import save_photo
from dotenv import load_dotenv
import argparse

def download_epic_images(api_key, count=5):
    os.makedirs('images')
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_images = response.json()
    images = epic_images[:count]

    for image in images:
        image_name = image['image']
        image_date = image['date'].split()[0].replace('-', '/')
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png'
        image_filename = f'{image_name}.png'
        image_path = os.path.join('images', image_filename)
        save_photo(image_url, image_path)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('SPACE_API_KEY')
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--download_count',
        '-d', type=int,
        required=True,
        help='Количество скачиваемых фотографий'
    )
    args = parser.parse_args()
    download_count = args.download_count
    download_epic_images(api_key,download_count)