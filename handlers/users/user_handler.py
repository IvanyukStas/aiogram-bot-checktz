import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.inline.category_keyboard import categories_kb
from keyboards.inline.user_keyboard import acept_keyboard
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
    data = get_task(call.data[4:])
    message = ''
    for d in data:
        message += d[1] + ' '
    await call.message.answer(f'{message}', reply_markup=acept_keyboard)
    await call.message.edit_reply_markup()

@dp.callback_query_handler(text_contains='acept', state=UserState.executor)
async def acept_task(call: types.CallbackQuery):
    await call.message.answer(f' rere tgnf')
    await call.message.edit_reply_markup()


@dp.callback_query_handler(text='cancel', state=UserState.executor)
async def acept_task(call: types.CallbackQuery):
    await call.message.answer('Выберите категорию:',reply_markup=categories_kb)
    await call.message.edit_reply_markup()