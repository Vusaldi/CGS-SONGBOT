import os
import os
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from CGS import CGS as app
from CGS.__main__ import START_TEXT, HELP_TEXT, btn, btns

START_TEXT = """
**HELLO [{}](tg://user?id={}) 
I'M CGS SONG DOWNLOAD BOT**
You can download song me a very fast ⚡
Commands view to send /help or help button.
"""
HELP_TEXT = """
**Heya [{}](tg://user?id={}) Command list By CGSSONGBOT**
✪ /song - send you want download song name
✪ /saavn - send you want download saavn name
✪ /lyric - send you want see lyric name
✪ /video - send you want download video nam
Thanks 🍀
"""

   
    
    
# Call backs @CGSUPDATES 

@app.on_callback_query()
async def cb_data(client, message):
    if message.data == "help":
        await message.message.edit_text(
            text=HELP_TEXT.format(message.from_user.mention),
            reply_markup=btn,
            disable_web_page_preview=True,
        )
    elif message.data == "helpback":
        await message.message.edit_text(
            text=START_TEXT.format(message.from_user.mention),
            reply_markup=btns,
            disable_web_page_preview=True
        )
