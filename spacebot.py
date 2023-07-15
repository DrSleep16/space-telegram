import telegram
import os
import random
import time


TOKEN = os.getenv('TOKEN')
bot = telegram.Bot(TOKEN)


def publish_photos(directory, channel_id, interval_hours):

    # Получение списка файлов из указанной директории
    photos = os.listdir(directory)
    random.shuffle(photos)  # Перемешивание списка фотографий в случайном порядке

    while True:
        for photo in photos:
            photo_path = os.path.join(directory, photo)
            with open(photo_path, 'rb') as photo_file:
                bot.send_photo(chat_id=channel_id, photo=photo_file)

            time.sleep(interval_hours * 3600)

if __name__ == '__main__':
    directory = 'images/'
    channel_id = os.getenv('CHANNEL_ID')
    interval_hours = int(os.getenv('INTERVAL_HOURS'))
    publish_photos(directory, channel_id, interval_hours)