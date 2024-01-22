import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

user_responses = {}

questions = [
    "Тебе нравится создавать и конструировать вещи?",
    "Интересуешься ли ты компьютерными технологиями и программированием?",
    "Любишь ли ты рисовать или заниматься дизайном?",
    "Увлекаешься ли ты изучением живой природы и биологии?",
    "Интересуешься ли техникой, машиностроением или автомобилями?",
    "Хочешь ли ты узнать больше о науке о Земле и географии?",
    "Привлекает ли тебя мир науки о космосе и авиации?",
    "Мечтаешь ли создавать новые материалы с помощью нанотехнологий?"
]

def start_test(message):
    chat_id = message.chat.id
    user_responses[chat_id] = {'robo': 0, 'design': 0, 'it': 0, 'hitech': 0, 'auto': 0, 'aero': 0, 'nano': 0, 'geo': 0, 'bio': 0, 'energy': 0, 'vr': 0}
    send_question(chat_id, 0)

def send_question(chat_id, question_num):
    questions = [
        "Тебе нравится создавать и конструировать вещи?",
        "Интересуешься ли ты компьютерными технологиями и программированием?",
        "Любишь ли ты рисовать или заниматься дизайном?",
        "Увлекаешься ли ты изучением живой природы и биологии?",
        "Интересуешься ли техникой, машиностроением или автомобилями?",
        "Хочешь ли ты узнать больше о науке о Земле и географии?",
        "Привлекает ли тебя мир науки о космосе и авиации?",
        "Мечтаешь ли создавать новые материалы с помощью нанотехнологий?"
    ]
    answers = [
        [("Да", "robo"), ("Нет", "other")],
        [("Да", "it"), ("Нет", "other")],
        [("Да", "design"), ("Нет", "other")],
        [("Да", "bio"), ("Нет", "other")],
        [("Да", "auto"), ("Нет", "other")],
        [("Да", "geo"), ("Нет", "other")],
        [("Да", "aero"), ("Нет", "other")],
        [("Да", "nano"), ("Нет", "other")]
    ]
    markup = types.InlineKeyboardMarkup()
    for answer_text, category in answers[question_num]:
        markup.add(types.InlineKeyboardButton(answer_text, callback_data=f'{category}_{question_num}'))
    bot.send_message(chat_id, questions[question_num], reply_markup=markup)

def handle_test_answer(call):
    category, question_num = call.data.split('_')
    chat_id = call.message.chat.id
    if category != 'other':
        user_responses[chat_id][category] += 1
    next_question = int(question_num) + 1
    if next_question < len(questions):
        send_question(chat_id, next_question)
    else:
        final_category = max(user_responses[chat_id], key=user_responses[chat_id].get)
        bot.send_message(chat_id, f"Вам, возможно, понравится направление: {directions_descriptions[final_category]}")

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Здравствуйте! Какое направление вы хотите выбрать?', reply_markup=get_markup())

@bot.message_handler(commands=['test'])
def start_test_command(message):
    start_test(message)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if '_' in call.data:
        handle_test_answer(call)
    else:
        chat_id = call.message.chat.id
        bot.send_message(chat_id, directions_descriptions.get(call.data, 'Выбрано неизвестное направление'))

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

bot.polling(none_stop=True)
