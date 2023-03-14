from Sniper import listener
import asyncio

checker = listener()

async def lol():
    while True:
        try:
            await checker.check("Keekd_up")
        except Exception:
            pass

asyncio.run(lol())