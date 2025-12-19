from aiogram import Bot, Dispatcher
from data import config
from baza.sqlite import Database
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN

bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
db = Database(path_to_db="main.db")
dp = Dispatcher()