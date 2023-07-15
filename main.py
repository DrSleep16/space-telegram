from epic import download_epic_images
from fetch_spacex_images import get_latest_launch_photos
from apod import download_apod_images

download_epic_images(5, 'epic_images')
get_latest_launch_photos('images',id='launches/5eb87d47ffd86e000604b38a')
download_apod_images(10, 'apod_images')