import asyncio
import random

counter = 0
lock = asyncio.Lock()

async def increment(user_id):
    global counter
    async with lock:  # only one task can enter at a time
        temp = counter
        delay = random.uniform(0.5, 2.0)
        await asyncio.sleep(delay)
        counter = temp + 1
        print(f"User {user_id} incremented counter to {counter} in {delay:.2f}s")

async def main():
    tasks = [asyncio.create_task(increment(i)) for i in range(5)]
    await asyncio.gather(*tasks)
    print("Final counter:", counter)

asyncio.run(main())
