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
π» Κα΄Κ {message.from_user.mention()} !
π¨π π€πππΌ π¬ππππΌ π‘ππ π¨ πΊπ π―πππΎππ₯πππ π΅πΌ π‘πππ₯
β π¨ π’πΊπ π£ππππππΊπ½ π²πππππ§
β π¨ π’πΊπ πππΊπ π²ππππ π₯ππ πΈπππ π΅πΌπ΄
β π¨ π’πΊπ π¦πΎπ π΄ππΎππ π¨π½π
π’ππΎπΊππΎπ½ π‘π </α΄α΄Ιͺα΄ Κα΄α΄s <s/Κ>π±π°**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " α΄α΄α΄ α΄α΄ πβ ", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        " α΄α΄‘Ι΄α΄Κπ ", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        " sα΄α΄α΄α΄Κα΄π ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        " ΙͺΙ΄ΚΙͺΙ΄α΄π ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "</α΄α΄Ιͺα΄ Κα΄α΄s <s/Κ>π±π°", url=f"https://t.me/EpicBotsSl"
                    )]
            ]
       ),
    )

