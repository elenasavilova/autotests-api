from pydantic import BaseModel, Field, EmailStr, ConfigDict
from tools.fakers import fake


class UserSchema(BaseModel):
    """
    Описание структуры пользователя
    """
    model_config = ConfigDict(populate_by_name=True) # дает возможность заполнять модель по алиас и по названию поля
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа получения пользователя
    """
    model_config = ConfigDict(populate_by_name=True)
    user: UserSchema


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса создания пользователя
    """
    model_config = ConfigDict(populate_by_name=True)
    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя
    """
    model_config = ConfigDict(populate_by_name=True)
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на частичное изменение информации о пользователе
    """
    model_config = ConfigDict(populate_by_name=True)
    email: EmailStr | None = Field(default_factory=fake.email) # поле необязательно
    last_name: str | None = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str | None = Field(alias="middleName", default_factory=fake.middle_name)


class UpdateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления пользователя
    """
    model_config = ConfigDict(populate_by_name=True)
    user: UserSchema
