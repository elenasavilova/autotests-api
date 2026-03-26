from clients.api_client import APIClient
from httpx import Response
from clients.public_http_builder import get_public_http_client
from clients.authentification.authentication_schema import LoginRequestSchema, RefreshRequestSchema, LoginResponseSchema


class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "api/v1/authentication/login",
            json=request.model_dump(by_alias=True)
        )

    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "api/v1/authentication/refresh",
            json=request.model_dump(by_alias=True)
        )

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        """
        Метод возвращает токен
        :param request: словарь с email, password
        :return: ответ от сервера в виде LoginResponseDict (token: Token)
        """
        response = self.login_api(request)
        # return LoginResponseSchema(**response.json()) # выдаст ошибку, если вернется не Json
        return LoginResponseSchema.model_validate_json(response.text) # не выдаст ошибку, этот способ предпочтительнее

def get_authentication_client() -> AuthenticationClient:
    """
    Функция создает экземпляр класса AuthenticationClient с уже настроенным http-клиентом
    :return: готовый к использованию AuthenticationClient
    """
    return AuthenticationClient(client=get_public_http_client())


# Вариант с Typed Dict
# from typing import TypedDict


# class Token(TypedDict):
#     tokenType: str
#     accessToken: str
#     refreshToken: str
#
# class LoginRequestDict(TypedDict):
#     """
#     Описание структуры запроса на аутентификацию.
#     """
#     email: str
#     password: str
#
# class LoginResponseDict(TypedDict):
#     token: Token
#
# class RefreshRequestDict(TypedDict):
#     """
#     Описание структуры запроса для обновления токена.
#     """
#     refreshToken: str

# class AuthenticationClient(APIClient):
#     """
#     Клиент для работы с /api/v1/authentication
#     """
#     def login_api(self, request: LoginRequestDict) -> Response:
#         """
#         Метод выполняет аутентификацию пользователя.
#
#         :param request: Словарь с email и password.
#         :return: Ответ от сервера в виде объекта httpx.Response
#         """
#         return self.post("api/v1/authentication/login", json=request)
#
#     def refresh_api(self, request: RefreshRequestDict) -> Response:
#         """
#         Метод обновляет токен авторизации.
#
#         :param request: Словарь с refreshToken.
#         :return: Ответ от сервера в виде объекта httpx.Response
#         """
#         return self.post("api/v1/authentication/refresh", json=request)
#
#     def login(self, request: LoginRequestDict) -> LoginResponseDict:
#         """
#         Метод возвращает токен
#         :param request: словарь с email, password
#         :return: ответ от сервера в виде LoginResponseDict (token: Token)
#         """
#         response = self.login_api(request)
#         return response.json()
#
# def get_authentication_client() -> AuthenticationClient:
#     """
#     Функция создает экземпляр класса AuthenticationClient с уже настроенным http-клиентом
#     :return: готовый к использованию AuthenticationClient
#     """
#     return AuthenticationClient(client=get_public_http_client())
