import asyncio
from dotenv import load_dotenv
from os import getenv
from pyrogram import Client, filters
from pyrogram.types import BotCommand, ReplyKeyboardMarkup, ReplyKeyboardMarkup

load_dotenv()

api_id = getenv('api_id')
api_hash = getenv('api_hash')
bot_token = getenv('bot_token')

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
# app = Client("my_account", api_id=api_id, api_hash=api_hash)

# TARGET = -1001666747721
TARGET = -4142900821

MESSAGE = "{}, Whelcome to group!"

# @app.on_message()
# async def get_chat_id(client, message):
#     print(message)

# markup = ReplyKeyboardMarkup(
#     keyboard=[],
#     resize_keyboard=True,
#     mute=True
# )


@app.on_message(filters.chat(TARGET) & filters.new_chat_members)
async def welcome(client, message):
    new_members = [u.mention for u in message.new_chat_members]
    text = MESSAGE.format(",".join(new_members))
    print(message)
    await app.send_message(TARGET,
                              text,
                              disable_web_page_preview=True,
                              disable_notification=True)


# bot_commands = [
#         BotCommand("start", "Start the bot")
#         ]

# async def set_commands():
#     async with app:
#         await app.set_bot_commands(bot_commands)


app.run()

