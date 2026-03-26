from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema
from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


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

    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получения информации о пользователе по его идентификатору
        :param user_id: идентификатор пользователя
        :return: ответ от сервера в виде httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод изменения информации о пользователе по его идентификатору
        :param user_id: идентификатор пользователя
        :param request: словарь, содержащий email, lastName, firstName, middleName
        :return: ответ от сервера в виде httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True))

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по его идентификатору
        :param user_id: идентификатор пользователя
        :return: ответ от сервера в виде httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Метод, инициализирующий получение данных пользователя
        :param user_id: идентификатор пользователя
        :return: ответ от сервера в формате GetUserResponseSchema
        """
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Функция создает экземпляр класса PrivateUsersClient с уже настроенным httpx клиентом
    :return: готовый к использованию PrivateUsersClient
    """
    return PrivateUsersClient(client=get_private_http_client(user))

# _______________________________________________________________________________________________________________________
# Вариант с TypedDict
# from httpx import Response
# from clients.api_client import APIClient
# from typing import TypedDict
#
# from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
#
# class User(TypedDict):
#     """
#     Описание структуры данных пользователя
#     """
#     id: str
#     email: str
#     lastName: str
#     firstName: str
#     middleName: str
#
# class GetUserResponseDict(TypedDict):
#     """
#     Описание структуры ответа получения пользователя
#     """
#     user: User
#
# class UpdateUserRequestDict(TypedDict):
#     """
#     Описание структуры запроса на частичное изменение информации о пользователе
#     """
#     email: str | None = None # поле необязательно
#     lastName: str | None = None # поле необязательно
#     firstName: str | None = None # поле необязательно
#     middleName: str | None = None # поле необязательно
#
#
# class PrivateUsersClient(APIClient):
#     """
#     Клиент для работы с /api/v1/users
#     """
#     def get_user_me_api(self) -> Response:
#         """
#         Метод получения информации о текущем пользователе
#         :return: ответ от сервера в виде httpx.Response
#         """
#         return self.get("/api/v1/users/me")
#
#     def get_user_api(self, user_id: str) -> Response:
#         """
#         Метод получения информации о пользователе по его идентификатору
#         :param user_id: идентификатор пользователя
#         :return: ответ от сервера в виде httpx.Response
#         """
#         return self.get(f"/api/v1/users/{user_id}")
#
#     def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
#         """
#         Метод изменения информации о пользователе по его идентификатору
#         :param user_id: идентификатор пользователя
#         :param request: словарь, содержащий email, lastName, firstName, middleName
#         :return: ответ от сервера в виде httpx.Response
#         """
#         return self.patch(f"/api/v1/users/{user_id}", json=request)
#
#     def delete_user_api(self, user_id: str) -> Response:
#         """
#         Метод удаления пользователя по его идентификатору
#         :param user_id: идентификатор пользователя
#         :return: ответ от сервера в виде httpx.Response
#         """
#         return self.delete(f"/api/v1/users/{user_id}")
#
#     def get_user(self, user_id: str) -> GetUserResponseDict:
#         """
#         Метод, инициализирующий получение данных пользователя
#         :param user_id: идентификатор пользователя
#         :return: ответ от сервера в формате GetUserResponseDict
#         """
#         response = self.get_user_api(user_id)
#         return response.json()
#
# def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
#     """
#     Функция создает экземпляр класса PrivateUsersClient с уже настроенным httpx клиентом
#     :return: готовый к использованию PrivateUsersClient
#     """
#     return PrivateUsersClient(client=get_private_http_client(user))
