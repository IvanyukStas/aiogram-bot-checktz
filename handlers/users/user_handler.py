import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.inline.category_keyboard import categories_kb
from loader import dp
from states.user_state import UserState
from utils.db_api.sqlite_db import add_user_to_bd, get_task


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
    await UserState.executor.set()


@dp.callback_query_handler(Text(startswith='btn_'), state=UserState.executor)
async def check_task_for_category(call: types.CallbackQuery):
    print('Работает', call.data[4:])
    logging.info(f'Получили колбек')
    await call.answer('Работает')
    data = get_task(call.data[4:])
    await call.message.answer(f'{data}')
