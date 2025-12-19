from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove

from keyboard_buttons.contact import contact_entry_kb
from loader import ADMINS, bot, dp
from filters.admin import IsBotAdminFilter
from states.contact import ContactTeacher


# Admin xabariga reply qilinganda user_id ni aniqlash uchun xotira xaritasi
ADMIN_REPLY_MAP = {}  # key: (admin_id, admin_message_id) -> user_id
# Foydalanuvchiga yuborilgan admin javoblariga yana reply qilishni qo'llash uchun
USER_REPLY_MAP = {}   # key: user_message_id -> admin_id


async def _notify_admins(payload: str, user_id: int):
    for admin_id in ADMINS:
        try:
            sent = await bot.send_message(chat_id=int(admin_id), text=payload)
            ADMIN_REPLY_MAP[(int(admin_id), sent.message_id)] = user_id
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
        "Savolingizni yozib yuboring. Ustozga uzatiladi.",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.callback_query(F.data == "contact_teacher")
async def contact_callback(call: CallbackQuery, state: FSMContext):
    await state.set_state(ContactTeacher.waiting_message)
    await call.message.answer(
        "Savolingizni yozib yuboring. Ustozga uzatiladi.",
        reply_markup=ReplyKeyboardRemove(),
    )
    await call.answer()


@dp.message(ContactTeacher.waiting_message, F.text.casefold() == "bekor qilish")
async def cancel_contact(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Bekor qilindi.", reply_markup=ReplyKeyboardRemove())


@dp.message(ContactTeacher.waiting_message, F.contact)
async def handle_phone(message: Message, state: FSMContext):
    await message.answer("Faqat matn yuboring, telefon raqami shart emas.")


@dp.message(ContactTeacher.waiting_message)
async def forward_question(message: Message, state: FSMContext):
    info = _user_info(message)
    user_text = message.text or message.caption or "(matn yuborilmadi)"
    payload = f"✉️ Yangi murojaat\n{info}Matn: {user_text}"
    await _notify_admins(payload, user_id=message.from_user.id)
    await message.answer(
        "Habaringiz adminga yetkazildi. Javobni shu yerda olasiz.",
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.clear()


@dp.message(
    F.reply_to_message,
    F.text,
    IsBotAdminFilter(ADMINS),
)
async def admin_reply_to_user(message: Message):
    key = (message.from_user.id, message.reply_to_message.message_id)
    user_id = ADMIN_REPLY_MAP.get(key)
    if not user_id:
        return
    sent = await bot.send_message(chat_id=user_id, text=f"Admin javobi:\n{message.text}")
    USER_REPLY_MAP[sent.message_id] = message.from_user.id
    await message.answer("Javob foydalanuvchiga yuborildi ✅")


@dp.message(
    F.reply_to_message,
    F.text,
)
async def user_reply_to_admin(message: Message):
    admin_id = USER_REPLY_MAP.get(message.reply_to_message.message_id)
    info = _user_info(message)
    user_text = message.text or message.caption or "(matn yuborilmadi)"
    payload = f"✉️ Yangi murojaat\n{info}Matn: {user_text}"

    if admin_id:
        try:
            sent = await bot.send_message(chat_id=int(admin_id), text=payload)
            ADMIN_REPLY_MAP[(int(admin_id), sent.message_id)] = message.from_user.id
        except Exception:
            await _notify_admins(payload, user_id=message.from_user.id)
    else:
        await _notify_admins(payload, user_id=message.from_user.id)

    await message.answer("Habaringiz adminga yetkazildi. Javobni shu yerda olasiz.")


