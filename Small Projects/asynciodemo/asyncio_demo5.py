import asyncio


# await is use to await a coroutine and allow it to execute and get the result.
# you are only allowed to use await keyword inside an async function or coroutine

# creating a coroutine that simulates a time-consuming task
async def fetch_data(id, delay):
    print(f"Coroutine: {id} is now starting to fetch data...")
    await asyncio.sleep(delay) # Simulate I/O operation using sleep
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():

    # Run coroutines concurrently and gather their return values, returns a list
    results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 3))

    # Process result
    for result in results:
        print(f"Received result: {result}")

asyncio.run(main())