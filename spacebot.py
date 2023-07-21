import telegram
import os
import random
import time


def publish_photos(channel_id, interval_hours, token, directory='images/'):
    photos = os.listdir(directory)
    random.shuffle(photos)
    bot = telegram.Bot(token)
    while True:
        for photo in photos:
            photo_path = os.path.join(directory, photo)
            with open(photo_path, 'rb') as photo_file:
                bot.send_photo(chat_id=channel_id, photo=photo_file)
            time.sleep(interval_hours * 3600)


if __name__ == '__main__':
    directory = 'images/'
    channel_id = os.getenv('TG_CHANNEL_ID')
    interval_hours = int(os.getenv('PUBLISH_INTERVAL_HOURS'))
    token = os.getenv('TG_TOKEN')
    publish_photos(channel_id, interval_hours, token, directory)