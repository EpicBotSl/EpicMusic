import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_sticker("CAACAgUAAxkBAAEFFdJisHcXrQZdD6l32JJPM0xg9RwWrQACUgUAAhzhiFX8K8u4AiS1cygE")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**
👻 ʜᴇʏ {message.from_user.mention()} !
𝖨𝗆 𝖤𝗉𝗂𝖼 𝖬𝗎𝗌𝗂𝖼 𝖡𝗈𝗍 𝖨 𝖺𝗆 𝖯𝗈𝗐𝖾𝗋𝖥𝗎𝗅𝗅 𝖵𝖼 𝖡𝗈𝗍💥
❇ 𝖨 𝖢𝖺𝗇 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖲𝗈𝗇𝗀𝗌🐧
❇ 𝖨 𝖢𝖺𝗇 𝗉𝗅𝖺𝗒 𝖲𝗈𝗇𝗀𝗌 𝖥𝗈𝗋 𝖸𝗈𝗎𝗋 𝖵𝖼🌴
❇ 𝖨 𝖢𝖺𝗇 𝖦𝖾𝗍 𝖴𝗌𝖾𝗋𝗌 𝖨𝖽🍁
𝖢𝗋𝖾𝖺𝗍𝖾𝖽 𝖡𝗒 </ᴇᴘɪᴄ ʙᴏᴛs <s/ʟ>🇱🇰**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ᴀᴅᴅ ᴍᴇ 🚀​ ", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        " ᴏᴡɴᴇʀ🙄 ", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        " sᴜᴘᴘᴏʀᴛ🆘 ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        " ɪɴʟɪɴᴇ🔍 ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "</ᴇᴘɪᴄ ʙᴏᴛs <s/ʟ>🇱🇰", url=f"https://t.me/EpicBotsSl"
                    )]
            ]
       ),
    )

