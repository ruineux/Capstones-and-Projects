import asyncio

async def waiter(event):
    print("Waiting for the event to be set")
    await event.wait()
    print("Waiting is over! Running some other codes now")

async def setter(event):
    await asyncio.sleep(2)
    event.set()
    print("Event has been set!")

async def main():

    # Create an asyncio event object
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))

asyncio.run(main())