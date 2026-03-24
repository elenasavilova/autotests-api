from typing import TypedDict
from clients.api_client import APIClient
from httpx import Response

from clients.public_http_builder import get_public_http_client

class User(TypedDict):
    """
    Описание структуры данных пользователя
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса создания пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя
    """
    user: User

class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет создание пользователя.
        :param request: словарь, содержащий email, password, lastName, firstName, middleName
        :return: ответ от сервера - объект httpx.Response
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        """
        Метод инициализирует создание пользователя, возвращает ответ в формате json
        :param request: словарь, содержащий email, password, lastName, firstName, middleName
        :return: ответ от сервера в виде CreateUserResponseDict
        """
        response = self.create_user_api(request)
        return response.json()

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создает экземпляр класса PublicUsersClient с уже настроенным http-клиентом
    :return: готовый к использованию PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())