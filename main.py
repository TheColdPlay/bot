from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image


API_TOKEN = '5611442031:AAHl4bkynBZh_wZKC5_12p8yxiT-0KsOJk8'
 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def qr(message: types.Message):
   await message.answer("Привет.Введи свой иин для регистрации.")
   await bot.send_photo(chat_id=message.chat.id, photo='https://i.pinimg.com/originals/c7/8a/1f/c78a1ff26086681a2712a0477504b785.jpg')


urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Четная', callback_data="even")
urlButton2 = InlineKeyboardButton(text='Нечетная', callback_data="odd")
urlkb.add(urlButton,urlButton2)


# @dp.message_handler()
# async def signup(message: types.Message):
#     await message.answer(text="Вы можете прописать команду help для помощи!",
#                     )
    
@dp.message_handler(lambda message:len(message.text) == 12)
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Расписание")
    keyboard.add(button_1)
    button_2 = "Успеваемость"
    keyboard.add(button_2)
    button_3 = "Уведомления"
    keyboard.add(button_3)
    button_4 = "Учебные материалы"
    keyboard.add(button_4)
    button_5 = "Другие услуги"
    keyboard.add(button_5)
    await message.answer("Выберите нужную услугу", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text =="Расписание")
async def with_puree(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Четная", callback_data="even"))
    keyboard.add(InlineKeyboardButton(text="Нечетная", callback_data="odd"))
    await message.answer("Выберите неделю",reply_markup=urlkb)

 


@dp.message_handler(lambda message: message.text =="Успеваемость")
async def with_puree(message: types.Message):
    await message.answer("Выберите предмет")

@dp.message_handler(lambda message: message.text =="Уведомления")
async def with_puree(message: types.Message):
    await message.answer("Выберите вкл/выкл")



@dp.message_handler(lambda message: message.text =="Другие услуги")
async def with_puree(message: types.Message):
    await message.answer("тд")

@dp.message_handler(lambda message: message.text =="Учебные материалы")
async def with_puree(message: types.Message):
    await message.answer("Выберите предмет")

@dp.callback_query_handler(text="odd")
async def choice_registr_method(callback_query: types.CallbackQuery):
    await bot.send_photo(
        callback_query.from_user.id,
        photo=type.InputFile("1.png")
    )
@dp.callback_query_handler(text="even")
async def choice_registr_method(callback_query: types.CallbackQuery):
    await bot.send_photo(
        callback_query.from_user.id,
        photo=types.InputFile('img/1.png')
    )

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
