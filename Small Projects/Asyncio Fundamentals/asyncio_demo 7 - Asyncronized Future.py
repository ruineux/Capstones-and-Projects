import asyncio

async def set_future_result(future, future_value, delay):
    print("Simulating a delay before setting result...")
    await asyncio.sleep(2)  # Simulate an asynchronous operation
    future.set_result(future_value)
    print("Result has been set.")

async def main():

    # Create an asyncio Future object
    future = asyncio.Future()

    # Simulate setting the result in an asynchronous operation
    asyncio.create_task(set_future_result(future, "Future result has been set!", 5))

    # Check is future value is done
    print(f"Future done? {future.done()}")

    print("Waiting for the future result...")
    result = await future  # Wait for the result to be set
    print(f"Received result: {result}")

    print(f"Future done? {future.done()}")

asyncio.run(main())