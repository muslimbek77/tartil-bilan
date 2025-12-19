from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


def contact_entry_kb() -> InlineKeyboardMarkup:
    button = InlineKeyboardButton(text="📞 Ustoz bilan bog'lanish", callback_data="contact_teacher")
    return InlineKeyboardMarkup(inline_keyboard=[[button]])


def share_phone_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📞 Telefon raqamni yuborish", request_contact=True)],
            [KeyboardButton(text="Bekor qilish")],
        ],
        resize_keyboard=True,
        input_field_placeholder="Savolingizni yozing yoki raqam yuboring",
    )
