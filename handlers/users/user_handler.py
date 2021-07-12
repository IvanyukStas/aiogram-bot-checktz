import logging

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.category_keyboard import categories_kb
from loader import dp
from states.user_state import UserState
from utils.db_api.sqlite_db import add_user_to_bd


@dp.message_handler(state=UserState.registration)
async def registration(message: types.Message):
    a = message.text.split(' ')
    fio = ''
    tel = 0
    for i in a:
        if i.isdigit():
            tel = i
        else:
            fio = fio + i + ' '
    user_data = (message.from_user.id, fio,  tel)
    print(user_data)
    add_user_to_bd(user_data)
    await message.answer(f'Добавили в базу данных!', reply_markup=categories_kb)
    logging.info(f'Добавили нвоого пользователя {message.from_user.id}')
    UserState.executor.set()