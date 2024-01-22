import telebot
from telebot import types

bot = telebot.TeleBot('6415511856:AAFDpvJ-2YsryCM_fv09CnYPBqOMiMlqpbg')


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Здравствуйте! Какое направление вы хотите выбрать?', reply_markup=get_markup())


def get_markup():
    markup = types.InlineKeyboardMarkup()
    btnIt = types.InlineKeyboardButton('Айти', callback_data='it')
    btnrobo = types.InlineKeyboardButton('Робо', callback_data='robo')
    btnavto = types.InlineKeyboardButton('Авто', callback_data='auto')
    btnaer = types.InlineKeyboardButton('Аэро', callback_data='aero')
    btnIdk = types.InlineKeyboardButton('Я не знаю', callback_data='idk')
    markup.add(btnIt, btnrobo, btnavto, btnaer, btnIdk)
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'it':
        bot.answer_callback_query(call.id, 'Вы выбрали Айти' )

    elif call.data == 'robo':
        bot.answer_callback_query(call.id, 'Вы выбрали Робо')

    elif call.data == 'auto':
        bot.answer_callback_query(call.id, 'Вы выбрали Авто')

    elif call.data == 'aero':
        bot.answer_callback_query(call.id, 'Вы выбрали Аэро')

    elif call.data == 'idk':
        bot.answer_callback_query(call.id, 'Если вы не знаете какое напрвление вам выбрать предлогаем пройти тест!')

bot.polling(none_stop=True)