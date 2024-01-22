import telebot
from telebot import types

bot = telebot.TeleBot('6172790383:AAHhhXexws5mUkwy139XcNfUIJ4zSVFnj70')

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Здравствуйте! Какое направление вы хотите выбрать?', reply_markup=get_markup())

def get_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btnMedia = types.InlineKeyboardButton('Медиа квантум', callback_data='media')
    btnRobo = types.InlineKeyboardButton('Робо квантум', callback_data='robo')
    btnDesign = types.InlineKeyboardButton('Промышленный дизайн', callback_data='design')
    btnIT = types.InlineKeyboardButton('IT-квантум', callback_data='it')
    btnHiTech = types.InlineKeyboardButton('Hi-Tech цех', callback_data='hitech')
    btnAuto = types.InlineKeyboardButton('Автоквантум', callback_data='auto')
    btnAero = types.InlineKeyboardButton('Аэроквантум', callback_data='aero')
    btnNano = types.InlineKeyboardButton('Наноквантум', callback_data='nano')
    btnGeo = types.InlineKeyboardButton('Геоквантум', callback_data='geo')
    btnBio = types.InlineKeyboardButton('Биоквантум', callback_data='bio')
    btnEnergy = types.InlineKeyboardButton('Энерджиквантум', callback_data='energy')
    btnVRAR = types.InlineKeyboardButton('VR/AR квантум', callback_data='vrar')
    btnIdk = types.InlineKeyboardButton('Я не знаю', callback_data='idk')
    markup.add(btnMedia, btnRobo, btnDesign, btnIT, btnHiTech, btnAuto, btnAero, btnNano, btnGeo, btnBio, btnEnergy, btnVRAR, btnIdk)
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    directions = {
        'media': 'Медиа квантум',
        'robo': 'Робо квантум',
        'design': 'Промышленный дизайн',
        'it': 'IT-квантум',
        'hitech': 'Hi-Tech цех',
        'auto': 'Автоквантум',
        'aero': 'Аэроквантум',
        'nano': 'Наноквантум',
        'geo': 'Геоквантум',
        'bio': 'Биоквантум',
        'energy': 'Энерджиквантум',
        'vrar': 'VR/AR квантум',
        'idk': 'Если вы не знаете какое направление вам выбрать, предлагаем пройти тест!'
    }
    bot.answer_callback_query(call.id, f'Вы выбрали {directions[call.data]}')

bot.polling(none_stop=True)
