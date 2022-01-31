import os

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from CGS.plug import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from CGS import CGS
from CGS import LOGGER

   START_TEXT = """
HELLO I'M CGS SONG DOWNLOAD BOT
You can download song me a very fast ⚡
Commands view to send /help or help button.
"""
   HELP_TEXT = """
*Command list By CGSSONGBOT*
/song - send you want download song name
/saavn - send you want download saavn name
/lyric - send you want see lyric name
/video - send you want download video name
Thanks users 🍀
"""

@CGS.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        BUTTONS = [
    [
        InlineKeyboardButton("Help 🆘", callback_data="help")
    ],
    [    InlineKeyboardButton("UPDATES 📢", url="https://t.me/CGSUPDATES"),
        InlineKeyboardButton("SUPPORT 💬", url="https://t.me/CGSsupport")
    ],
]    
    else:
        BUTTONS = None
    await message.reply_text(
                    reply_markup=InlineKeyboardMarkup(BUTTONS),
                    caption=START_TEXT.format(name, user_id))

# help

@CGS.on_message(filters.command("help"))
async def help(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        BUTTONSA = [
    [
        InlineKeyboardButton("BACK 🍀", callback_data="help_back")
    ],
]    
    else:
        BUTTONS = None
    await message.reply_text(
                    reply_markup=InlineKeyboardMarkup(BUTTONSA),
                    caption=HELP_TEXT.format(name, user_id))



CGS.start()
LOGGER.info("CGS PROJECT WORKING✅✔️")
idle()
