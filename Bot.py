import telebot
from telebot import types

TOKEN = "ТВОЙ_ТОКЕН_ОТСЮДА_ИЗ_BOTFATHER"

bot = telebot.TeleBot(TOKEN)

# --- Главное меню ---
def main_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        types.KeyboardButton("🏋️ Тренировки"),
        types.KeyboardButton("🍗 Питание"),
        types.KeyboardButton("💊 Спортпит")
    )
    return kb

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(
        msg.chat.id,
        "Привет! Я твой фитнес-бот 💪\nВыбери, что тебя интересует:",
        reply_markup=main_menu()
    )

# --- Обработка кнопок ---
@bot.message_handler(func=lambda m: True)
def handle(msg):
    if msg.text == "🏋️ Тренировки":
        bot.send_message(msg.chat.id, "Вот твои упражнения 🔥")
    elif msg.text == "🍗 Питание":
        bot.send_message(msg.chat.id, "Советы по питанию 🥗")
    elif msg.text == "💊 Спортпит":
        bot.send_message(msg.chat.id, "Информация о добавках 💊")
    else:
        bot.send_message(msg.chat.id, "Не понял, выбери пункт меню.")

bot.infinity_polling()
