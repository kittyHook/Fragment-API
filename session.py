import asyncio
from pyrogram import Client

api_id = 123
api_hash = ""


async def main():
    async with Client("stars", api_id, api_hash) as app:
        await app.send_message("me", "AutoGifts Deployed [!]")


asyncio.run(main())