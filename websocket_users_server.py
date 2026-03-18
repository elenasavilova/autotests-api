import asyncio
import websockets


async def echo(websocket):
    """Создаем сервер, принимающий web-socket подключения от клиентов, получающий и логирующий сообщения от клиентов,
    отправляющий клиенту пять ответных сообщений"""
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")

        for i in range(1, 6):
            await websocket.send(f'{i} Сообщение пользователя: {message}')  # отправляем ответ


# Запуск Web-socket сервера
async def start_server():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()


asyncio.run(start_server())
