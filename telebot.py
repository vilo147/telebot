import requests
import telebot
def get_fox():
    
    response=requests.get('https://randomfox.ca/floof/').json()
    return response["image"]
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
TOKEN="1193716664:AAEqEQ4_geLomHLVMFaGhdnIH1XoyHtVkgA"
bot=telebot.TeleBot(TOKEN)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

keyboard.add(KeyboardButton("Calculate"))

keyboard.add(KeyboardButton("Activity"))

keyboard.add(KeyboardButton("University"))

val=0
print(val)
@bot.message_handler(commands=["help","start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "Lets start! This bot was created by Egupec Vladislave. It need only for pastimes and it can do many things.  you can click any button from keyboard.", reply_markup=keyboard)
@bot.message_handler(regexp=r"Calculate")
def say_hello(message):
    global val
    val=1
    bot.send_message(message.chat.id, "Write your example in a line with whitespace(2 + 1)")
    @bot.message_handler(regexp=r'\d \W{1} \d')
    def calculate(message):
            global val
            if(val==1):
                try:
                    f,c,s=map(str,message.text.split())
                    if(c=="+"):
                        bot.send_message(message.chat.id,int(f)+int(s))
                    elif(c=="-"):
                        bot.send_message(message.chat.id,int(f)-int(s))
                    elif(c=="*"):
                       bot.send_message(message.chat.id,int(f)*int(s))
                    elif(c=="/"):
                        bot.send_message(message.chat.id,int(f)/int(s)) 
                    val=0
                    print(val)
                except ZeroDivisionError:
                   bot.send_message(message.chat.id, "I'm sorry. I think you'r example have a mistake, so I'll give you a fox image")
                   bot.send_photo(message.chat.id, get_fox())
            bot.send_message(message.chat.id, "Try somethink else or click on button again")
@bot.message_handler(func=lambda s: "Activity" in s.text)
def give_act(message):
    act=requests.get('https://www.boredapi.com/api/activity').json()
    print(act)
    bot.send_message(message.chat.id, f"{act['activity']}, its '{act['type']}' activity which you can do easely")
@bot.message_handler(regexp=r"University")
def University(message):
    global val
    val=2
    bot.send_message(message.chat.id, "Choose a country")
    @bot.message_handler(regexp=r'\w')
    def getUniv(message):
            global val
            if(val==2):
                params={
                    "country":message.text
                }
                find=requests.get('http://universities.hipolabs.com/search',params).json()
                print(find)
                try:
                    for i in range(5):
                      bot.send_message(message.chat.id, find[i]['name'])
                    val=0
                except:
                    bot.send_message(message.chat.id, "I'm sorry. I dont have that country in my database, so I'll give you a fox image")
                    bot.send_photo(message.chat.id, get_fox())
bot.infinity_polling()