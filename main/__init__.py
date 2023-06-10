from pyrogram import Client, idle

from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

import os
from config import *
import libtorrent as lt
import time 
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

logging.getLogger("pyrogram").setLevel(logging.WARNING)
app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
  )
app.start()


print("[INFO]: STARTING Lib Torrent CLIENT")
idle()
ses = lt.session()
ses.listen_on(6881, 6891)

queue = []

status = app.get_messages(LINK_ID,STATUS_ID)
