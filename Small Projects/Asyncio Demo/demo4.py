import asyncio
import api


async def main():

    # Demo 5: Controlling the result of the task
    task = asyncio.create_task(
        api.fetch_data()
    )
    
    # In case you want to cancel the task
    # task.cancel()
    # if task.cancelled():
    #    print(tas.cancelled())
    
    try:
        if task.done():
            result = await task
            print(result)
    except asyncio.CancelledError:
        print("CANCELLED: Request was cancelled")
    except asyncio.TimeoutError:
        print("TIMEOUT: Request took too long")

if __name__ == "__main__":
    asyncio.run(main())