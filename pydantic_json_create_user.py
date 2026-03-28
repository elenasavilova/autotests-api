from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email
import jsonschema

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
create_user_response_schema = CreateUserResponseSchema.model_json_schema()

jsonschema.validate(create_user_response.json(), schema=create_user_response_schema)
print('Create user data:', create_user_response)

validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)


# Пример
# from clients.authentification.authentication_schema import TokenSchema
#
# print(TokenSchema.model_json_schema())
#
# schema = {'description': 'Описание структуры аутентификационных токенов.',
#           'properties': {
#               'tokenType': {'title': 'Tokentype', 'type': 'string'},
#               'accessToken': {'title': 'Accesstoken', 'type': 'string'},
#               'refreshToken': {'title': 'Refreshtoken', 'type': 'string'}},
#           'required': ['tokenType', 'accessToken', 'refreshToken'],
#           'title': 'TokenSchema', 'type': 'object'
#           }