from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


admin_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Foydalanuvchilar soni"),
            KeyboardButton(text="Reklama yuborish"),
        ],
         [
            KeyboardButton(text="⛓ Kanallar ro'yxati"), 
        ],
         [
            KeyboardButton(text="➕ Kanal qo'shish"), 
            KeyboardButton(text="➖ Kanal o'chirish"), 
        ],
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

def inline_wars_btn(wars):
    if len(wars)<=6:
        row = 3
    elif len(wars)<=8: 
        row = 4
    elif len(wars)<=12: 
        row = 6
    elif len(wars)<=16: 
        row = 8
    else:
        row = 10
    
    
    l = []
    tr = 1
    for war in wars:
        l.append(InlineKeyboardButton(text=f"{tr}", callback_data=f"{war[0]}"))
        tr += 1
    l.append(InlineKeyboardButton(text=f"Asosiy menuga qaytish", callback_data=f"back_admin"))
    wars_check = InlineKeyboardMarkup(inline_keyboard=[l])
    
    return wars_check


def channel_add_options() -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text="Postni forward qilish", callback_data="add_forward"),
        InlineKeyboardButton(text="ID yuborish (-100...)", callback_data="add_id"),
        InlineKeyboardButton(text="Username yuborish (@kanal)", callback_data="add_username"),
    ]
    return InlineKeyboardMarkup(inline_keyboard=[buttons])