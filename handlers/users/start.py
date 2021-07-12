import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from states.user_state import UserState


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         f"Предоставьте контактные данные (ФИО, рабочий номер)")
    await UserState.registration.set()
    logging.info(f'Начинаем процедуру регистрации нового Исполнителя')