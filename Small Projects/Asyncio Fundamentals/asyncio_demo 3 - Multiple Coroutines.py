import asyncio


# await is use to await a coroutine and allow it to execute and get the result.
# you are only allowed to use await keyword inside an async function or coroutine

# creating a coroutine that simulates a time-consuming task
async def fetch_data(delay, id):
    print(f"Fetching Data... id: {id}")
    await asyncio.sleep(delay) # Simulate I/O operation using sleep
    print(f"Data Fetched for id: {id}")
    return {"data": "Some data", "id": id}

# define another coroutine that calls the first coroutine
async def main():
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)

    result1 = await task1
    print(f"Received result: {result1}")

    result2 = await task2
    print(f"Received result: {result2}")

asyncio.run(main())
