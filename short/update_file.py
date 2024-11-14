import httpx

headers = {
    "Authorization": "Api-Key YOUR_API_KEY",
    "Content-Type": "application/json"
}

file_id = "YOUR_FILE_ID"

with open("example.txt", "rb") as file:
    file_content = file.read()

data = {
    "content": file_content.decode(),
    "description": "Updated detailed description",
    "labels": {
        "environment": "production",
        "purpose": "documentation",
        "version": "2.0",
        "status": "updated"
    },
    "expirationConfig": {
        "expirationPolicy": "STATIC",
        "ttlDays": "60",
        "expiresAt": "2024-12-31T23:59:59Z"
    },
    "metadata": {
        "updated_by": "user123",
        "update_reason": "content revision",
        "custom_field": "custom value"
    }
}

response = httpx.patch(
    f"https://assistant.api.cloud.yandex.net/foundation-models/v1/files/{file_id}",
    headers=headers,
    json=data
) 