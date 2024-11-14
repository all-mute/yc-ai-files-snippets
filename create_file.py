import os
import httpx
import json
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Получение учетных данных
folder_id = os.getenv("FOLDER_ID")
api_key = os.getenv("YANDEX_API_KEY")

if not folder_id or not api_key:
    print("Ошибка: Не найдены FOLDER_ID или YANDEX_API_KEY в .env файле")
    exit(1)

# Настройка заголовков
headers = {
    "Authorization": f"Api-Key {api_key}",
    "Content-Type": "application/json"
}

# Подготовка данных для запроса
try:
    with open("example.txt", "rb") as file:
        file_content = file.read()
except FileNotFoundError:
    print("Ошибка: Файл example.txt не найден")
    exit(1)

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
try:
    response = httpx.post(
        "https://assistant.api.cloud.yandex.net/files/v1/files",
        headers=headers,
        json=data
    )
    
    # Вывод статуса и заголовков для отладки
    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    print(f"Response Text: {response.text}")
    
    # Проверка статуса
    response.raise_for_status()
    
    # Попытка распарсить JSON
    try:
        result = response.json()
        print("JSON Response:", result)
        
        # Сохранение file_id в файл
        if 'id' in result:
            with open('file_id.txt', 'w') as f:
                f.write(result['id'])
            print(f"File ID сохранен в file_id.txt")
        else:
            print("Ошибка: В ответе отсутствует поле 'id'")
            
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON: {e}")
        print(f"Тело ответа: {response.text}")
        
except httpx.RequestError as e:
    print(f"Ошибка при отправке запроса: {e}")
except httpx.HTTPStatusError as e:
    print(f"Ошибка HTTP: {e}") 