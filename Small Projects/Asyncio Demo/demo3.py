import asyncio
import api


async def main():

    # Demo 4: Creating a task, this is beneficial in a way you can control
    # how things are turning out
    task = asyncio.create_task(
        api.fetch_data()
    )
    
    
    try:
        result = await task
    except:
        pass

if __name__ == "__main__":
    asyncio.run(main())