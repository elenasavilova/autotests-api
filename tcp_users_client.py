import socket

# Создание TCP-пакета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
server_address = ("localhost", 12345)
client_socket.connect(server_address)

# Отправляем сообщение на сервер
message = "Как дела?"
client_socket.send(message.encode())

# Получаем сообщение от сервера
response = client_socket.recv(1024).decode()
print(response)

# Закрываем соединение
client_socket.close()
