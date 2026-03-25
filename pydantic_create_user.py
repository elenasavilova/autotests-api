from pydantic import BaseModel, Field, EmailStr

# Модель данных пользователя
class UserSchema(BaseModel):
    """
    Описание структуры данных пользователя
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

# Модель запроса на создание пользователя
class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры данных запроса на создание пользователя
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

# Модель ответа при создании пользователя
"""
Описание структуры данных ответа при создании пользователя
"""
class CreateUserResponseSchema(BaseModel):
    user: UserSchema


