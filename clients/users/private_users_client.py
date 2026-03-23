from httpx import Response
from clients.api_client import APIClient
from typing import TypedDict

class UpdateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на частичное изменение информации о пользователе
    """
    email: str | None = None # поле необязательно
    lastName: str | None = None # поле необязательно
    firstName: str | None = None # поле необязательно
    middleName: str | None = None # поле необязательно


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def get_user_me_api(self) -> Response:
        """
        Метод получения информации о текущем пользователе
        :return: ответ от сервера в виде httpx.Response
        """
        return self.get("/api/v1/users/me")

    def get_get_user_api(self, user_id: str) -> Response:
        """
        Метод получения информации о пользователе по его идентификатору
        :param user_id: идентификатор пользователя
        :return: ответ от сервера в виде httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Метод изменения информации о пользователе по его идентификатору
        :param user_id: идентификатор пользователя
        :param request: словарь, содержащий email, lastName, firstName, middleName
        :return: ответ от сервера в виде httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по его идентификатору
        :param user_id: идентификатор пользователя
        :return: ответ от сервера в виде httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")
