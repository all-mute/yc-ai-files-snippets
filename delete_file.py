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

# Чтение file_id из файла
try:
    with open('file_id.txt', 'r') as f:
        file_id = f.read().strip()
except FileNotFoundError:
    print("Файл file_id.txt не найден. Сначала создайте файл через create_file.py")
    exit(1)

# Отправка запроса
response = httpx.delete(
    f"https://assistant.api.cloud.yandex.net/foundation-models/v1/files/{file_id}",
    headers=headers
)

# Вывод результата
print(response.status_code)

# Удаление file_id.txt после успешного удаления файла
if response.status_code == 200:
    try:
        os.remove('file_id.txt')
        print("Файл file_id.txt удален")
    except FileNotFoundError:
        pass