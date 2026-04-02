from http import HTTPStatus
from clients.authentification.authentication_client import get_authentication_client
from clients.authentification.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
import pytest


@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    # Инициализируем API-клиент для работы с пользователями
    public_users_client = get_public_users_client()
    # Формируем тело запроса для создания пользователя
    create_user_request = CreateUserRequestSchema()
    # Отправляем запрос для создания пользователя
    public_users_client.create_user(create_user_request)
    # Инициализируем API-клиент для аутентификации пользователя
    authentication_client = get_authentication_client()
    # Формируем тело запроса для аутентификации пользователя
    login_request = LoginRequestSchema(email=create_user_request.email, password=create_user_request.password)
    # Отправляем запрос аутентификации пользователя
    login_response = authentication_client.login_api(login_request)
    # Инициализируем модель ответа на основе полученного JSON в ответе
    # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)
    # Проверяем статус-код ответа
    assert_status_code(login_response.status_code, HTTPStatus.OK)
    # Проверяем, что данные ответа совпадают с данными запроса
    assert_login_response(login_response_data)
    # Выполняем валидацию JSON-схемы
    validate_json_schema(login_response.json(), login_response_data.model_json_schema())

