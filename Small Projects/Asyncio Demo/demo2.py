import asyncio
import api

async def kill_time(num):
    print(f"Running: {num}")
    await asyncio.sleep(1)
    print(f"Finished: {num}")


async def main():
    print("Started!")

    task_list = []

    for i in range (1, 1000 + 1):
        task_list.append(kill_time(i))

    await asyncio.sleep(2)

    # Demo 3: Synchronous Code Run with a thousand function running simultaneously
    await asyncio.gather(*task_list)
    print ("Done")

if __name__ == "__main__":
    asyncio.run(main())