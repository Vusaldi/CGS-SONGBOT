import os
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from CGS import CGS as app


class exe(object):

    START_TEXT = """
**Hi,👋 {} 😀
    I'm Wrld Music** 🍀
    
You can download song me a very fast ⚡

Commands view to send /help or help button.
"""
    HELP_TEXT = """
**Heya {} 🍀
      Command list By Wrld Music** 🗣

✪ /song - send you want download song name
✪ /saavn - send you want download saavn name
✪ /lyric - send you want see lyric name
✪ /video - send you want download video name

Thanks 🍀
"""
    btn = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("🆘️ Help 🆘", callback_data="help")
        ],[
        InlineKeyboardButton("UPDATES 📢", url="https://t.me/WrldMusicUptadesChannel"),
        InlineKeyboardButton("Batlle Group 💬", url="https://t.me/battlemuzakire")
        ]]
    )
    btns = InlineKeyboardMarkup( 
        [[
        InlineKeyboardButton(text="Back 🍀", callback_data="helpback")
        ]]    
    )
