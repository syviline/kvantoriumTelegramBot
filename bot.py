import telebot
from telebot import types

bot = telebot.TeleBot('6172790383:AAHhhXexws5mUkwy139XcNfUIJ4zSVFnj70')

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Здравствуйте! Какое направление вы хотите выбрать?', reply_markup=get_markup())

def get_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    # Добавлены кнопки для всех направлений
    btns = [types.InlineKeyboardButton(name, callback_data=data) for name, data in [
        ('Робоквантум', 'robo'), ('Промдизайн', 'design'), ('IT-квантум', 'it'),
        ('Hi-Tech цех', 'hitech'), ('Автоквантум', 'auto'), ('Аэроквантум', 'aero'),
        ('Наноквантум', 'nano'), ('Геоквантум', 'geo'), ('Биоквантум', 'bio'),
        ('Энерджиквантум', 'energy'), ('VR квантум', 'vr'), ('Я не знаю', 'idk')
    ]]
    markup.add(*btns)
    return markup

directions_descriptions = {
    'robo': 'Робоквантум: Основан на проектировании и управлении робототехническими системами.',
    'design': 'Промдизайн: Фокусируется на проектировании объектов массового производства.',
    'it': 'IT-квантум: Сосредоточен на информационных технологиях для решения прикладных задач.',
    'hitech': 'Hi-Tech цех: Занимается передовыми технологиями для материализации проектов.',
    'auto': 'Автоквантум: Включает разработки в области наземного транспорта, проектирование и конструирование.',
    'aero': 'Аэроквантум: Ориентирован на создание летательных аппаратов, включая беспилотные.',
    'nano': 'Наноквантум: Охватывает исследование на наноразмерном уровне и создание новых материалов.',
    'geo': 'Геоквантум: Работа с геоинформационными технологиями и пространственными данными.',
    'bio': 'Биоквантум: Инженерно-биологические системы, прикладная биология и биотехнологии.',
    'energy': 'Энерджиквантум: Знакомство с основами традиционной и альтернативной энергетики.',
    'vr': 'VR квантум: Разработка приложений виртуальной, дополненной и смешанной реальности.',
    'idk': 'Если вы не знаете какое направление вам выбрать, предлагаем пройти тест!'
}

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    bot.send_message(chat_id, directions_descriptions.get(call.data, 'Выбрано неизвестное направление'))

bot.polling(none_stop=True)
