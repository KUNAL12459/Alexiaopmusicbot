import asyncio
from time import time
from datetime import datetime
from Music import BOT_USERNAME
from Music.config import UPDATES_CHANNEL, ALEXIA_SUPPORT
from Music.MusicUtilities.helpers.filters import command
from Music.MusicUtilities.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7b35fd7da9c0c8864494f.jpg",
        caption=f"""**A Telegram Music Bot Based Mongodb.
 Add Me To Ur Chat For and Help and And Support Click On Buttons  ...
β‘ These Features A.I Based
Powered By [π¨π³π¬πΏπ°π¨](t.me/ALEXIA_SUPPORT) ...
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β β° α΄α΄α΄ α΄α΄ α΄α΄ Κα΄α΄Κ Ι’Κα΄α΄α΄ β± β", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Κα΄Κα΄ & α΄α΄α΄α΄α΄Ι΄α΄κ±", url=f"https://t.me/ALEXIA_UPDATE/3"
                    ),
                    InlineKeyboardButton(
                        "κ±α΄α΄Κα΄α΄ α΄α΄α΄α΄", url="https://github.com/KUNAL12459/Alexiaopmusicbot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π ββββ βͺβ’ππ©πππ­π ππ‘ππ§π§ππ₯β’β« ββββ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "ββββ βͺ β’ππ?π©π©π¨π«π­ ππ«π¨π?π©β’ β« ββββπ?π³", url=f"https://t.me/{ALEXIA_SUPPORT}"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7b35fd7da9c0c8864494f.jpg",
        caption=f"""Thanks For Adding Me To Ur Chat, For Any Query U Can Join Our Support Groups π€­""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π₯ α΄α΄ΙͺΙ΄ Κα΄Κα΄ π", url=f"https://t.me/{SUPPORT_GROUP}")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7b35fd7da9c0c8864494f.jpg",
        caption=f"""Here Is The Source Code Fork And Give Stars β¨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " Κα΄α΄α΄ βοΈ", url=f"https://github.com/KUNAL12459/Alexiaopmusicbot")
                ]
            ]
        ),
    )
