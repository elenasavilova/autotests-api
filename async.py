import asyncio
import time


def fetch_data():
    print("Fetching data...")
    time.sleep(2)

# for _ in range(5): # используем  _ вместо, например, i, если не планируем использовать i дальше в цикле, т.е.
#     # обозначаем, что _ - переменная, но ее значение не важно, это принятый python паттерн
#     fetch_data()


async def fetch_data_async():
    print("Fetching data...")
    await asyncio.sleep(2)

loop = asyncio.new_event_loop()
tasks = {
    loop.create_task(fetch_data_async()),
    loop.create_task(fetch_data_async()),
    loop.create_task(fetch_data_async()),
    loop.create_task(fetch_data_async()),
    loop.create_task(fetch_data_async()),
}
loop.run_until_complete(asyncio.wait(tasks))
loop.close()