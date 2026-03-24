from httpx import Client

from clients.authentification.authentication_client import get_authentication_client, LoginRequestDict
from typing import TypedDict


class AuthenticationUserDict(TypedDict):
    """
    Структура данных пользователя для его авторизации
    """
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserDict) -> Client:
    """
    Функция создает экземпляр httpx.Client с аутентификацией пользователя
    :param user: объект AuthenticationUserDict с email, password
    :return: готовый к использованию объект httpx.Client с установленным заголовком Authorization
    """
    authentication_client = get_authentication_client()

    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )
