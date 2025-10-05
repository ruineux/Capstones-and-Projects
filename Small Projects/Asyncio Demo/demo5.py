import asyncio
import api


async def main():

    # Demo 5: Making sure things are done
    task = asyncio.create_task(
        api.fetch_data()
    )
    
    
    try:
        # It will time out since we set in api.py to wait for 2.5 secs
        await asyncio.wait_for(task, timeout=2)
    except asyncio.CancelledError:
        print("CANCELLED: Request was cancelled")
    except asyncio.TimeoutError:
        print("TIMEOUT: Request took too long")

if __name__ == "__main__":
    asyncio.run(main())