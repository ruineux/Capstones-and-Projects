import asyncio

async def fetch_data() -> str:
    print("Fetching Data...")
    await asyncio.sleep(2.5) # Similates wait time of an API
    print("Data Fetched!")

    return "API Data"