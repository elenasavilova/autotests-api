from pydantic import BaseModel, Field
"""
Pydantic — это библиотека для валидации данных и управления схемами данных в Python. Она позволяет определять строгие 
структуры данных с использованием аннотаций типов, автоматически проверяя их на соответствие заданным требованиям.

Организация кода с Pydantic:
1. Используйте суффикс Schema, чтобы избежать конфликтов.
2. Давайте понятные названия моделям, отражающие их смысл.
3. Разделяйте краткие и полные версии моделей (ShortUserSchema, ExtendedUserSchema).
4. Не привязывайтесь к API-методу в названии модели, используйте CreateUserRequestSchema, GetUserResponseSchema.
5. Разбивайте модели по файлам (courses_schema.py, users_schema.py).
6. Модели отвечают только за валидацию, а не за логику API-запросов.
7. Используйте наследование, чтобы избегать дублирования кода.
"""


class Address(BaseModel):
    city: str
    zip: str
class User(BaseModel):
    id: int
    name: str
    email: str
    # address: Address # Вложенная модель
    is_active: bool = Field(alias="isActive") # Значение по умолчанию


user_data = {
    "id": 1,
    "name": "Lena",
    "email": "Lena@gmail.com",
    "isActive": True
}
user = User(**user_data) # распаковка словаря

# user = User(id="123", name="Alice")
# print(user.id)  # 123 (автоматически преобразован в int)


#
# user = User(
#     id=1,
#     name="Lena",
#     email="Lena@gmail.com",
#     # address={"city": "Voronezh", "zip": "396836"}, - можно передать значения в виде словаря
#     address=Address(city="Voronezh", zip="396836") # или сразу через модель
# )
print(user.model_dump()) # из модели преобразуем в dict
print(user.model_dump_json()) # из модели преобразуем в json-строку