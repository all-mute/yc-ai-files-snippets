import os
import httpx
from dotenv import load_dotenv

load_dotenv()

folder_id = os.getenv("FOLDER_ID")
api_key = os.getenv("YANDEX_API_KEY")

headers = {
    "Authorization": f"Api-Key {api_key}",
    "Content-Type": "application/json"
}

# Параметры запроса
params = {
    "folderId": folder_id,
    "pageSize": 10,  # Количество файлов на странице
    "pageToken": ""  # Токен для получения следующей страницы
}

# Отправка запроса
response = httpx.get(
    "https://assistant.api.cloud.yandex.net/foundation-models/v1/files",
    headers=headers,
    params=params
)

# Вывод результата
print(response.json()) 