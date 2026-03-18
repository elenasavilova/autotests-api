import asyncio

import websockets


# Обработчик входящих сообщений
async def echo(websocket):
    print("Клиент подключился")
    async for message in websocket:
        print(f"Получено сообщение: {message}")
        response = f"Сервер получил: {message}"

        for _ in range(5):
            await websocket.send(response)  # Отправляем ответ


# Запуск WebSocket-сервера на порту 8765
async def main():
    server = await websockets.serve(echo, "127.0.0.1", 8765)
    print("WebSocket сервер запущен на ws://127.0.0.1:8765")
    await server.wait_closed()


asyncio.run(main())
