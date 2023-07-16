from epic import download_epic_images
from fetch_spacex_images import get_latest_launch_photos
from apod import download_apod_images
from spacebot import publish_photos
from dotenv import load_dotenv


if __name__ =='__main__':
    load_dotenv()
    download_epic_images()
    get_latest_launch_photos()
    download_apod_images()
    publish_photos()