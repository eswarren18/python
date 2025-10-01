import asyncio
import random

counter = 0  # shared state

async def increment(user_id):
    global counter
    temp = counter
    delay = random.uniform(0.5, 2.0)
    await asyncio.sleep(delay)  # pretend we're waiting on I/O
    counter = temp + 1
    print(f"User {user_id} incremented counter to {counter}")

async def main():
    tasks = [asyncio.create_task(increment(i)) for i in range(5)]
    await asyncio.gather(*tasks)
    print("Final counter:", counter)

asyncio.run(main())
