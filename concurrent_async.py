import asyncio
import random
import httpx

# Simulate making an API call
async def handle_request(user_id: int):
    delay = random.uniform(0.5, 2.0)
    await asyncio.sleep(delay)  # simulates network wait
    print(f"User {user_id} request handled in {delay:.2f}s")

async def main():
    # Kick off 10 tasks concurrently
    tasks = [asyncio.create_task(handle_request(i)) for i in range(10)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
