import httpx

headers = {
    "Authorization": "Api-Key YOUR_API_KEY",
    "Content-Type": "application/json"
}

file_id = "YOUR_FILE_ID"

response = httpx.get(
    f"https://assistant.api.cloud.yandex.net/foundation-models/v1/files/{file_id}/getUrl",
    headers=headers
) 