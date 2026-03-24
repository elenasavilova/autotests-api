from httpx import Client, URL, QueryParams, Response
from typing import Any
from httpx._types import RequestData, RequestFiles


class APIClient:
    """
        Базовый API клиент, принимающий объект httpx.Client.

        :param client: экземпляр httpx.Client для выполнения HTTP-запросов
    """
    def __init__(self, client:Client):
        self.client = client


    """
    Выполняет GET-запрос.

    :param url: URL-адрес эндпоинта.
    :param params: GET-параметры запроса (например, ?key=value).
    :return: Объект Response с данными ответа.
    """
    def get(
            self,
            url: URL | str,
            params: QueryParams | None = None
    ) -> Response:
       return self.client.get(url, params=params)


    """
    Выполняет POST-запрос.

    :param url: URL-адрес эндпоинта.
    :param json: Данные в формате JSON.
    :param data: Форматированные данные формы (например, application/x-www-form-urlencoded).
    :param files: Файлы для загрузки на сервер.
    :return: Объект Response с данными ответа.
    """
    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        return self.client.post(url, json=json, data=data, files=files)


    """
    Выполняет PATCH-запрос (частичное обновление данных).

    :param url: URL-адрес эндпоинта.
    :param json: Данные для обновления в формате JSON.
    :return: Объект Response с данными ответа.
    """
    def patch(
            self,
            url: URL | str,
            json: Any | None = None
    ) -> Response:
        return self.client.patch(url, json=json)


    """
    Выполняет DELETE-запрос (удаление данных).

    :param url: URL-адрес эндпоинта.
    :return: Объект Response с данными ответа.
    """
    def delete(self, url: URL | str) -> Response:
        return self.client.delete(url)