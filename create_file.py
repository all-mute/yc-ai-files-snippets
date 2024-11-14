import os
import httpx
import json
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Получение учетных данных
folder_id = os.getenv("FOLDER_ID")
api_key = os.getenv("YANDEX_API_KEY")

# Настройка заголовков
headers = {
    "Authorization": f"Api-Key {api_key}",
    "Content-Type": "application/json"
}

# Подготовка данных для запроса
with open("example.txt", "rb") as file:
    file_content = file.read()

data = {
    "folderId": folder_id,
    "name": "example.txt",
    "description": "Подробное описание файла для тестирования API",
    "mimeType": "text/plain",
    "content": file_content.decode(),
    "labels": {
        "environment": "testing",
        "purpose": "documentation"
    },
    "expirationConfig": {
        "expirationPolicy": "SINCE_LAST_ACTIVE",
        "ttlDays": "30"
    }
}

# Отправка запроса
response = httpx.post(
    "https://assistant.api.cloud.yandex.net/foundation-models/v1/files",
    headers=headers,
    json=data
)

# Вывод результата
result = response.json()
print(result)

# Сохранение file_id в файл
if 'id' in result:
    with open('file_id.txt', 'w') as f:
        f.write(result['id']) 