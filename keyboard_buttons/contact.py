from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def contact_entry_kb() -> InlineKeyboardMarkup:
    button = InlineKeyboardButton(text="✉️ Ustozga yozish", callback_data="contact_teacher")
    return InlineKeyboardMarkup(inline_keyboard=[[button]])
