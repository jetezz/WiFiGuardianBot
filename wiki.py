from settings import bot

#control de comandos
@bot.message_handler(commands=['start'])
def start_count(message):
    bot.reply_to(message, "Hello, I'm a Telegram Bot. I can help you with your daily tasks.")
  

#Iteraciones
@bot.message_handler(commands=['count'])
def iteraciones(message):
    bot.reply_to(message, "manda un siguiente mensaje para interactuar")
    bot.register_next_step_handler(message,interative_function)

def interative_function(message):
    words = message.text.split()
    bot.reply_to(message,f"el texto tiene {len(words)} palabras")

#Mensajes
@bot.message_handler(content_types=['text'])
def echo(message):
    if(message.text.lower() == "hola"):
        bot.reply_to(message, "pa ti mi cola")
    else:
        bot.reply_to(message, message.text)

#Iteraciones
@bot.message_handler(commands=['count'])
def iteraciones(message):
    bot.reply_to(message, "manda un siguiente mensaje para interactuar")
    bot.register_next_step_handler(message,interative_function)

def interative_function(message):
    words = message.text.split()
    bot.reply_to(message,f"el texto tiene {len(words)} palabras")