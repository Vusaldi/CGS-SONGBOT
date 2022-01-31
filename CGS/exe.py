import os
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from CGS import CGS as app


START_TEXT = """
**HELLO {}
I'M CGS SONG DOWNLOAD BOT**
You can download song me a very fast ⚡
Commands view to send /help or help button.
"""
HELP_TEXT = """
**Heya {} Command list By CGSSONGBOT**

✪ /song - send you want download song name
✪ /saavn - send you want download saavn name
✪ /lyric - send you want see lyric name
✪ /video - send you want download video nam
Thanks 🍀
"""
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
btns = InlineKeyboardMarkup(
           [[
           InlineKeyboardButton(
               text="Back 🍀", callback_data="help_back")
           ],]
       )
   
    
    
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
