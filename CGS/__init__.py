#MIT License
#https://t.me/CGSUPDATES

import logging
from CGS.db.tginfo import API_HASH, API_ID, BOT_TOKEN
from pyrogram import Client
from Python_ARQ import ARQ
from aiohttp import ClientSession
from CGS.db.tginfo import ARQ_API_KEY


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

CGS = Client("CGS", bot_token=BOT_TOKEN, api_hash=API_HASH, api_id=API_ID)
ARQ_API_URL = "https://thearq.tech"
aiohttpsession = ClientSession()
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
