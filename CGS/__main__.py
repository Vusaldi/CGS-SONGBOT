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

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from CGS.plug import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from CGS import CGS as app
from CGS import LOGGER




@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(
                text="🆘️ Help 🆘️", callback_data="help")
            ],[
            InlineKeyboardButton(
                text="Updates 📢", url="https://t.me/cgsUpdates"),
            InlineKeyboardButton(
                text="Support 💬", url="https://t.me/cgsSupport")
            ],]
        )
    else:
        btn = None
    await message.reply_text(START_TEXT.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def help(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btns = InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(
                text="Back 🍀", callback_data="help_back")
            ],]
        )
    else:
        btns = None
    await message.reply_text(HELP_TEXT.format(name, user_id))


app.start()
LOGGER.info("CGSSongBot is online.")
idle()
