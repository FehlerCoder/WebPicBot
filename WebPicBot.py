#-*- coding: utf-8 -*-
import telebot
import redis as r
import sys
import urllib
import re
import os
import json
import time
import random
from random import randint
from telebot import types
from time import sleep
reload(sys)
# join us : @FehlerCoder :D
sys.setdefaultencoding("utf-8")
redis = r.StrictRedis(host='localhost', port=6379, db=0)
token = 'TOKEN'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(m):
 redis.sadd('user:bot',m.from_user.id)
 bot.send_message(m.chat.id,'Hi Dear,\nWelcome To WebShot Bot Just Send Site URL To Get Picture of the Site...!\n\nWrited by @FehlerCode')

@bot.message_handler(commands=['stats'])
def stats(m):
  bot.send_message(m.chat.id,'Users: {}'.format(str(redis.scard('user:bot'))))

@bot.message_handler(content_types=['text'])
def webshot(m):
 try:
  if re.match('(ftp|http|https)://(beeg.com|sex.com|pornhub.com|xnxx.com|xxx.com|fuck.com)$',m.text.split()[0]):
   bot.reply_to(m,'Porn Web Sites Is Not Allowed..!')
  else:
   if re.match('(ftp|http|https)://.*$',m.text.split()[0]):
    t = bot.reply_to(m,'Downloading...')
    cid = m.chat.id
    time.sleep(3)
    t2 = bot.edit_message_text(chat_id=cid, message_id=t.message_id, text='Sending....')
    bot.send_chat_action(cid,'upload_photo')
    url = urllib.urlretrieve("https://api.url2img.com/?url={}".format(m.text.split()[0]), "img.jpg")
    bot.send_photo(m.chat.id, open('img.jpg'),caption='Downloaded By: @WebPicBot')
    bot.edit_message_text(chat_id=cid, message_id=t2.message_id, text='Done!')
    os.remove('img.jpg')

   else:
    bot.send_message(m.chat.id,'[{}] Is Not a Link..!\n Example: \nhttps://Google.com'.format(m.text.split()[0]))
 except:
  print 'Err'

@bot.edited_message_handler(content_types=['text'])
def web_edit_shot(m):
 try:
  if re.match('(ftp|http|https)://(beeg.com|sex.com|pornhub.com|xnxx.com|xxx.com|fuck.com)$',m.text.split()[0]):
   bot.reply_to(m,'Porn Web Sites Is Not Allowed..!')
  else:
   if re.match('(ftp|http|https)://.*$',m.text.split()[0]):
    t = bot.reply_to(m,'Downloading...')
    cid = m.chat.id
    time.sleep(3)
    t2 = bot.edit_message_text(chat_id=cid, message_id=t.message_id, text='Sending....')
    bot.send_chat_action(cid,'upload_photo')
    url = urllib.urlretrieve("https://api.url2img.com/?url={}".format(m.text.split()[0]), "img.jpg")
    bot.send_photo(m.chat.id, open('img.jpg'),caption='Downloaded By: WebPicBot!\nJoin us : @FehlerCoder)
    bot.edit_message_text(chat_id=cid, message_id=t2.message_id, text='Done!')
    os.remove('img.jpg')
   else:
    bot.send_message(m.chat.id,'[{}] Is Not a Link..!\n Example: \nhttps://Google.com'.format(m.text.split()[0]))
 except:
  print 'Err'

bot.polling(True)