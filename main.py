import time

import telebot
from telebot import types

# Токен бота
BOT_TOKEN = '6752871267:AAEHKd3C-fYcrSBz-uJkE5kP2tAQkN7M9XI'
user_states = {}
sleepTime = 0.5
# Создание бота
bot = telebot.TeleBot(BOT_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Создание клавиатуры
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Добавление кнопок
    button_safety = types.KeyboardButton('🛡️ Советы по безопасности')
    button_passwords = types.KeyboardButton('🔐 Проверка паролей')
    button_stats = types.KeyboardButton('📊 Статистики и советы')
    keyboard.add(button_safety, button_passwords, button_stats)

    # Отправка сообщения с клавиатурой
    bot.send_message(message.chat.id, 'Привет! Выберите, что вас интересует:', reply_markup=keyboard)

# Обработчик нажатия кнопки "Советы по безопасности"
@bot.message_handler(func=lambda message: message.text == '🛡️ Советы по безопасности')
def safety(message):
    # Создание клавиатуры
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Добавление кнопок
    button_vk = types.KeyboardButton('🔒 ВКонтакте')
    button_telegram = types.KeyboardButton('🔐 Telegram')
    button_instagram = types.KeyboardButton('📸 Instagram')
    button_youTube = types.KeyboardButton('🎥 YouTube')
    button_twitter = types.KeyboardButton('🐦 Twitter')
    button_back = types.KeyboardButton('⬅️ Назад')
    keyboard.add(button_vk, button_telegram, button_instagram, button_youTube, button_twitter, button_back)

    user_states[message.from_user.id] = 'safety'
    # Отправка сообщения с клавиатурой
    bot.send_message(message.chat.id, 'Выберите социальную сеть:', reply_markup=keyboard)



# ВКонтакте
@bot.message_handler(func=lambda message: message.text == '🔒 ВКонтакте')
def vk(message):
    vk_tips = [
        "🔐 Используйте надежный пароль и не делитесь им ни с кем.",
        "📲 Включите двухфакторную аутентификацию.",
        "❌ Не переходите по ссылкам из сомнительных источников.",
        "🛡️ Будьте осторожны с приложениями, которые запрашивают доступ к вашим данным.",
        "🙅‍♂️ Не публикуйте личную информацию на своей странице.",
        "🔒 Сделайте свой профиль приватным.",
        "🚫 Не добавляйте в друзья незнакомых людей.",
        "🎣 Будьте осторожны с фишинговыми атаками."
    ]
    vk_tips_issue = [
        "🔑 Если вы забыли пароль, вы можете восстановить его с помощью вашего номера телефона или электронной почты.",
        "🆘 Если ваш аккаунт был взломан, вы можете обратиться в службу поддержки ВКонтакте."
    ]

    bot.send_message(message.chat.id, "ВКонтакте:")
    for tip in vk_tips:
        time.sleep(sleepTime)
        bot.send_message(message.chat.id, tip)
    bot.send_message(message.chat.id, "Советы по устранению проблем:")
    for tip in vk_tips_issue:
        time.sleep(sleepTime)
        bot.send_message(message.chat.id, tip)

# Инстаграм
@bot.message_handler(func=lambda message: message.text == '📸 Instagram')
def instagram(message):
    instagram_tips = [
        "🔐 Используйте сложный пароль и меняйте его регулярно.",
        "📲 Включите двухфакторную аутентификацию.",
        "🔒 Ограничьте доступ к вашему аккаунту с помощью приватного аккаунта.",
        "🚫 Будьте осторожны с подпиской на непроверенные аккаунты и приложения.",
        "🤐 Не делитесь личной информацией, такой как адрес и номер телефона, публично."
    ]
    instagram_tips_issue = [
        "🔑 Если у вас проблемы с доступом к аккаунту, воспользуйтесь опцией восстановления пароля в приложении."
    ]

    bot.send_message(message.chat.id, "Instagram:")
    for tip in instagram_tips:
        time.sleep(sleepTime)
        bot.send_message(message.chat.id, tip)
    bot.send_message(message.chat.id, "Советы по устранению проблем:")
    for tip in instagram_tips_issue:
        time.sleep(sleepTime)
        bot.send_message(message.chat.id, tip)


# Телеграм
@bot.message_handler(func=lambda message: message.text == '🔐 Telegram')
def telegram(message):
    telegram_tips = [
        "🔐 Включите двухфакторную аутентификацию.",
        "🚫 Не доверяйте непроверенным ботам и приложениям.",
        "🤐 Не передавайте свой код подтверждения никому.",
        "⚠️ Будьте осторожны с присоединением к публичным группам и каналам."
    ]
    telegram_tips_issue = [
        "🆘 Если у вас проблемы с безопасностью, вы можете связаться с службой поддержки Телеграм."
    ]

    bot.send_message(message.chat.id, "Telegram:")
    for tip in telegram_tips:
        time.sleep(sleepTime)
        bot.send_message(message.chat.id, tip)
    bot.send_message(message.chat.id, "Советы по устранению проблем:")
    for tip in telegram_tips_issue:
        time.sleep(sleepTime)
        bot.send_message(message.chat.id, tip)


# YouTube
@bot.message_handler(func=lambda message: message.text == '🎥 YouTube')
def youtube(message):
    youtube_tips = [
        "Используйте надежный пароль для вашего аккаунта. 🔐",
        "Настройте двухфакторную аутентификацию для дополнительной защиты. 📲",
        "Будьте осторожны с личной информацией в комментариях и видео. 🚫",
        "Не отвечайте на подозрительные запросы от непроверенных аккаунтов. ❌",
        "Не делитесь личной информацией, такой как адрес или номер телефона, публично. 🤐"
    ]
    youtube_tips_issue = [
        "Если у вас возникли проблемы с безопасностью аккаунта, обратитесь в службу поддержки YouTube. 🆘"
    ]

    bot.send_message(message.chat.id, "YouTube:")
    for tip in youtube_tips:
        time.sleep(sleepTime)
        bot.send_message(message.chat.id, tip)
    bot.send_message(message.chat.id, "Советы по устранению проблем:")
    for tip in youtube_tips_issue:
        time.sleep(sleepTime)
        bot.send_message(message.chat.id, tip)


# Twitter
@bot.message_handler(func=lambda message: message.text == '🐦 Twitter')
def twitter(message):
    twitter_tips = [
        "Используйте сложный пароль и регулярно меняйте его. 🔐",
        "Включите двухфакторную аутентификацию для дополнительной безопасности. 📲",
        "Будьте осторожны с кликами на сокращенные ссылки и подозрительные аккаунты. 🚫",
        "Не делитесь личной информацией, такой как домашний адрес или номер телефона, в открытых твитах. 🤐"
    ]
    twitter_tips_issue = [
        "Если у вас возникли проблемы с безопасностью аккаунта, обратитесь в службу поддержки Twitter. 🆘"
    ]

    bot.send_message(message.chat.id, "Twitter:")
    for tip in twitter_tips:
        time.sleep(sleepTime)
        bot.send_message(message.chat.id, tip)
    bot.send_message(message.chat.id, "Советы по устранению проблем:")
    for tip in twitter_tips_issue:
        time.sleep(sleepTime)
        bot.send_message(message.chat.id, tip)


@bot.message_handler(func=lambda message: message.text == '⬅️ Назад')
def back(message):
    # Возвращаем пользователя к основному меню
    start(message)

    # Удаляем состояние пользователя
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

statistics_data = {
    'Общая статистика': (
        '📊 Всего зарегистрировано пользователей - 1 млрд.\n'
        '🌐 Активных пользователей в день - 500 млн.'
    ),
    'Фишинговые атаки': '🎣 За последний месяц зарегистрировано 100 тыс. попыток фишинга.',
    'Случаи взлома аккаунтов': '🚨 Ежедневно регистрируется 10 тыс. случаев взлома аккаунтов.',
    'Использование двухфакторной аутентификации': '🔐 Только 30% пользователей используют двухфакторную аутентификацию.',
}


# Обработчик нажатия кнопки "Статистики и советы"
@bot.message_handler(func=lambda message: message.text == '📊 Статистики и советы')
def stats(message):
    # Создание клавиатуры с кнопками тематик
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for category in statistics_data.keys():
        keyboard.add(types.KeyboardButton(category))
    keyboard.add(types.KeyboardButton("⬅️ Назад"))
    user_states[message.from_user.id] = 'safety'

    # Добавление эмодзи и форматирование сообщения
    introduction_message = (
        "📈 Добро пожаловать в раздел статистик и советов! 📈\n\n"
        "Выберите тематику для просмотра статистики:"
    )

    # Отправка сообщения с клавиатурой и введением
    bot.send_message(message.chat.id, introduction_message, reply_markup=keyboard)


# Обработчик выбора категории статистики
@bot.message_handler(func=lambda message: message.text in statistics_data.keys())
def show_statistics(message):
    category = message.text
    statistics = statistics_data.get(category, '❌ Нет данных для выбранной тематики.')
    bot.send_message(message.chat.id, f'📊 Статистика по теме "{category}":\n\n{statistics}')


# Обработчик нажатия кнопки "Проверка паролей"
@bot.message_handler(func=lambda message: message.text == '🔐 Проверка паролей')
def passwords(message):
    bot.send_message(message.chat.id, '🔒 Введите пароль, который хотите проверить:')


@bot.message_handler(func=lambda message: True)
def check_password(message):
    user_password = message.text
    bot.send_message(message.chat.id, check_password_strength(user_password))

def check_password_strength(password):
    if len(password) < 8:
        return "❌ Пароль слишком короткий. Минимальная длина: 8 символов."

    if not any(char.isupper() for char in password):
        return "❌ Добавьте хотя бы одну заглавную букву в пароль."

    if not any(char.isdigit() for char in password):
        return "❌ Добавьте хотя бы одну цифру в пароль."

    special_characters = "!@#$%^&*()-=_+[]{}|;:'\"<>,.?/"
    if not any(char in special_characters for char in password):
        return "❌ Добавьте хотя бы один специальный символ в пароль."

    return "✅ Пароль отличный! 👍"





# Запуск бота
bot.polling()
