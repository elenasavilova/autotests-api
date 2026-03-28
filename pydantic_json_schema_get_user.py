from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema(
  email=get_random_email(),
  password="string",
  last_name="string",
  first_name="string",
  middle_name="string"
)
# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user_api(create_user_request)
print('Create user data:', create_user_response)

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

# Инициализируем клиент PrivateUsersClient
private_users_client = get_private_users_client(authentication_user)

# Отправляем GET запрос на получение данных о созданном пользователе
get_user_response = private_users_client.get_user_api(user_id=create_user_response.user.id)
get_user_response_json = get_user_response.json()

# Валидация json-схемы
get_user_schema = GetUserResponseSchema.model_json_schema()
validate_json_schema(instance=get_user_response_json, schema=get_user_schema)
print('Get user data:', get_user_response)