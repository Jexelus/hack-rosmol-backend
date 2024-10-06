import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import time

bot = telebot.TeleBot("7586843035:AAFoDA2w2au7UHhWqs36_yc7lGrsHcnv9K4")

# Словарь для хранения данных пользователя
user_progress = {}
coins = []

# Данные курса
course_data = [
    {
        'section': 'Этапы проектной деятельности',
        'theory1': """
        Залог успешного проектного управления – планирование всех этапов и видов деятельности. В зависимости от особенностей проекта может применяться как краткосрочное, так и долгосрочное планирование. Так, если важно выполнить все работы без опоздания, то при составлении планов устанавливают жесткие временные рамки завершения каждой стадии. Если достижение поставленной цели важнее сроков, то проектные планы могут допускать определенную степень гибкости.
Основные преимущества применения управления проектами в компании: ориентация на итоговые показатели, налаженная коммуникация с клиентами и заказчиками, возможность измерить в количественных показателях достижение той или иной цели, инновационный характер методики.
Этапы проектной деятельности предполагают четкое распределение задач и действий участников проектов, а также получение определенных результатов на каждом конкретном этапе выполнения проекта за счет использования соответствующих технологий проведения проектного исследования. 
        """,
        'theory2': """
        С проектной деятельностью мы сталкиваемся в своей жизни постоянно. К ней можно отнести многое из того, что мы делаем. От небольших проектов, занимающих дни или недели (например,  организации  дня  рождения  или  встречи  друзей), до  крупных  проектов, продолжающихся месяцы (например, подготовка выпускной работы или книги) или даже годы (например, строительство стадиона).

Необходимо изучить виды проектов и их классификацию, ознакомиться с этапами работы над проектами.

В рамках проектной деятельности результатом проекта может быть:

1) продукт, представляющий собой компонент другого изделия, улучшение изделия или конечное изделие;

2)  услуга или способность предоставлять услугу (например, бизнес-функция, поддерживающая производство или дистрибуцию);

3)  улучшение существующей линейки продуктов или услуг, предпринятых для уменьшения дефектов;

4)  конечный результат или документ (например, исследовательский проект приносит новые знания, которые можно использовать для определения наличия тенденции или пользы какого-либо нового процесса для общества);

5)  разработка или приобретение новой или усовершенствованной информационной системы (оборудование или программное обеспечение);

6)  исследование, результат которого будет надлежащим образом зафиксирован;

7)  строительство здания, промышленного предприятия или сооружения;

8)  внедрение, улучшение или усовершенствование существующих бизнес-процессов и процедур
        """
    },
    {
        'section': 'Методология проектной деятельности',
        'theory1': """
        Методология управления проектами – это учение об организации продуктивной деятельности человека (организации), которая может быть представлена в виде завершенных циклов, которые называются проектами, и реализуема в определенной временной последовательности по фазам (стадиям, этапам) жизненного цикла.
Задача развития методологии управления проектами заключается в поддержании соответствия методов, способов и стратегий исследования предмета (организация деятельности) современным тенденциям развития организации и экономики в целом.
Методология управления проектами является стандартом ведения проектов от старта до завершения. Она включает в себя:
- конкретные принципы работы: способы оценки сроков, постановки задач, передачи заданий между сотрудниками и отделами, стандарты для совместной работы;
- определённые инструменты управления проектами, например, диаграммы Ганта, Kanban-доски, планировщики;
- способы оценки результатов задач и проекта в целом.
Методология позволяет менеджеру один раз выбрать инструменты и стандарты, создать «конвейер» и потом прогонять проекты по этому конвейеру, чтобы получать предсказуемый результат.
Методологии управление проектами используются везде: от разработки приложений до автомобильной промышленности и строительства космических кораблей. Везде, где есть проект и команда, применяют ту или иную методологию, сочетание нескольких или хотя бы их отдельные элементы.
        """,
        'theory2':  """
                     С проектной деятельностью мы сталкиваемся в своей жизни постоянно. К ней можно отнести многое из того, что мы делаем. От небольших проектов, занимающих дни или недели (например,  организации  дня  рождения  или  встречи  друзей), до  крупных  проектов, продолжающихся месяцы (например, подготовка выпускной работы или книги) или даже годы (например, строительство стадиона).
Необходимо изучить виды проектов и их классификацию, ознакомиться с этапами работы над проектами.
В рамках проектной деятельности результатом проекта может быть:
1) продукт, представляющий собой компонент другого изделия, улучшение изделия или конечное изделие;
2)  услуга или способность предоставлять услугу (например, бизнес-функция, поддерживающая производство или дистрибуцию);
3)  улучшение существующей линейки продуктов или услуг, предпринятых для уменьшения дефектов;
4)  конечный результат или документ (например, исследовательский проект приносит новые знания, которые можно использовать для определения наличия тенденции или пользы какого-либо нового процесса для общества);
5)  разработка или приобретение новой или усовершенствованной информационной системы (оборудование или программное обеспечение);
6)  исследование, результат которого будет надлежащим образом зафиксирован;
7)  строительство здания, промышленного предприятия или сооружения;
8)  внедрение, улучшение или усовершенствование существующих бизнес-процессов и процедур
                     """
        }
]


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    username = message.from_user.username
    coins.append({'username':f"{username}", 'coins': 0})
    print(coins)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_progress[user_id] = 0
    button1 = types.KeyboardButton("Выбрать курс 🤔")
    button2 = types.KeyboardButton("Мини-игра 🎲")
    button3 = types.KeyboardButton("Скиллкоины 🌟")
    keyboard.add(button1, button2, button3)
    bot.send_message(message.chat.id, "Привет!👋\nЯ бот-Проекторий, который поможет тебе обогатиться знаниями!💭\nЗа каждый пройденный курс ты получишь скиллкоины, за которые ты сможешь купить мерч 🖊👕👜\nЛибо можете пройти мини-игру 🎲", reply_markup=keyboard)

def check_kurs(message):
    user_id = message.from_user.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kurs1 = types.KeyboardButton("Основы проектной деятельности")
    keyboard.add(kurs1)
    bot.send_message(message.chat.id, "Выберите курс, который хотите освоить 🤔", reply_markup=keyboard)

def main_task1(message):
    user_id = message.chat.id
    for point in course_data:
        bot.send_message(user_id, f"{point['section']}\n\n{point['theory1']}")
        time.sleep(8)   #  хуйня, нужна кнопка для выброса следующего блока
        bot.send_message(user_id, f"{point['theory2']}")
        time.sleep(10)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    yes = "Да ✅"
    no = "Главное меню 🏘"
    markup.add(yes,no)
    bot.send_message(user_id, "Готовы ли вы пройти тесты?", reply_markup=markup)

def check_tests(message):
    user_id = message.chat.id
    username = message.from_user.username
    bot.send_message(user_id, "https://forms.yandex.ru/u/6701e59a90fa7b46fa27d829/")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Главное меню 🏘"))
    time.sleep(15)    # можно наебывать, надо чтобы как-то ловилось прошел чел или нет
    bot.send_message(user_id, "Поздравляю, вы прошли курс! Вам начислено 100 скиллкоинов! ⭐⭐⭐",reply_markup=markup)    
    for user in coins:
        if user['username'] == username:
            coin = user['coins']
            user['coins'] = user['coins']+100

def main_menu(message):
    user_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_progress[user_id] = 0
    button1 = types.KeyboardButton("Выбрать курс 🤔")
    button2 = types.KeyboardButton("Мини-игра 🎲")
    coin = types.KeyboardButton("Скиллкоины 🌟")
    keyboard.add(button1, button2, coin)
    bot.send_message(message.chat.id, "Вы в главном меню! 🏘", reply_markup=keyboard)

def check_coins(message):
    user_id = message.chat.id
    username = message.from_user.username
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Главное меню 🏘")
    coin = 0
    for user in coins:
        if user['username'] == username:
            coin = user['coins']
    bot.send_message(user_id, f"Ваше кол-во коинов - {coin} ⭐", reply_markup=keyboard)
    
def mini_game(message):
    user_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Главное меню 🏘")
    bot.send_message(user_id, "Составьте 4 слова, которые можно составить из слова «проект»", reply_markup=keyboard)
    
def mini_game_coin(message):
    user_id = message.chat.id
    username = message.from_user.username
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Главное меню 🏘")
    for user in coins:
        if user['username'] == username:
            coin = user['coins']
            user['coins'] = user['coins']+20
    bot.send_message(user_id, "Вы заработали 20 скиллкоинов! ⭐", reply_markup=keyboard)

def mini_game_coin_wrong(message):
    user_id = message.chat.id
    username = message.from_user.username
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Главное меню 🏘")
    bot.send_message(user_id, "Данное слово не подходит 😢", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def func(message):
    word_list = ["копер", "протек", "потек", "покер"]
    guessed_word_list = []
    if message.text  == "Выбрать курс 🤔":
        check_kurs(message)
    elif message.text =="Основы проектной деятельности":
        main_task1(message)
    elif message.text == "Да ✅":
        check_tests(message)
    elif message.text == "Главное меню 🏘":
        main_menu(message)
    elif message.text == "Скиллкоины 🌟":
        check_coins(message)
    elif message.text == "Мини-игра 🎲":
        mini_game(message)
    elif message.text.lower() in word_list:
            mini_game_coin(message)
    elif message.text.lower() not in word_list:
            mini_game_coin_wrong(message)
    # elif message.text.lower() == "копер":
    #     mini_game_coin(message)
    # elif message.text.lower() == "протек":
    #     mini_game_coin(message)
    # elif message.text.lower() == "потек":
    #     mini_game_coin(message)
    # elif message.text.lower() == "покер":
    #     mini_game_coin(message)
    
if __name__ == '__main__':
    bot.polling(none_stop=True)