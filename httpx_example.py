from tkinter.scrolledtext import example

import  httpx


# Отправка GET-запроса
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code, "\n", response.json())


#Отправка POST-запроса
data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

post_response = httpx.post("https://jsonplaceholder.typicode.com/todo", json=data)

print(post_response.status_code, "\n", post_response.json())


# Отправка данных в application/x-www-form-urlencoded
data = {"username": "test_user", "password": "12345"}

response = httpx.post("https://httpbin.org/post", data=data)

print(response.json())


# Передача заголовков
headers = {"Authorization": "Bearer don't_show_my_token"}

response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.json()) # Заголовки включены в ответ

# Работа с параметрами запроса
params = {"userId": 1}

response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.url)
print(response.json())

# Отправка файлов
files = {"file": {"example.txt", open("example.txt", "rb")}}
response = httpx.post("https://httpbin.org/post", files=files)

print(response.json())  # Ответ с данными о загруженном файле

# Работа с сессиями (httpx.Client)
with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())  # Данные первой задачи
print(response2.json())  # Данные второй задачи

# Добавление базовых заголовков в Client


client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})

response = client.get("https://httpbin.org/get")

print(response.json())  # Заголовки включены в ответ
client.close()


# Работа с ошибками. Проверка статуса ответа (raise_for_status)
try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()  # Вызовет исключение при 4xx/5xx
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")


# Работа с ошибками. Обработка таймаутов
try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")