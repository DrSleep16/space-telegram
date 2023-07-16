import telegram
import os
import random
import time


def publish_photos(channel_id, interval_hours, directory='images/', choose_photo=None):
    photos = os.listdir(directory)
    random.shuffle(photos)

    while True:
        for photo in photos:
            photo_path = os.path.join(directory, photo)
            with open(photo_path, 'rb') as photo_file:
                if choose_photo is not None:
                    BOT.send_photo(chat_id=channel_id, photo=choose_photo)
                else:
                    BOT.send_photo(chat_id=channel_id, photo=photo_file)
            time.sleep(interval_hours * 3600)


if __name__ == '__main__':
    TOKEN = os.getenv('TG_TOKEN')
    BOT = telegram.Bot(TOKEN)
    directory = 'images/'
    channel_id = os.getenv('TG_CHANNEL_ID')
    interval_hours = int(os.getenv('PUBLISH_INTERVAL_HOURS'))
    publish_photos(channel_id, interval_hours, directory)