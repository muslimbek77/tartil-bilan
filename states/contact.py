from aiogram.fsm.state import State, StatesGroup


class ContactTeacher(StatesGroup):
    waiting_message = State()
