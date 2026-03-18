import grpc

import user_service_pb2
import user_service_pb2_grpc

# Устанавливаем соединение с сервером
"""
Этот код выполняет следующие действия:

Создает gRPC-канал

grpc.insecure_channel('localhost:50051') создает соединение с сервером, который работает на локальном хосте (localhost)
 и порту 50051.
insecure_channel означает незащищенное соединение без шифрования (TLS). Это удобно для локального тестирования.
Создает gRPC-клиента

UserServiceStub(channel) — это специальный клиентский объект, который используется для отправки запросов gRPC-серверу.
stub — это "заглушка" (stub), через которую клиент взаимодействует с сервером.
"""
channel = grpc.insecure_channel('localhost:50051')
stub = user_service_pb2_grpc.UserServiceStub(channel)

# Отправляем запрос
"""
Здесь клиент выполняет следующие шаги:
Создает gRPC-запрос

user_service_pb2.GetUserRequest(username="Lena") создает объект запроса, который содержит поле username="Lena".
Этот объект соответствует message GetUserRequest { string username = 1; } в user_service.proto.
Отправляет запрос серверу

stub.GetUser(...) вызывает метод GetUser на сервере через gRPC.
Клиент ожидает ответа, который будет объектом GetUserResponse.
Получает и выводит ответ

response.message содержит строку, полученную от сервера.
Если сервер работает, в консоли появится:
Привет, Lena!
"""
response = stub.GetUser(user_service_pb2.GetUserRequest(username='Lena')) #
print(response.message)