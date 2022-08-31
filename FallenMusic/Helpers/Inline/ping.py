import config
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ping_ig = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="sᴜᴩᴩᴏʀᴛ",
                    url=config.SUPPORT_CHAT,
                ),
                InlineKeyboardButton(
                    text="sᴏᴜʀᴄᴇ",
                    url="https://t.me/Xd_LyF"
                )
            ]
        ]
    )
