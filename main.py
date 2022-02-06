from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.types import CallbackQuery
import random
import os

PHOTO_LINK = [
 "https://telegra.ph/file/517bdca1f232bc8f7de28.jpg",
 "https://telegra.ph/file/5025089cc3a6ee4a3b15e.jpg"
 ]

Muhammed=Client(
    "Pyrogram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)


@Muhammed.on_message(filters.command("start")) 
async def start_message(bot, message):
    button = [[
      InlineKeyboardButton("Mo Tech YT", callback_data="start")
      ]]
    await messages.reply_photo(
        photo=random.choice(PHOTO_LINK),
        text="Hello {message.from_user.mention}   Bro Sugamano",
        reply_markup=InlineKeyboardMarkup(buttons)
    )



@Muhammed.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "start":
        await msg.message.edit(
            text=f" hello {msg.from_user.mention}  Start Text"
        )


Muhammed.run()

