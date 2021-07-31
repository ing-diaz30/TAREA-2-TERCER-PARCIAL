import time
import telebot
from telebot import types

TOKEN = '1904037036:AAF7oZXhHyL5Pl4EzsP1ICJfa2SDmZBX0zE'

knownUsers = [] 
userStep = {}  

commands = { 
    'start'         : 'Iniciar el bot\n\n',
    'help'          : 'Muestra los comandos disponibles\n\n',
    'conversion'    : 'Muestra las conversiones disponibles'
}

imageSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)  
imageSelect.add('Gigabytes a Megabytes', 'Terabytes a Gigabytes','Megabytes a Kilobytes','Bytes a Bits')

hideBoard = types.ReplyKeyboardRemove()  

def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("Nuevo usuarios detectado, pero no ha usado \"/start\" ")
        return 0

def listener(messages):
    for m in messages:
        if m.content_type == 'text':0
    print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)     

@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers: 
        knownUsers.append(cid)  
        userStep[cid] = 0 
        
        bot.send_message(cid, 'Bienvenido Conversion Unidades Informática')
        bot.send_chat_action(cid, 'typing')  
        time.sleep(1)
        bot.send_chat_action(cid, 'typing')  
        time.sleep(1)
        command_help(m) 
    else:
        bot.send_message(cid, "Ya usaste el comando /start, usa el comando /help para visualizar más comandos")

@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "Selecciona el comando de tu interes:\n\n\n"
    for key in commands: 
            help_text += "/" + key + ": "
            help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  

@bot.message_handler(commands=['conversion'])
def command_image(m):
    cid = m.chat.id
    bot.send_message(cid, "Selecciona la tecla de tu preferencia ", reply_markup=imageSelect)  
    userStep[cid] = 1 

@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1)
def msg_image_select(m):
    cid = m.chat.id
    text = m.text
    bot.send_chat_action(cid, 'typing')
    time.sleep(1)
    bot.send_chat_action(cid, 'typing')
    time.sleep(1)
    bot.send_chat_action(cid, 'typing')
    time.sleep(1)

    if text == 'Gigabytes a Megabytes':
        bot.send_message(cid, "A continuacíon se te enviara una imagen de la formula Gigabytes a Megabytes")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('GB_a_MB.png', 'rb'),
                       reply_markup=hideBoard)  
        time.sleep(3)
        bot.send_message(cid, "Selecciona el comando /conversion para realizar otra consulta o /help para otros comandos")
        userStep[cid] = 0 

    elif text == 'Terabytes a Gigabytes':
        bot.send_message(cid, "A continuacíon se te enviara una imagen de la formula Terabytes a Gigabytes")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('TB_a_GB.png','rb'),
                       reply_markup=hideBoard)  
        time.sleep(3)
        bot.send_message(cid, "Selecciona el comando /conversion para realizar otra consulta o /help para otros comandos")
        userStep[cid] = 0  

    elif text == 'Megabytes a Kilobytes':
        bot.send_message(cid, "A continuacíon se te enviara una imagen de la formula Megabytes a Kilobytes")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('MB_a_KB.png','rb'),
                       reply_markup=hideBoard)  
        time.sleep(3)
        bot.send_message(cid, "Selecciona el comando /conversion para realizar otra consulta o /help para otros comandos")
        userStep[cid] = 0

    elif text == 'Bytes a Bits':
        bot.send_message(cid, "A continuacíon se te enviara una imagen de la formula Bytes a Bits")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open("B_a_BITS.png","rb"),
                       reply_markup=hideBoard)  
        time.sleep(3)
        bot.send_message(cid, "Selecciona el comando /conversion para realizar otra consulta o /help para otros comandos")
        userStep[cid] = 0   
    else:
        bot.send_message(m.chat.id, "No entiendo el texto:\"" + m.text + "\"\nIntenta usar /help para visualizar la lista de comandos disponibles")
        bot.send_message(cid, "Vamos, intentalo de nuevo. ")

bot.polling()