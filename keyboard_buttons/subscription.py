from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import bot

async def check_button(channels):
    me = await bot.get_me()
    l = []
    for channel in channels:
        if channel[2] == 0:
            l.append(InlineKeyboardButton(text=f"{channel[1]}", url=f"{channel[0]}"))
        else:
            l.append(InlineKeyboardButton(text=f"✅ {channel[1]}", url=f"{channel[0]}"))
    # Use callback to trigger subscription re-check in middleware
    l.append(InlineKeyboardButton(text="✅ Obunani tekshirish ✅", callback_data="check_subs"))
    channels_check = InlineKeyboardMarkup(inline_keyboard=[l])
    return channels_check