import asyncio
from telebot.async_telebot import AsyncTeleBot
import aioschedule as schedule
from lessons import schoolschedule as ls

bot = AsyncTeleBot('5306175698:AAGlqVWutT12CYJOZi72lshroxb6oFFJ0Vk')

chat_ids = []
test_ids = []
check_ids = {}

async def mon_1():
    msg = ls.get_lesson('mon', 1)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass    
async def mon_2():
    msg = ls.get_lesson('mon', 2)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def mon_3():
    msg = ls.get_lesson('mon', 3)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def mon_4():
    msg = ls.get_lesson('mon', 4)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def mon_5():
    msg = ls.get_lesson('mon', 5)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def mon_6():
    msg = ls.get_lesson('mon', 6)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def mon_7():
    msg = ls.get_lesson('mon', 7)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def mon_8():
    msg = ls.get_lesson('mon', 8)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass

async def tue_1():
    msg = ls.get_lesson('tue', 1)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def tue_2():
    msg = ls.get_lesson('tue', 2)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def tue_3():
    msg = ls.get_lesson('tue', 3)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def tue_4():
    msg = ls.get_lesson('tue', 4)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def tue_5():
    msg = ls.get_lesson('tue', 5)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def tue_6():
    msg = ls.get_lesson('tue', 6)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def tue_7():
    msg = ls.get_lesson('tue', 7)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass

async def wed_1():
    msg = ls.get_lesson('wed', 1)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def wed_2():
    msg = ls.get_lesson('wed', 2)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def wed_3():
    msg = ls.get_lesson('wed', 3)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def wed_4():
    msg = ls.get_lesson('wed', 4)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def wed_5():
    msg = ls.get_lesson('wed', 5)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def wed_6():
    msg = ls.get_lesson('wed', 6)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def wed_7():
    msg = ls.get_lesson('wed', 7)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def wed_8():
    msg = ls.get_lesson('wed', 8)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass

async def thu_1():
    msg = ls.get_lesson('thu', 1)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def thu_2():
    msg = ls.get_lesson('thu', 2)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def thu_3():
    msg = ls.get_lesson('thu', 3)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def thu_4():
    msg = ls.get_lesson('thu', 4)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def thu_5():
    msg = ls.get_lesson('thu', 5)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def thu_6():
    msg = ls.get_lesson('thu', 6)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def thu_7():
    msg = ls.get_lesson('thu', 7)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass

async def fri_1():
    msg = ls.get_lesson('fri', 1)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def fri_2():
    msg = ls.get_lesson('fri', 2)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def fri_3():
    msg = ls.get_lesson('fri', 3)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def fri_4():
    msg = ls.get_lesson('fri', 4)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def fri_5():
    msg = ls.get_lesson('fri', 5)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def fri_6():
    msg = ls.get_lesson('fri', 6)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
async def fri_7():
    msg = ls.get_lesson('fri', 7)
    if len(chat_ids):
        for id in chat_ids:
            await bot.send_message(id, msg)
    else:
        pass
    
async def test_day():
    msg = 'test'
    if len(test_ids):
        for id in test_ids:
            await bot.send_message(id, msg)
    else:
        pass

async def set_monday():
    schedule.every().monday.at('9:00').do(mon_1)
    schedule.every().monday.at('9:40').do(mon_2)
    schedule.every().monday.at('10:20').do(mon_3)
    schedule.every().monday.at('11:00').do(mon_4)
    schedule.every().monday.at('12:00').do(mon_5)
    schedule.every().monday.at('12:40').do(mon_6)
    schedule.every().monday.at('13:20').do(mon_7)
    schedule.every().monday.at('14:00').do(mon_8)
async def set_tuesday():
    schedule.every().tuesday.at('9:00').do(tue_1)
    schedule.every().tuesday.at('9:40').do(tue_2)
    schedule.every().tuesday.at('10:20').do(tue_3)
    schedule.every().tuesday.at('11:00').do(tue_4)
    schedule.every().tuesday.at('12:00').do(tue_5)
    schedule.every().tuesday.at('12:40').do(tue_6)
    schedule.every().tuesday.at('13:20').do(tue_7)
async def set_wednesday():
    schedule.every().wednesday.at('9:00').do(wed_1)
    schedule.every().wednesday.at('9:40').do(wed_2)
    schedule.every().wednesday.at('10:20').do(wed_3)
    schedule.every().wednesday.at('11:00').do(wed_4)
    schedule.every().wednesday.at('12:00').do(wed_5)
    schedule.every().wednesday.at('12:40').do(wed_6)
    schedule.every().wednesday.at('13:20').do(wed_7)
    schedule.every().wednesday.at('14:00').do(wed_8)   
async def set_thursday():
    schedule.every().thursday.at('9:00').do(thu_1)
    schedule.every().thursday.at('9:40').do(thu_2)
    schedule.every().thursday.at('10:20').do(thu_3)
    schedule.every().thursday.at('11:00').do(thu_4)
    schedule.every().thursday.at('12:00').do(thu_5)
    schedule.every().thursday.at('12:40').do(thu_6)
    schedule.every().thursday.at('13:20').do(thu_7)   
async def set_friday():
    schedule.every().friday.at('9:00').do(fri_1)
    schedule.every().friday.at('9:40').do(fri_2)
    schedule.every().friday.at('10:20').do(fri_3)
    schedule.every().friday.at('11:00').do(fri_4)
    schedule.every().friday.at('12:00').do(fri_5)
    schedule.every().friday.at('12:40').do(fri_6)
    schedule.every().friday.at('13:20').do(fri_7)

async def set_test():
    schedule.every(15).seconds.do(test_day)

# ----------------------------start/stop-------------------------------
@bot.message_handler(commands=['start_notify'])
async def start_notify(msg):

    if msg.chat.id not in chat_ids:
        chat_ids.append(msg.chat.id)
        await bot.send_message(msg.chat.id, 'Нагадування почалося!')
    else:
        await bot.send_message(msg.chat.id, 'Нагадування вже почалося!')

    await set_monday()
    await set_tuesday()
    await set_wednesday()
    await set_thursday()
    await set_friday()

@bot.message_handler(commands=['stop'])
async def stop_notify(msg):
    
    if msg.chat.id in chat_ids :
        chat_ids.remove(msg.chat.id)
        bot.send_message(msg.chat.id, 'Нагадування зупинилося!')
    else:
        bot.send_message(msg.chat.id, 'Нагадування не було почате!')
      
# ------------------------------test start/stop--------------------------
  
@bot.message_handler(commands=['test_start'])
async def test_notify(msg):
    
    if msg.chat.id not in test_ids:
        test_ids.append(msg.chat.id)
        await bot.send_message(msg.chat.id, 'test Нагадування почалося!')
        await set_test()
    else:
        await bot.send_message(msg.chat.id, 'test Нагадування вже почалося!')   
    
 

@bot.message_handler(commands=['test_stop'])
async def stop_notify(msg):

    if msg.chat.id in test_ids:
        test_ids.remove(msg.chat.id)
        await bot.send_message(msg.chat.id, 'test Нагадування зупинилося!')
    else:
        await bot.send_message(msg.chat.id, 'test Нагадування не було почате!')

# -------------------------------------------------------------------------------

async def scheduler():
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(bot.infinity_polling(), scheduler())

if __name__ == '__main__':
    asyncio.run(main())