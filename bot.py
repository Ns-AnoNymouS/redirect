

app = Client(
    
    api_id = int(os.environ.get("API_ID"))
    api_hash = os.environ.get("API_HASH")

)

import asyncio
from pyrogram import Client, compose

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_tokens = [token for token in os.environ.get("BOT_TOKEN")]


async def main():
    apps = []
    i = 0
    for token in bot_tokens:
        i += 1
        x = Client(f"account{i}", bot_token=token, api_id=API_ID, api_hash=API_HASH)
        apps.append(x)
    
    await compose(apps)


if __name__ == '__main__':
    asyncio.run(main())
