from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['mem'])
async def start_command(message: types.Message):
    await message.answer_photo(types.InputFile(r"C:\Users\Admin\Downloads\200px-Wojak.png"))


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "Как зовут учителя?"
    answer = [
        "Владимир",
        "Боб",
        "Эсенбек",
        "Гриффит",
        "Дио",
        "Карл",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    question = "Какой нынешний месяц обучения?"
    answer = [
        "1",
        "2",
        "3",
        "73",
        "Python",
        "Не знаю",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
    )


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await message.answer(int(message.text)**2)
    else:
        await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)