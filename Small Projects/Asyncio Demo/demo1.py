import asyncio
import api

async def send_data(to: str):
    
    print(f"Sending data to {to}...")
    await asyncio.sleep(2)
    print(f"Data sent to {to}")

async def main():
    data = await api.fetch_data()
    print(f"Data: {data}")

    # Demo 1: Test run of the function
    # await send_data("Mario") 
    
    # Demo 2: Synchronous Code Run with two function running simultaneously
    await asyncio.gather(send_data("Mario"), send_data("Luigi"))

if __name__ == "__main__":
    asyncio.run(main())