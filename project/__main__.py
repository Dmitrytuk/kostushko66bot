import asyncio
from dotenv import load_dotenv
from os import getenv
from pyrogram import Client, filters

import logging


load_dotenv()

api_id = getenv('api_id')
api_hash = getenv('api_hash')
bot_token = getenv('bot_token')

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

TARGET = -4142900821
# OCC gooup
#TARGET = -1818883697

MESSAGE = "{}, Welcome to group!"

@app.on_message(filters.chat(TARGET) & filters.new_chat_members)
async def welcome(client, message):
    new_members = [u.mention for u in message.new_chat_members]
    text = MESSAGE.format(",".join(new_members))
    print(message)
    await app.send_message(TARGET,
                              text,
                              disable_web_page_preview=True,
                              disable_notification=True)


logging.basicConfig(
    filename="warnings.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    try:
        app.run()
    except:
        import traceback

        logger.warning(traceback.format_exc())



