import os, asyncio
from pyrogram import Client, compose

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
bot_tokens = [token for token in os.environ.get("BOT_TOKEN")]


async def send_reply(c, m):
    await m.reply_text("**Hey I am Back 😘\n\nPermanent shifted to 👉: @UploadXPro_Bot**", quote=True)

async def main():
    apps = []
    i = 0
    for token in bot_tokens:
        i += 1
        x = Client(f"account{i}", bot_token=token, api_id=API_ID, api_hash=API_HASH)
        x.add_handler(MessageHandler(send_reply))
        apps.append(x)
    
    await compose(apps)


if __name__ == '__main__':
    asyncio.run(main())
