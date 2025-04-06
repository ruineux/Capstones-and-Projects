import asyncio


# await is use to await a coroutine and allow it to execute and get the result.
# you are only allowed to use await keyword inside an async function or coroutine

# creating a coroutine that simulates a time-consuming task
async def fetch_data(delay):
    print("Fetching Data...")
    await asyncio.sleep(delay) # Simulate I/O operation using sleep
    print("Data Fetched")
    return {"data": "Some data"}

# define another coroutine that calls the first coroutine
async def main():
    print("Start of main coroutine")
    
    # we assign a variable for the coroutine object to trigger but it will not display the result until you awaited
    task = fetch_data(3) 

    # wait for the fetch_data coroutine, pausing the execution of main until fetch_data completes
    result = await task
    print(f"Received result: {result}")
    print("End of main coroutine")

asyncio.run(main())
