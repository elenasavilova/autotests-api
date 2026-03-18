import asyncio
import websockets


async def client():
    """Реализация клиента, который устанавливает соединение с сервером, отправляет одно сообщение, получает и выводит в
    консоль 5 сообщений от сервера"""
    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"  # сообщение от клиента
        print(f"Отправка: {message}")
        await websocket.send(message)  # отправляем сообщение серверу

        for _ in range(5):
            response = await websocket.recv()  # получаем ответ от сервера
            print(response)


asyncio.run(client())
