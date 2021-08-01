from telegram.ext import Updater,MessageHandler,Filters

def lighton(bot,update):
  chat_id=bot.message.chat_id
  path=''
  update.bot.sendPhoto(chat_id=chat_id,photo='https://static.scientificamerican.com/sciam/cache/file/2B38DE31-C1D3-4339-8808D61972976EE4.jpg')
  bot.message.reply_text("the light is on ")
  from Adafruit_IO import Client
  aio = Client('anas1605', 'aio_oMzi613gjTj8LduHxpt8iDwWmMAq')
  aio.send('light', 1)
  data = aio.receive('light')
  print('Received value: {0}'.format(data.value))

def lightoff(bot,update):
  chat_id=bot.message.chat_id
  path=''
  update.bot.sendPhoto(chat_id=chat_id,photo='https://ak.picdn.net/shutterstock/videos/16051507/thumb/1.jpg')
  bot.message.reply_text("the light is off")
  from Adafruit_IO import Client
  aio = Client('anas1605', 'aio_oMzi613gjTj8LduHxpt8iDwWmMAq')
  aio.send('light', 0)
  data = aio.receive('light')
  print('Received value: {0}'.format(data.value))

def fanon(bot,update):
  chat_id=bot.message.chat_id
  path=''
  update.bot.sendPhoto(chat_id=chat_id,photo="https://previews.123rf.com/images/llstock/llstock1909/llstock190900033/130060912-a-working-ceiling-fan-on-a-white-ceiling-close-up-with-blurred-fan-blades-three-lamps-daytime-.jpg")
  bot.message.reply_text("the fan is on")
  from Adafruit_IO import Client
  aio = Client('anas1605', 'aio_oMzi613gjTj8LduHxpt8iDwWmMAq')
  aio.send('fan', 1)
  data = aio.receive('fan')
  print('Received value: {0}'.format(data.value))

def fanoff(bot,update):
  chat_id=bot.message.chat_id
  path=''
  update.bot.sendPhoto(chat_id=chat_id,photo='https://images-na.ssl-images-amazon.com/images/I/31fec2V1l4L._SX425_.jpg')
  bot.message.reply_text("the fan is off")
  from Adafruit_IO import Client
  aio = Client('anas1605', 'aio_oMzi613gjTj8LduHxpt8iDwWmMAq')
  aio.send('fan', 0)
  data = aio.receive('fan')
  print('Received value: {0}'.format(data.value))

def greeting(bot,update):
  bot.message.reply_text("hi, what can i do for you?")
  bot.message.reply_text("commands available only for fan and light now")

def demo(bot,update):
  a=bot.message.text
  a=a.lower()
  a=a.split()
  if 'light' in a and 'on'in a:
   lighton(bot,update)
  elif 'light' in a and 'off'in a:
    lightoff(bot,update)
  elif 'fan' in a and 'on'in a:
    fanon(bot,update)
  elif 'fan' in a and 'off'in a:
    fanoff(bot,update) 
  elif 'hi' in a or 'hello'in a:
    greeting(bot,update)
  else:
    bot.message.reply_text("INVALID COMMAND")

  
  

BOT_TOKEN='1933670922:AAFgBvg1ME746QpL0UQYiQVufpoaII2TYWo'
u=Updater(BOT_TOKEN,use_context=True)
dp=u.dispatcher
dp.add_handler(MessageHandler(Filters.text,demo))
u.start_polling()
u.idle()


  
  

BOT_TOKEN='1933670922:AAFgBvg1ME746QpL0UQYiQVufpoaII2TYWo'
u=Updater(BOT_TOKEN,use_context=True)
dp=u.dispatcher
dp.add_handler(MessageHandler(Filters.text,demo))
u.start_polling()
u.idle()



