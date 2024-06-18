from pyrogram import Client, filters
import os
from pyrogram.types import *
from pyrogram import filters

import time
import random
import psutil
import platform
import logging
from config import OWNER_ID, BOT_USERNAME
from config import *
from COPYRIGHT import COPYRIGHT as app

import pyrogram
from pyrogram.errors import FloodWait


NYKAA = [
    "https://telegra.ph/file/167699a93e93a71f088cd.jpg",
]


start_txt = """<b> ❖ ʜɪɪ ʙᴀʙʏ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !\n━━━━━━━━━━━━━━━━━━━━━━\n\n● ɪ ᴀᴍ ɢʀᴏᴜᴘ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴄᴏᴘʏʀɪɢʜᴛ ʙᴏᴛ.\n● ɪ ʜᴀᴠᴇ ɢʀᴏᴜᴘ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ғᴇᴀᴛᴜʀᴇs.\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ @itz_Asuraa </b>"""

@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="Cright_back"),
          InlineKeyboardButton("ʜᴇʟᴘ", callback_data="Asur_back")
        ],
        [
          InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", callback_data="gib_source"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(random.choice(NYKAA), caption=start_txt,reply_markup=reply_markup
    )

# ------------------------------------------------------------------------------- #


gd_buttons = [              
        [
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="https://t.me/roy_editx"),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/THE_FRIENDZ"),    
        ]
        ]
# ------------------------------------------------------------------------------- #

ROY_BTN = [              
        [
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/the_friendz"),
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="https://t.me/roy_editx"),    
        ]
]
# ------------------------------------------------------------------------------- #


@app.on_callback_query(filters.regex("cuteback"))
async def cutebackbutton(client, callback_query: CallbackQuery, _):  
    try:
        startkeyboard = [
            [ 
              InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
            [
              InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="Cright_back"),
              InlineKeyboardButton("ʜᴇʟᴘ", callback_data="Asur_back")
            ],
            [
              InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", callback_data="gib_source"),
            ]
        ]
        await callback_query.message.edit_caption(start_txt,  
                reply_markup=InlineKeyboardMarkup(startkeyboard)
                )
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        await callback_query.message.reply_text(error_message)

    

@app.on_callback_query(filters.regex("Cright_back"))
async def Cright_back(_, query: CallbackQuery):
    await query.message.edit_caption(ABOUT_STRING,
                                    reply_markup=InlineKeyboardMarkup(gd_buttons),)
        

# -------------------------------------------------------------------------------------


ABOUT_STRING = """**❖ ɪ ʜᴀᴠᴇ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ ɢʀᴏᴜᴘ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ғᴇᴀᴛᴜʀᴇs.\n\n● ɴᴏ ᴘᴏʀɴᴏɢʀᴀᴘʜʏ \n● ɴᴏ ᴍᴇssᴀɢᴇ ᴇᴅɪᴛ\n● ɴᴏ ᴘᴅғ ғɪʟᴇ sʜᴀʀᴇ\n● ɴᴏ ʟᴏɴɢ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ\n● ɴᴏ sᴘᴀᴍᴍᴇʀ ʀᴇᴘᴏʀᴛs\n● ɴᴏ ɴᴄᴇʀᴛ ᴄᴏɴᴛᴇsᴛ\n\n❖ ᴀɴᴅ ᴍᴏʀᴇ ᴄᴏɴᴛᴇsᴛs ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ, ғᴜʟʟ ɢʀᴏᴜᴘ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ.**"""


# -------------------------------------------------------------------------------------

HELP_STRING = """**❖ ᴏᴡɴᴇʀ/sᴜᴅᴏ ᴜsᴇʀ ᴄᴍᴅs ⏤͟͟͞͞★\n\n● /bcast ➥ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀɴʏ ᴍᴇssᴀɢᴇ.\n● /announce ➥ ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀɴɴᴏᴜɴᴄᴇ.\n\n❖ ᴀʟʟ ᴜsᴇʀs  ᴄᴏᴍᴍᴀɴᴅs ⏤͟͟͞͞★\n\n● /start ➥ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.\n● /ping ➥ ᴄʜᴋ ʙᴏᴛ ᴘɪɴɢ sᴛᴀᴛs.\n● /repo ➥ ɢᴇᴛ ʙᴏᴛ ʀᴇᴘᴏ.\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥  @itz_Asuraa**"""

# ------------------------------------------------------------------------------- #

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
    ],
]

# ------------------------------------------------------------------------------- #


@app.on_callback_query(filters.regex("Asur_back"))
async def Asur_back(_, query: CallbackQuery):
    await query.message.edit_caption(HELP_STRING,
                                    reply_markup=InlineKeyboardMarkup(ROY_BTN),)

# ------------------------------------------------------------------------------- #
REPO_STRING = """**
❖ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ  ♥︎

● ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴄᴏᴘʏʀɪɢʜᴛ sʜɪᴇʟᴅ ʙᴏᴛ ⚡ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.

❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ @itz_Asuraa
"""

@app.on_message(filters.command("repo"))
async def start(_, msg):
    REPO_BTN = [
        [
          InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/GOD-R4V4N/RavanCopyRight-Robot"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(REPO_BTN)
    
    await msg.reply_photo(photo="https://telegra.ph/file/feb8ec9cd6194018ccc4c.jpg", caption=REPO_STRING,reply_markup=reply_markup=
                         )


# ------------------------------------------------------------------------------- #

def time_formatter(milliseconds: float) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def size_formatter(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {unit}"


# ------------------------------------------------------------------------------- #


@app.on_message(filters.command("ping"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')

    python_version = platform.python_version()

    reply_text = (
        f"❖ ᴄᴏᴘʏʀɪɢʜᴛ ʙᴏᴛ ᴘɪɴɢ sᴛᴀᴛs ⏤͟͟͞͞★\n\n"
        f"● ᴜᴘᴛɪᴍᴇ ➥ {uptime}\n"
        f"● ᴄᴘᴜ ➥ {cpu}%\n"
        f"● ᴛᴏᴛᴇʟ ꜱᴛᴏʀᴀɢᴇ ➥ {size_formatter(storage.total)}\n"
        f"● ᴜsᴇᴅ ➥ {size_formatter(storage.used)}\n"
        f"● ғʀᴇᴇ ➥ {size_formatter(storage.free)}\n"
        f"● ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ➥ {python_version}\n\n"
        f"❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥  @itz_Asuraa "
    )

    await message.reply(reply_text, reply_markup=InlineKeyboardMarkup(EVAA), quote=True)

# -------------------------------------------------------------------------------------

FORBIDDEN_KEYWORDS = ["porn", "xxx", "sex", "NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]

@app.on_message()
async def handle_message(client, message):
    if any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"⬤ ᴅᴇʟᴇᴛɪɴɢ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ɪᴅ ➥ {message.id}")
        await message.delete()
      # user_mention = msg.from_user.mention
        await message.reply_text(f"⬤ ʜᴇʏ {user_mention}, ʙᴀʙʏ ᴅᴏɴ'ᴛ sᴇɴᴅ ɴᴇxᴛ ᴛɪᴍᴇ.")
    if any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"⬤ ᴅᴇʟᴇᴛɪɴɢ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ɪᴅ ➥ {message.id}")
        await message.delete()
        #user_mention = msg.from_user.mention
        await message.reply_text(f"⬤ ʜᴇʏ {user_mention}, ʙᴀʙʏ ᴅᴏɴ'ᴛ sᴇɴᴅ, ɴᴇxᴛ ᴛɪᴍᴇ.")
        
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()



# ----------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
def delete_long_messages(_, m):
    return len(m.text.split()) > 200

@app.on_message(filters.group & filters.private & delete_long_messages)
async def delete_and_reply(_, msg):
    await msg.delete()
    #user_mention = msg.from_user.mention
    await app.send_message(msg.chat.id, f"⬤ ʜᴇʏ {user_mention} ʙᴀʙʏ, ᴘʟᴇᴀsᴇ ᴋᴇᴇᴘ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ sʜᴏʀᴛ.")
    

# -----------------------------------------------------------------------------------


async def delete_pdf_files(client, message):
    if message.document and message.document.mime_type == "application/pdf":
        warning_message = f"⬤ ʜᴇʏ {user_mention} ᴅᴏɴ'ᴛ sᴇɴᴅ ᴘᴅғ ғɪʟᴇs ʙᴀʙʏ, ғᴏʀ ᴄᴏᴘʏʀɪɢʜᴛ ᴄʟɪᴍʙ."
        await message.reply_text(warning_message)
        await message.delete()
    else:  
        pass

@app.on_message(filters.group & filters.document)
async def message_handler(client, message):
    await delete_pdf_files(client, message)


