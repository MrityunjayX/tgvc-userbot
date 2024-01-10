"""
tgvc-userbot, Telegram Voice Chat Userbot
Copyright (C) 2021  Dash Eclipse

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from os import environ
import logging


from pyrogram import Client, idle

    
API_ID = int(environ.get("API_ID", 6))
API_HASH = environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
SESSION_NAME = environ.get("SESSION_NAME", None)

PLUGINS = dict(
    root="plugins",
    include=[
        "vc." + environ["PLUGIN"],
        "ping",
        "sysinfo",
        "stream",
        "devtools"
    ]
)

app = Client(SESSION_NAME, API_ID, API_HASH, plugins=PLUGINS)

app.start()
print('>>> USERBOT STARTED')
logging.info('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
logging.info('>>> USERBOT STOPPED')
