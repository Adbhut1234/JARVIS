from mem0 import AsyncMemoryClient
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    mem0 = AsyncMemoryClient()
    try:
        results = await mem0.get_all(filters={'user_id': 'Adi'})
        print(f"TYPE: {type(results)}")
        print(f"RESULTS: {results}")
    except Exception as e:
        print(f"ERROR: {e}")

asyncio.run(main())
