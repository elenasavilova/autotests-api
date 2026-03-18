from concurrent import futures  # Импорт пула потоков для асинхронного выполнения

import grpc  # Импорт библиотеки gRPC

import user_service_pb2  # Сгенерированные классы для работы с gRPC-сообщениями
import user_service_pb2_grpc  # Сгенерированный класс для работы с сервисом


# Реализация gRPC-сервиса
"""
Этот класс реализует gRPC-сервис UserService, который был определен в user_service.proto.

Наследование от UserServiceServicer

Класс UserServiceServicer унаследован от автоматически сгенерированного класса user_service_pb2_grpc.UserServiceServicer.
Это означает, что мы должны реализовать все методы, объявленные в .proto-файле.
Метод GetUser(self, request, context)

Получает объект запроса (GetUserRequest), который содержит username.
Логирует полученный запрос (print).
Формирует и возвращает ответ (GetUserResponse) с приветственным сообщением
"""
class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer):
    """Реализация методов gRPC-сервиса UserService"""

    def GetUser(self, request, context):
        """Метод GetUser обрабатывает входящий запрос"""
        print(f'Получен запрос к методу GetUser от пользователя: {request.username}')

        # Формируем и возвращаем ответное сообщение
        return user_service_pb2.GetUserResponse(message=f"Привет, {request.username}!")


# Функция для запуска gRPC-сервера
"""
Функция serve() выполняет несколько ключевых задач:

Создание gRPC-сервера

Использует grpc.server(), передавая ThreadPoolExecutor(max_workers=10), который позволяет обрабатывать до 10 
параллельных запросов.
Регистрация сервиса

Метод add_UserServiceServicer_to_server() связывает наш UserServiceServicer с сервером.
Настройка порта

Сервер будет слушать соединения на 50051 (стандартный порт для gRPC).
server.add_insecure_port('[::]:50051') означает, что сервер будет доступен по всем IP-адресам ([::] — это аналог 
0.0.0.0, но для IPv6).
Запуск сервера

server.start() запускает сервер в фоновом режиме.
Ожидание завершения работы

server.wait_for_termination() заставляет программу не завершаться, пока сервер не будет остановлен вручную.
"""
def serve():
    """Функция создает и запускает gRPC-сервер"""

    # Создаем сервер с использованием пула потоков (до 10 потоков)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Регистрируем сервис UserService на сервере
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)

    # Настраиваем сервер для прослушивания порта 50051
    server.add_insecure_port('[::]:50051')

    # Запускаем сервер
    server.start()
    print("gRPC сервер запущен на порту 50051...")

    # Ожидаем завершения работы сервера
    server.wait_for_termination()


# Запуск сервера при выполнении скрипта
"""
Этот блок кода выполняет serve() только если файл запущен напрямую (а не импортирован как модуль).
Это стандартный прием в Python, предотвращающий непреднамеренный запуск кода при импорте.
"""
if __name__ == "__main__":
    serve()