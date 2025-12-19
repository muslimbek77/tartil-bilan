from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


async def set_default_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="contact", description="Ustoz bilan bog'lanish"),
        BotCommand(command="help", description="Yordam"),
        BotCommand(command="about", description="Biz haqimizda"),

    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())