from pyrogram import Client, idle

from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import sys
import os
from config import *
import libtorrent as lt
from datetime import datetime
import logging

 
class app(Client):
    def __init__(self):
        super().__init__(
            name="app",
            api_hash=API_HASH,
            api_id=APP_ID,            

       
            bot_token=BOT_TOKEN
        )
        self.LOGGER = LOGGER

async def start(self):
        await super().start()
        self.uptime = datetime.now()
        print("[INFO]: STARTING Lib Torrent CLIENT")  
        
        await app.run()






ses = lt.session()
ses.listen_on(6881, 6891)

queue = []

status = app.get_messages(LINK_ID,STATUS_ID)
