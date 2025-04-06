import asyncio

# Simulate shared resource
shared_resource = 0

# Create an asyncio lock object
lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    async with lock:
        print("Critical Section Starts")
        print(f"Resource before modification: {shared_resource}")
        shared_resource += 1
        await asyncio.sleep(2)
        print(f"Resource after modification: {shared_resource}")
        print("Critical Section Ends")


async def main():

    await asyncio.gather(*(modify_shared_resource() for v in range(5))) # Asterisk denotes unpacking a generate which is in this example, range

    # Alternatively, it is similar to this one
    # await asyncio.gather(
    #     modify_shared_resource(),
    #     modify_shared_resource(),
    #     modify_shared_resource(),
    #     modify_shared_resource(),
    #     modify_shared_resource()
    # )

    

asyncio.run(main())