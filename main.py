import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiohttp import web

TOKEN = "8837299627:AAHgBPggMASHbOqQQv-OYH5P2WuFkct7K9w"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    text = f"مرحباً بك في بوت متجر سهل الجامعي، {message.from_user.full_name}! الخدمة تعمل الآن."
    await message.answer(text)

async def start_bot():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

async def handle_ping(request):
    return web.Response(text="Bot is running perfectly!")

async def main() -> None:
    app = web.Application()
    app.router.add_get('/', handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

    await start_bot()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
