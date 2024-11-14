import httpx

headers = {
    "Authorization": "Api-Key YOUR_API_KEY",
    "Content-Type": "application/json"
}

file_id = "YOUR_FILE_ID"

response = httpx.delete(
    f"https://assistant.api.cloud.yandex.net/foundation-models/v1/files/{file_id}",
    headers=headers
)

# Вывод результата
print(response.status_code)