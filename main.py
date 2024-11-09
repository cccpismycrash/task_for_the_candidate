import asyncio
import logging
from aiogram import Bot, Dispatcher 
from config_reader import config
from aiogram.types import FSInputFile
from aiogram.types import InputMediaPhoto
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from processing import make_pic

TEST_GROUP_ID = '@teatingforbor'

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()

make_pic()

async def send_gragh():
    async with Bot(token=config.bot_token.get_secret_value()) as bot:
        await bot.send_media_group(chat_id=TEST_GROUP_ID, media=[InputMediaPhoto(type='photo', media=FSInputFile('/result.png'), caption='text')])


async def main():

    await send_gragh()

if __name__ == '__main__':
    scheduler = AsyncIOScheduler()
    # scheduler.add_job(send_gragh, 'interval', seconds=3)
    scheduler.add_job(send_gragh, 'cron', day_of_week='mon-sun', hour=12, minute=00, end_date='2025-10-13')

    scheduler.start()

    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass