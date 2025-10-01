import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# Mock function: simulates handling a request
def handle_request(user_id: int) -> str:
    # Simulate network delay (0.5 to 2 seconds)
    delay = random.uniform(0.5, 2.0)
    time.sleep(delay)
    return f"User {user_id} request handled in {delay:.2f}s"

def main():
    num_users = 10   # simulate 10 concurrent users
    max_threads = 5  # size of our thread pool

    print(f"Simulating {num_users} concurrent users with {max_threads} threads...\n")

    # Thread pool
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        # Submit all tasks
        futures = [executor.submit(handle_request, i) for i in range(num_users)]

        # Collect results as they complete
        for future in as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    main()
