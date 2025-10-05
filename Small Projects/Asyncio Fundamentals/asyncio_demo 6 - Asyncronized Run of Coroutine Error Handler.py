import asyncio


# await is use to await a coroutine and allow it to execute and get the result.
# you are only allowed to use await keyword inside an async function or coroutine

# creating a coroutine that simulates a time-consuming task
async def fetch_data(id, delay):
    print(f"Coroutine: {id} is now starting to fetch data...")
    await asyncio.sleep(delay) # Simulate I/O operation using sleep

    if id == 4:
        raise ValueError(f"Coroutine {id} encountered an error!")
    
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():

    tasks = []

    async with asyncio.TaskGroup() as tg:
        for index, get_delay in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(index, get_delay))
            tasks.append(task)

        # this is are just the same thing coded differently
        # tasks = [
        #     tg.create_task(fetch_data(1, 2)),
        #     tg.create_task(fetch_data(2, 1)),
        #     tg.create_task(fetch_data(3, 3)),
        # ]

    

    # Runs after the TaskGroup block. If all task are completed without error
    results = [task.result() for task in tasks]

    # Process result
    for result in results:
        print(f"Received result: {result}")

asyncio.run(main())