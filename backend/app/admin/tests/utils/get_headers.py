from starlette.testclient import TestClient

from backend.core.conf import settings


def get_token_headers(
    client: TestClient, username: str, password: str
) -> dict[str, str]:
    data = {
        "username": username,
        "password": password,
    }
    response = client.post(
        f"{settings.FASTAPI_API_V1_PATH}/auth/login/swagger", params=data
    )
    response.raise_for_status()
    token_type = response.json()["token_type"]
    access_token = response.json()["access_token"]
    headers = {"Authorization": f"{token_type} {access_token}"}
    return headers
