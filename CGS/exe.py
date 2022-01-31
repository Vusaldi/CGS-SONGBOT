import os
import os
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from CGS import CGS as app
from CGS.__main__ import START_TEXT, HELP_TEXT, btn, btns



   
    
    
# Call backs @CGSUPDATES 

@app.on_callback_query()
async def cb_data(client, message):
    if message.data == "help":
        await message.message.edit_text(
            text=HELP_TEXT.format(message.from_user.mention),
            reply_markup=BUTTONSA,
            disable_web_page_preview=True,
        )
    elif message.data == "helpback":
        await message.message.edit_text(
            text=START_TEXT.format(message.from_user.mention),
            reply_markup=BUTTONS,
            disable_web_page_preview=True
        )
