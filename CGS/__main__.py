import os

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from CGS.plug import *
from pyrogram import idle, filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from CGS import CGS
from CGS import LOGGER

START_TEXT = """
**HELLO [{}](tg://user?id={}), I'M CGS SONG DOWNLOAD BOT**

You can download song me a very fast ⚡

Commands view to send /help or help button.
"""
HELP_TEXT = """
**Heya [{}](tg://user?id={}), Command list By CGSSONGBOT**

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
    await message.reply(START_TEXT.format(name, user_id), reply_markup=BUTTONS)
                 
# help

@CGS.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == "private":
        BUTTONSA = [
    [
        InlineKeyboardButton("BACK 🍀", callback_data="help_back")
    ],
]    
    else:
        BUTTONSA = None
    await message.reply(HELP_TEXT.format(name, user_id), reply_markup=BUTTONSA)


CGS.start()
LOGGER.info("CGS PROJECT WORKING✅✔️")
idle()
