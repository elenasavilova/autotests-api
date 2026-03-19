import socket

# Создаем TCP-сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
server_address = ('localhost', 12345)
client_socket.connect(server_address) #  — устанавливаем TCP-соединение с сервером. Если сервер не запущен,
# клиент получит ошибку.

# Отправляем сообщение серверу
"""
message = "Привет, сервер!" — задаем текст сообщения.
.encode() — преобразует строку в байты, так как send() принимает только байты.
client_socket.send() — отправляет данные по TCP-соединению.
"""
message = "Привет, сервер!"
client_socket.send(message.encode())

# Получаем ответ от сервера
response = client_socket.recv(1024).decode()
print(f"Ответ от сервера: {response}")

# Закрываем соединение
client_socket.close()