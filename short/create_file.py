import httpx

headers = {
    "Authorization": "Api-Key YOUR_API_KEY",
    "Content-Type": "application/json"
}

with open("example.txt", "rb") as file:
    file_content = file.read()

data = {
    "folderId": "YOUR_FOLDER_ID",
    "name": "example.txt",
    "description": "Detailed file description",
    "mimeType": "text/plain",
    "content": file_content.decode(),
    "labels": {
        "environment": "testing",
        "purpose": "documentation",
        "version": "1.0",
        "status": "active"
    },
    "expirationConfig": {
        "expirationPolicy": "SINCE_LAST_ACTIVE",
        "ttlDays": "30",
        "expiresAt": "2024-12-31T23:59:59Z"
    },
    "metadata": {
        "key1": "value1",
        "key2": "value2"
    }
}

response = httpx.post(
    "https://assistant.api.cloud.yandex.net/files/v1/files",
    headers=headers,
    json=data
) 