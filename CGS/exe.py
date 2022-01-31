import os
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from CGS import CGS as app


class exe(object):

    START_TEXT = """
**HELLO {} 😀
    I'M CGS SONG DOWNLOAD BOT** 🍀
    
You can download song me a very fast ⚡

Commands view to send /help or help button.
"""
    HELP_TEXT = """
**Heya {} 🍀
      Command list By CGSSONGBOT**

✪ /song - send you want download song name
✪ /saavn - send you want download saavn name
✪ /lyric - send you want see lyric name
✪ /video - send you want download video name

Thanks {}🍀
"""
    btn = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("🆘️ Help 🆘", callback_data="help")
        ],[
        InlineKeyboardButton("UPDATES 📢", url="https://t.me/CGSUPDATES"),
        InlineKeyboardButton("SUPPORT 💬", url="https://t.me/CGSsupport")
        ]]
    )
    btns = InlineKeyboardMarkup( 
        [[
        InlineKeyboardButton(text="Back 🍀", callback_data="helpback")
        ]]    
    )
