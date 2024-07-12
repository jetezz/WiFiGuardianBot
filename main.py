import threading
import time

from service_wifi_checker import check_wifi_connection
from telebot import types
from settings import bot
from service_fetch import States

# ESTADO
is_counting = False
url = "http://185.61.207.234:55291/info"
time_between_checks = 5

# FUNCIONES PARA MODIFICAR ESTADO
@bot.message_handler(commands=['url'])
def iteraciones(message):
    bot.reply_to(message, "introduce la url de la api")
    bot.register_next_step_handler(message,change_url)

def change_url(message):
    global url
    url = message.text
    bot.reply_to(message,f"la nueva url es {url}")

@bot.message_handler(commands=['seconds'])
def iteraciones(message):
    bot.reply_to(message, "introduce los segundos entre las peticiones")
    bot.register_next_step_handler(message,change_time)

def change_time(message):
    global time_between_checks
    time_between_checks = int(message.text)
    bot.reply_to(message,f"el nuevo tiempo es {time_between_checks}")

# FUNCION PRINCIPAL
def counting(chat_id):
    global url,time_between_checks 
    while is_counting:        
        
          
        response = check_wifi_connection(url)
        if response == States.OK:
            print (response)
            time.sleep(time_between_checks)
            continue

        if response == States.REQUEST_ERROR:    
            bot.send_message(chat_id, "Error en la petición ⚠️")
        if response == States.TIMEOUT_ERROR:
            bot.send_message(chat_id, "Error de tiempo ⚠️")
        if response == States.SERVIDOR_ERROR:
            bot.send_message(chat_id, "Error en el servidor ⚠️")
        time.sleep(time_between_checks)


# Comando start modificado para enviar un teclado personalizado automáticamente
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Crear un nuevo teclado personalizado
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    # Añadir botones al teclado
    button_start = types.KeyboardButton("Start Counting")
    button_stop = types.KeyboardButton("Stop Counting")
    markup.add(button_start, button_stop)
    bot.send_message(message.chat.id, "Welcome! I'm your Telegram Bot. Use the buttons below to start or stop counting.", reply_markup=markup)

# Manejador para iniciar y detener el conteo basado en el texto del mensaje
@bot.message_handler(func=lambda message: message.text in ["Start Counting", "Stop Counting"])
def handle_message(message):
    global is_counting
    if message.text == "Start Counting":
        if not is_counting:
            is_counting = True
            bot.send_message(message.chat.id, "Counting started!")
            t = threading.Thread(target=counting, args=(message.chat.id,))
            t.start()
        else:
            bot.send_message(message.chat.id, "Counting is already running!")
    elif message.text == "Stop Counting":
        if is_counting:
            is_counting = False
            bot.send_message(message.chat.id, "Counting stopped!")
        else:
            bot.send_message(message.chat.id, "Counting is not active!")
   

bot.polling()
