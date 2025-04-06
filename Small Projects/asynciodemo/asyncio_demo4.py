import asyncio


# await is use to await a coroutine and allow it to execute and get the result.
# you are only allowed to use await keyword inside an async function or coroutine

# creating a coroutine that simulates a time-consuming task
async def fetch_data(id, delay):
    print(f"Coroutine: {id} is now starting to fetch data...")
    await asyncio.sleep(delay) # Simulate I/O operation using sleep
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():

    # Create task for running coroutines concurrently
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))

    result1 = await task1
    result2 = await task2

    task3 = asyncio.create_task(fetch_data(3, 1))
    task4 = asyncio.create_task(fetch_data(4, 4))

    result3 = await task3
    result4 = await task4

    print(result1, result2, result3, result4)

asyncio.run(main())