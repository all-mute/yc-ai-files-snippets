import httpx

headers = {
    "Authorization": "Api-Key YOUR_API_KEY",
    "Content-Type": "application/json"
}

params = {
    "folderId": "YOUR_FOLDER_ID",
    "pageSize": 10
}

response = httpx.get(
    "https://assistant.api.cloud.yandex.net/foundation-models/v1/files",
    headers=headers,
    params=params
) 