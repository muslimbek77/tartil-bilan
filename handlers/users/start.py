from aiogram.types import Message
from keyboard_buttons.contact import contact_entry_kb
from loader import dp,db, ADMINS
from aiogram.filters import CommandStart,Command

@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) # foydalanuvchi bazaga qo'shildi
        await message.answer(
            text=(
                "Assalomu alaykum, botimizga hush kelibsiz! "
                "Tajvid va Qur'on kursi bo'yicha savollaringiz bo'lsa, "
                "tugma orqali ustozga yozishingiz mumkin."
            ),
            reply_markup=contact_entry_kb(),
        )
    except:
        await message.answer(
            text=(
                "Assalomu alaykum! Ustoz bilan bog'lanish uchun quyidagi tugmadan foydalaning."
            ),
            reply_markup=contact_entry_kb(),
        )

