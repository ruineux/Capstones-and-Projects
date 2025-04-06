import asyncio

# coroutine function
async def main():
    print("Start of main coroutine")

# using this method, main() becomes a coroutine object

# coroutine object should be passed on this way, otherwise calling main() will just tell you it is a coroutine object
asyncio.run(main())

# Running this will just print the object and allocated memory + RuntimeWarning: coroutine 'main' was never awaited
# print(main())
