import requests
import os


def download_epic_images(api_key, count=5):
    os.makedirs('images')
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_images_data = response.json()
    images = epic_images_data[:count]

    for image in images:
        image_name = image['image']
        image_date = image['date'].split()[0].replace('-', '/')
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png'
        image_filename = f'{image_name}.png'
        save_path = os.path.join('images', image_filename)
        response = requests.get(image_url, params=params)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    download_count = 5
    download_epic_images(download_count)