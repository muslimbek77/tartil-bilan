from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove

from keyboard_buttons.contact import contact_entry_kb, share_phone_kb
from loader import ADMINS, bot, dp
from states.contact import ContactTeacher


async def _notify_admins(payload: str):
    for admin_id in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin_id), text=payload)
        except Exception:
            # Adminlarga xabar yuborishda xatolik bo'lsa ham foydalanuvchiga jarayon to'xtamasin
            continue


def _user_info(message: Message) -> str:
    username = f"@{message.from_user.username}" if message.from_user.username else "(username yo'q)"
    return (
        f"Foydalanuvchi: {message.from_user.full_name}\n"
        f"ID: <code>{message.from_user.id}</code> | {username}\n"
    )


@dp.message(Command("contact"))
async def contact_command(message: Message, state: FSMContext):
    await state.set_state(ContactTeacher.waiting_message)
    await message.answer(
        "Ustozga savolingizni yuboring yoki telefon raqamingizni ulashing.",
        reply_markup=share_phone_kb(),
    )


@dp.callback_query(F.data == "contact_teacher")
async def contact_callback(call: CallbackQuery, state: FSMContext):
    await state.set_state(ContactTeacher.waiting_message)
    await call.message.answer(
        "Savolingizni yozib yuboring yoki telefon raqamingizni ulashing.",
        reply_markup=share_phone_kb(),
    )
    await call.answer()


@dp.message(ContactTeacher.waiting_message, F.text.casefold() == "bekor qilish")
async def cancel_contact(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Bekor qilindi.", reply_markup=ReplyKeyboardRemove())


@dp.message(ContactTeacher.waiting_message, F.contact)
async def handle_phone(message: Message, state: FSMContext):
    phone = message.contact.phone_number
    info = _user_info(message)
    payload = f"📞 Telefon raqami yuborildi\n{info}Raqam: {phone}"
    await _notify_admins(payload)
    await message.answer(
        "Raqamingiz ustoza yuborildi. Tez orada bog'lanadi.",
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.clear()


@dp.message(ContactTeacher.waiting_message)
async def forward_question(message: Message, state: FSMContext):
    info = _user_info(message)
    user_text = message.text or message.caption or "(matn yuborilmadi)"
    payload = f"✉️ Yangi murojaat\n{info}Matn: {user_text}"
    await _notify_admins(payload)
    await message.answer(
        "Savolingiz ustoza yuborildi. Javobini kuting.",
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.clear()


