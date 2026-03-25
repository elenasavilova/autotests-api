from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel
import uuid

"""
BaseModel — это базовый класс, от которого наследуются все модели Pydantic.
Он предоставляет встроенную валидацию данных, сериализацию и десериализацию.
 
Атрибуты модели (id, title, maxScore, minScore, description, estimatedTime) соответствуют ключам JSON-объекта 
и имеют строго заданные типы 

Автоматическая валидация: если переданный в CourseSchema объект не соответствует ожидаемым типам,
Pydantic автоматически выбросит ошибку.
"""

class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl # HttpUrl — проверяет, что строка содержит корректный URL.

class UserSchema(BaseModel):
    id: str
    email: EmailStr # EmailStr — проверяет, является ли строка корректным email-адресом.
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    @computed_field
    def username(self) -> str:
        return f"{self.first_name} {self.last_name}"
    """
    Использование методов в Pydantic-модели – хотя Pydantic в основном используется для валидации и сериализации данных,
    мы можем добавлять методы для удобного представления или обработки данных.
    Метод get_username – возвращает строку с полным именем пользователя, объединяя first_name и last_name.
    Использование аннотации типов – метод возвращает str, что делает код более читаемым.
    """
    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"

class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True) # все поля в camelCase будут в snake_case
    # используем только тогда, когда уверены, что все поля в апи только в camelCase будут всегда
    # Иногда значения по умолчанию должны быть уникальными или вычисляться в момент создания объекта.
    #  Для этого используется default_factory. default=...	Когда значение фиксированное.
    id: str = Field(default_factory=lambda: str(uuid.uuid4())) # lambda генерирует гуид 4ой версии и превращает его
    # в строку
    title:str = "default" # значение по-умолчанию
    # max_score: int
    # min_score: int
    max_score: int = Field(alias="maxScore", default=1000) # значение по-умолчанию
    min_score: int = Field(alias="minScore", default=10) # значение по-умолчанию
    description: str = "default" # значение по-умолчанию
    preview_file: FileSchema = Field(alias='previewFile')
    # estimated_time: str
    estimated_time: str = Field(alias="estimatedTime", default="default time") # значение по-умолчанию
    created_by_user: UserSchema = Field(alias="createdByUser")

# Инициализация модели

# 1. Стандартный способ - передача аргументов при создании объекта, как в обычном Python-классе. Используется, если
# данные заданы явно.
course_default_model = CourseSchema(
    id="course_id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright course",
    previewFile=FileSchema(
        id="file_id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses"
    ),
    estimatedTime="2 weeks",
    createdByUser=UserSchema(
        id="user-id",
        email="user@gmail.com",
        lastName="Savilova",
        firstName="Lena",
        middleName="Aleksandra"
    )
)
print("Course default model:", course_default_model)

# 2. Инициализация с использованием словаря - используем **course_dict для распаковки словаря, передавая его содержимое
# в модель.
# Этот метод удобен, когда у нас уже есть данные в виде словаря, например, полученные из JSON-ответа API.

course_dict = {
    "id": "course_id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright course",
    "previewFile": {
        "id": "file_id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "2 weeks",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Savilova",
        "firstName": "Lena",
        "middleName": "Aleksandra"
        }
}
course_dict_model = CourseSchema(**course_dict) # через распаковку словаря
print("Course dict model:", course_dict_model)


# 3. Инициализация с использованием JSON - используем метод model_validate_json, который парсит строку и создает объект
# CourseSchema. Способ удобен, когда данные хранятся в файле или приходят от API.
course_json = """
{
    "id": "course_id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright course",
    "previewFile": {
        "id": "file_id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "2 weeks",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Savilova",
        "firstName": "Lena",
        "middleName": "Aleksandra"
        }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json) # pydantic парсит json и перекладывает в модель
print("Course json model:", course_json_model)

# Обратная конвертация (из модели в JSON)
# Сериализация
"""
Когда мы сериализуем Pydantic-модель обратно в JSON (dict() или json()), Pydantic по умолчанию сохраняет 
Python-стиль именования (snake_case).
                
Но если нам нужно вернуть JSON в camelCase, то можно использовать by_alias=True
"""
print(course_json_model.model_dump(by_alias=True)) # поля будут в том формате, в котором они указаны в alias
# (в нашем случае в camel case)
print(course_json_model.model_dump_json())

# Дефолтные значения - если задаем значения в схеме, при инициализации без указания конкретных значений,
# будут использоваться значения по-умолчанию. Если передаем новое значение, используется новое (т.е. оно приоритетнее)
# course_default = CourseSchema()
# print(course_default)

# id='course-id' title='default' max_score=1000 min_score=10 description='default' estimated_time='default time'

user = UserSchema(
        id="user-id",
        email="user@gmail.com",
        lastName="Savilova",
        firstName="Lena",
        middleName="Aleksandra"
)
print(user.get_username())
print(user.username)

try:
    user = UserSchema(
        id="user-id",
        email="usergmail.com",
        lastName="Savilova",
        firstName="Lena",
        middleName="Aleksandra"
    )
except ValidationError as error:
    print(error) # error содержит текст ошибки с пояснением.
    print(error.errors()) # error.errors() возвращает список словарей с подробной информацией об ошибке, например:

# loc — указывает, в каком поле произошла ошибка (url).
# msg — объясняет, в чем проблема.
# type — тип ошибки (url_parsing).
# input — проблемное значение (localhost).

"""
                        ФИНАЛЬНЫЙ СКРИПТ
"""

# Добавили модель FileSchema
class FileSchema(BaseModel):
    id: str
    url: HttpUrl  # Используем HttpUrl вместо str
    filename: str
    directory: str


# Добавили модель UserSchema
class UserSchema(BaseModel):
    id: str
    email: EmailStr  # Используем EmailStr вместо str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CourseSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    # Вложенный объект для файла-превью
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    # Вложенный объект для пользователя, создавшего курс
    created_by_user: UserSchema = Field(alias="createdByUser")


# Инициализируем модель CourseSchema через передачу аргументов
course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    # Добавили инициализацию вложенной модели FileSchema
    previewFile=FileSchema(
        id="file-id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses",
    ),
    estimatedTime="1 week",
    # Добавили инициализацию вложенной модели UserSchema
    createdByUser=UserSchema(
        id="user-id",
        email="user@gmail.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alise"
    )
)
print('Course default model:', course_default_model)

# Инициализируем модель CourseSchema через распаковку словаря
course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    # Добавили ключ previewFile
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    # Добавили ключ createdByUser
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)
print(course_dict_model.model_dump())
print(course_dict_model.model_dump(by_alias=True))

# Инициализируем модель CourseSchema через JSON
course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print('Course JSON model:', course_json_model)

# Инициализируем FileSchema c некорректным url
try:
    file = FileSchema(
        id="file-id",
        url="localhost",
        filename="file.png",
        directory="courses",
    )
except ValidationError as error:
    print(error)
    print(error.errors())
