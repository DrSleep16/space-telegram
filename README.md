**Описание проекта: Скрипты для скачивания и публикации фотографий космоса**

Проект состоит из четырех скриптов: `apod.py`, `epic.py`, `spacebot.py` и `fetch_spacex_images.py`, которые позволяют скачивать фотографии космоса с различных сервисов и публиковать их в Telegram-канале. Вспомогательный скрипт `main.py` позволяет автоматически запускать последовательное скачивание изображений.

**Содержание скриптов:**

1. `apod.py`: Скачивает фотографии Astronomy Picture of the Day (APOD) от NASA с использованием NASA API. Фотографии предоставляют уникальные и интересные изображения космоса каждый день.

2. `epic.py`: Скачивает фотографии Earth Polychromatic Imaging Camera (EPIC) от NASA с использованием NASA API. EPIC расположена на спутнике DSCOVR и предоставляет полные дисковые изображения Земли с уникальной перспективой, включая астрономические события, такие как лунные транзиты.

3. `fetch_spacex_images.py`: Скачивает последние фотографии с последнего запуска SpaceX с использованием SpaceX API. Фотографии представляют моменты запуска и посадки ракеты, а также другие интересные моменты в процессе запуска.

4. `spacebot.py`:
Скрипт spacebot.py представляет собой Telegram-бота, который публикует фотографии космоса в заданный Telegram-канал. Бот использует Telegram API для отправки фотографий.
5. `main.py`: Вспомогательный скрипт, который позволяет автоматически запускать последовательное скачивание фотографий с помощью скриптов `apod.py`, `epic.py`,`spacebot.py` и `fetch_spacex_images.py`. Это упрощает процесс получения и сохранения фотографий космоса, а также фотографий с последнего запуска SpaceX.

**Используемые сервисы:**

- NASA API: Используется для получения фотографий с сайта NASA, таких как Astronomy Picture of the Day (APOD) и Earth Polychromatic Imaging Camera (EPIC).

- SpaceX API: Используется для получения фотографий с последнего запуска SpaceX.

- Telegram API: Используется для публикации скачанных фотографий в Telegram-канале.

**Польза от проекта:**

- Получение интересных и красивых фотографий космоса: С помощью скриптов можно автоматически скачивать уникальные и захватывающие изображения космоса, предоставляемые NASA и SpaceX.

- Публикация в Telegram-канале: Скрипт `main.py` автоматизирует процесс скачивания и публикации фотографий в Telegram-канале, что позволяет регулярно обновлять канал интересными космическими изображениями.

- Изучение космоса: Проект предоставляет удобный способ изучения космических событий и фотографий, которые редко встречаются в повседневной жизни.

Этот проект поможет пользователям получить доступ к удивительным фотографиям космоса и разнообразным космическим событиям, а также автоматизировать их публикацию для интересующихся и поклонников космических открытий.

Для использования переменных окружения в Python можно воспользоваться модулем `python-dotenv`, который позволяет загружать переменные окружения из файла `.env`, расположенного в корневой папке проекта. В файле `.env` можно хранить конфиденциальные данные, такие как API-ключи, в формате `KEY=VALUE`.

**Инструкция для использования переменных окружения:**

1. Создайте файл `.env` в корневой папке проекта.
2. В файле `.env` определите переменную `SPACE_API_KEY` и укажите в ней ваш API-ключ, например:
   ```
   SPACE_API_KEY=YOUR_API_KEY_HERE
   ```
3. Аналогично определите переменные `TG_CHANNEL_ID` (id вашего канала в телеграмме),`PUBLISH_INTERVAL_HOURS` (частота публикаций в канале), `TG_TOKEN` (токен вашего бота).
4. Установите библиотеку `python-dotenv`, если она еще не установлена:
   ```
   pip install python-dotenv
   ```
5. Теперь вы можете использовать переменные окружения в вашем коде, не опасаясь, что они попадут в общий репозиторий.

**Инструкция по использованию вспомогательного скрипта main.py:**

1. Установите необходимые зависимости:
   - Убедитесь, что у вас установлен Python на вашем компьютере.
   - Установите библиотеку `requests`, если она ещё не установлена, выполнив команду:
     ```
     pip install requests
     ```

2. Создайте файл `main.py` и скопируйте в него код.

3. Убедитесь, что у вас настроены и работают скрипты `spacebot.py`, `epic.py`, `fetch_spacex_images.py` и `apod.py`. Если какой-то из этих скриптов не настроен, следуйте инструкциям, предоставленным для каждого из них.

4. Запустите скрипт:
   - Откройте командную строку или терминал.
   - Перейдите в каталог, где находится файл `main.py`.
   - Выполните следующую команду:
     ```
     python main.py
     ```
   - Скрипт начнет запускать последовательно функции `spacebot.py`, `download_epic_images()`, `get_latest_launch_photos()` и `download_apod_images()` для скачивания и отправки соответствующих изображений.

5. Дождитесь завершения выполнения скрипта. После этого все необходимые изображения будут скачаны и сохранены в соответствующих папках.

Теперь вы можете использовать вспомогательный скрипт `main.py`, чтобы автоматически запустить скачивание изображений с помощью скриптов `epic.py`, `fetch_spacex_images.py` и `apod.py`, а также отправлять их в телеграмм-канал при помощи `spacebot.py`. Это упростит процесс получения и сохранения фотографий космоса, а также фотографий с последнего запуска SpaceX.


**Инструкция по использованию скрипта fetch_spacex_images.py:**

1. Установите необходимые зависимости:
   - Убедитесь, что у вас установлен Python на вашем компьютере.
   - Установите библиотеку `requests`, если она ещё не установлена, выполнив команду:
     ```
     pip install requests
     ```

2. Создайте файл `fetch_spacex_images.py` и скопируйте в него код.

3. Создайте папку с именем `images` в том же каталоге, где находится файл `fetch_spacex_images.py`. Это будет место для сохранения скачанных изображений.

4. Запустите скрипт:
   - Откройте командную строку или терминал.
   - Перейдите в каталог, где находится файл `fetch_spacex_images.py`.
   - Выполните следующую команду:
     ```
     python fetch_spacex_images.py
     ```
   - Скрипт начнет загружать последние фотографии запуска SpaceX и сохранять их в папке `images`.

5. Дождитесь завершения выполнения скрипта. После этого в папке `images` появятся скачанные фотографии.

Теперь вы успешно загрузили последние фотографии запуска SpaceX с использованием скрипта `fetch_spacex_images.py` и сохранены в папке `images`.


**Инструкция по использованию скрипта epic.py:**

1. Установите необходимые зависимости:
   - Убедитесь, что у вас установлен Python на вашем компьютере.
   - Установите библиотеку `requests`, если она ещё не установлена, выполнив команду:
     ```
     pip install requests
     ```

2. Создайте файл `epic.py` и скопируйте в него код.

3. Получите API-ключ от NASA:
   - Перейдите на веб-сайт [NASA API](https://api.nasa.gov/).
   - Создайте учетную запись и получите API-ключ.
   - Сохраните полученный API-ключ.

4. Опционально: Измените значение переменной `download_count` в функции `download_epic_images`, если вы хотите скачать больше или меньше 5 изображений:
   ```python
   download_count = 5  # Здесь число 5 определяет количество изображений для скачивания
   ```

6. Создайте папку с именем `images` в том же каталоге, где находится файл `epic.py`. Это будет место для сохранения скачанных изображений.

7. Запустите скрипт:
   - Откройте командную строку или терминал.
   - Перейдите в каталог, где находится файл `epic.py`.
   - Выполните следующую команду:
     ```
     python epic.py
     ```
   - Скрипт начнет скачивать изображения с использованием вашего API-ключа от NASA и сохранять их в папке `images`.

8. Дождитесь завершения выполнения скрипта. После этого в папке `images` появятся скачанные изображения.

Теперь вы успешно скачали изображения с Earth Polychromatic Imaging Camera (EPIC) от NASA с использованием скрипта `epic.py` и сохранены в папке `images`.


**Инструкция по использованию скрипта apod.py:**

1. Установите необходимые зависимости:
   - Убедитесь, что у вас установлен Python на вашем компьютере.
   - Установите библиотеку `requests`, если она ещё не установлена, выполнив команду:
     ```
     pip install requests
     ```

2. Создайте файл `apod.py` и скопируйте в него код.

3. Получите API-ключ от NASA:
   - Перейдите на веб-сайт [NASA API](https://api.nasa.gov/).
   - Создайте учетную запись и получите API-ключ.
   - Сохраните полученный API-ключ.

4. Опционально: Измените значение переменной download_count в функции `download_apod_images`, если вы хотите скачать больше или меньше 5 изображений:
   ```python
   download_count = 5  # Здесь число 5 определяет количество изображений для скачивания
   ```

5. Создайте папку с именем `images` в том же каталоге, где находится файл `apod.py`. Это будет место для сохранения скачанных изображений.

6. Запустите скрипт:
   - Откройте командную строку или терминал.
   - Перейдите в каталог, где находится файл `apod.py`.
   - Выполните следующую команду:
     ```
     python apod.py
     ```
   - Скрипт начнет скачивать изображения с использованием вашего API-ключа от NASA и сохранять их в папке `images`.

7. Дождитесь завершения выполнения скрипта. После этого в папке `images` появятся скачанные изображения.

Теперь вы успешно скачали изображения Astronomy Picture of the Day (APOD) от NASA с использованием скрипта `apod.py` и сохрали их в папке `images`.


## Инструкция по использованию скрипта для публикации фотографий в Telegram-канал

1. Установите необходимые зависимости, если они ещё не установлены. Для этого введите в командной строке:
   ```
   pip install python-telegram-bot==13.0
   ```

2. Получите токен для вашего Telegram-бота. Если у вас ещё нет бота, создайте его с помощью @BotFather в Telegram.

3. Скачайте скрипт `space_bot.py` и откройте его в текстовом редакторе.

4. Добавьте переменную окружения TG_TOKEN, значением которого будет полученный токен.

5. Укажите путь к директории с фотографиями, которые вы хотите опубликовать в Telegram-канале. Найдите следующую строку в скрипте:
   ```python
   directory = 'images/'
   ```
   Замените `'images/'` на путь к директории с фотографиями.

6. Укажите идентификатор вашего Telegram-канала, в который будут отправляться фотографии. Для этого укажите его в переменной окружения TG_CHANNEL_ID.

7. Укажите интервал публикации фотографий в часах. Для этого укажите его в переменной окружения PUBLISH_INTERVAL_HOURS.
8. По желанию можно указать четвертый аргумент - путь к своему изображению.
9. Сохраните изменения в скрипте.

10. Откройте терминал или командную строку и перейдите в каталог, где находится скрипт `spacebot.py`.

11. Запустите скрипт с помощью команды:
    ```
    python spacebot.py
    ```

12. Скрипт начнет публикацию фотографий из указанной директории в ваш Telegram-канал с заданным интервалом. Если все фотографии были опубликованы, скрипт начнет публикацию заново, перемешивая фотографии.

13. Для остановки скрипта нажмите сочетание клавиш `Ctrl + C` в терминале или командной строке.

Теперь ваш бот будет автоматически публиковать фотографии из указанной директории в ваш Telegram-канал с заданным интервалом. Вы можете добавлять или удалять фотографии из директории, и бот будет автоматически адаптироваться к изменениям.