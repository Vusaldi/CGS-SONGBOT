import request

import asyncio
import math
import os
import time
import wget



from random import randint
from urllib.parse import urlparse

import aiofiles
import aiohttp
import youtube_dl
from yt_dlp import YoutubeDL
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import *
from youtube_search import YoutubeSearch


from CGS import CGS
from CGS import arq
from CGS import aiohttpsession as session
from pyrogram import filters
from io import BytesIO
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

is_downloading = False

# Funtion To Download song
"""
THIS IS SAAVN 
DOWNLOAD CODES
BY @CGSUPDATES
"""
async def download_song(url):
    async with session.get(url) as resp:
        song = await resp.read()
    song = BytesIO(song)
    song.name = "CGS Songs.mp3"
    return song

@CGS.on_message(filters.command("saavn") & ~filters.edited)
async def jssong(_, message):
    global is_downloading
    if len(message.command) < 2:
        return await message.reply_text("/saavn requires an argument.")
    if is_downloading:
        return await message.reply_text(
            "Another download is in progress, try again after sometime."
        )
    is_downloading = True
    text = message.text.split(None, 1)[1]
    m = await message.reply_text("Searching For Saavn....")
    try:
        songs = await arq.saavn(text)
        if not songs.ok:
            await m.edit(songs.result)
            is_downloading = False
            return
        sname = songs.result[0].song
        slink = songs.result[0].media_url
        ssingers = songs.result[0].singers
        sduration = songs.result[0].duration
        await m.edit(",📥Downloading Saavn...")
        song = await download_song(slink)
        await m.edit("📤 Uploading Saavn...")
        await message.reply_audio(
            audio=song,
            title=sname,
            performer=ssingers,
            duration=sduration,
            caption="Uploaded By: @CGSSongBot",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("☘️Join Updates☘️", url=f"https://t.me/CGSUpdates")]]),
        )
        await m.delete()
    except Exception as e:
        is_downloading = False
        return await m.edit(str(e))
    is_downloading = False
    song.close()


# lyrics download by @CGSUPDATES
"""
THIS IS LYRICS
DOWNLOAD CODES
BY @CGSUPDATES
"""


@CGS.on_message(filters.command(["lyric"]))
async def lirik(_, message):
    rep = await message.reply_text("🔎 **searching lyrics...**")
    try:
        if len(message.command) < 2:
            await message.reply_text("**give a lyric name too !**")
            return
        query = message.text.split(None, 1)[1]
        resp = requests.get(f"https://api-tede.herokuapp.com/api/lirik?l={query}").json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception as ex:
        print(ex)
        await rep.edit("**Lyrics not found.** please give a valid song name !")

# Video Download By @CGSUPDATES
"""
THIS IS LYRICS
DOWNLOAD CODES
BY @CGSUPDATES
"""
@CGS.on_message(filters.command(["video"]))
async def vsong(pbot, message):
    ydl_opts = {
        'format':'best',
        'keepvideo':True,
        'prefer_ffmpeg':False,
        'geo_bypass':True,
        'outtmpl':'%(title)s.%(ext)s',
        'quite':True
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
        views = results[0]["views"]
        results[0]["url_suffix"]
        results[0]["views"]
        rby = message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply_text("📥 **downloading video...**")
        with YoutubeDL(ydl_opts) as ytdl:
            rep = f'🎙 **Title**: [{title[:35]}]({link})\n🎬 **Source**: `YouTube`\n⏱️ **Duration**: `{duration}`\n📤 **By**: @CGSUPDATES '
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"❌**YouTube Download Error !*** {str(e)}\n\n Go support chat👉 @CGSsupport")
    preview = wget.download(thumbnail)
    await msg.edit("📤 **uploading video...**")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=rep,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Updates Channel📢", url=f"https://t.me/CGSUpdates")]]))
    try:
        os.remove(file_name)
        await msg.delete()
    except Exception as e:
        print(e)
