import telebot 
import random
from telebot import types
from datetime import date , datetime
from qrcode import make
from khayyam import JalaliDatetime

bot = telebot.TeleBot("!")

@bot.message_handler(commands='start')
def start(message):
    bot.send_message(message.chat.id , "Welcome to my Bot \n/game play a guessing game\n/qrcode turn a text into qrcode\n/max find the biggest number in an array\n/argmax find the index of the biggest number in an array\n/age enter your birthday and see your age!\n/voice turns text into voice")

@bot.message_handler(commands='game')
def game(message):
    guess = bot.reply_to(message," Guess a number (1-100) ")
    global num
    num = random.randint(1,100)
    bot.register_next_step_handler(guess , number)

def number(message):
    
    if int(message.text) == num:
        bot.reply_to(message, "You Win !")
        bot.send_message(message.chat.id , "Welcome to my Bot \n/game play a guessing game")
    elif int(message.text) > num:
        guess = bot.reply_to(message, "lower")
        bot.register_next_step_handler(guess , number)
    elif int(message.text) < num:        
        guess = bot.reply_to(message, "higher")
        bot.register_next_step_handler(guess , number)


@bot.message_handler(commands='max')
def Max(message):
    arr = bot.reply_to(message , "Plaese enter an array of numbers seprating each number with a space (example:2,4,5,6,10)")
    bot.register_next_step_handler(arr , findMax )

def findMax(message) :
    arr = message.text.split(',')
    maxNum = max(arr)
    bot.send_message(message.chat.id ,  maxNum)

@bot.message_handler(commands='argmax')
def MaxIndex(message):
    arr = bot.reply_to(message , "Plaese enter an array of numbers seprating each number with a space (example:2,4,5,6,10)")
    bot.register_next_step_handler(arr , findMaxIndex )

def findMaxIndex(message) :
    arr = message.text.split(',')
    maxNumIndex = arr.index(max(arr))
    bot.send_message(message.chat.id ,  maxNumIndex)

@bot.message_handler(commands=['qrcode'])
def qrCode(message):
    qr = bot.reply_to(message.chat.id , 'Enter your text: ')
    bot.register_next_step_handler(qr , Makeqr)

def Makeqr(message):
    qr = make(message.text)
    qr.save('qrcode.png')
    qr = open('qrcode.png' , 'rb')
    bot.send_photo(message.chat.id , qr)


@bot.message_handler(commands='age')
def BdDate(message):
    bd = bot.reply_to(message.chat.id , 'Enter your birthday (example : 1400/9/9)')
    bot.register_next_step_handler(bd , age)

def age(message):
    bd = message.text.split("/")
    age = JalaliDatetime.now() - JalaliDatetime(bd[0] , bd[1] , bd[2] )
    bot.send_message(message.chat.id , age )

bot.infinity_polling()


