import telegram


TOKEN = '6134575993:AAEFev1WHWIHSTlH4H8jA0JE0cLAY7UsoN4'
bot = telegram.Bot(TOKEN)
bot.sendMessage(chat_id='-1001709184129', text='Hello!')
bot.sendPhoto(chat_id='-1001709184129',photo='https://www.simplilearn.com/ice9/free_resources_article_thumb/what_is_image_Processing.jpg')