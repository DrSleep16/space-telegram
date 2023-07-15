import telegram
import os
import random
import time


TOKEN = os.getenv('TOKEN')
BOT = telegram.Bot(TOKEN)


def publish_photos(directory='images/', channel_id=os.getenv('CHANNEL_ID'), interval_hours=int(os.getenv('CHANNEL_ID')), choose_photo=None):
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
    directory = 'images/'
    channel_id = os.getenv('CHANNEL_ID')
    interval_hours = int(os.getenv('INTERVAL_HOURS'))
    publish_photos(directory, channel_id, interval_hours)