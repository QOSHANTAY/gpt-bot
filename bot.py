from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
import logging
import asyncio,time
from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command
from reg import get_response


from aiogram.client.session.aiohttp import AiohttpSession

session = AiohttpSession(proxy = "http://proxy.server:3128/")
api = '7847354831:AAFsPpB2xoC8mJragwbhCAS2Y27KUDDmOXI'
bot = Bot(api,session=session)
dp=Dispatcher()

@dp.message(Command('start'))
async def send_hello(sms:types.Message):
    await sms.answer(text=f'Welcome {sms.from_user.first_name}')
    

@dp.message()
async def send_answer(sms:types.Message):
    a = await sms.answer_sticker(sticker = 'CAACAgIAAxkBAAEOAqBnzBSy2Cnau0Rk6w2Taidi2FyRUwACTgEAAhZCawpt1RThO2pwgjYE')
    juwap = await get_response(question=sms.text)
    await a.delete()
    await sms.answer(text = juwap)

async def main():
    await dp.start_polling(bot)


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
