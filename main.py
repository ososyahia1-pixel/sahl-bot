import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiohttp import web

# ضع توكن البوت الخاص بك هنا
TOKEN = "YOUR_BOT_TOKEN_HERE"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer(f"مرحباً بك في بوت متجر سهل الجامعي، {message.from_user.full_name}! الخدمة تعمل الآن.")

async def start_bot():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

# صفحة وهمية لإرضاء سيرفرات Render
async def handle_ping(request):
    return web.Response(text="Bot is running perfectly!")

async def main() -> None:
    # إعداد السيرفر الوهمي
    app = web.Application()
    app.router.add_get('/', handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    
    # الحصول على المنفذ الذي يطلبه Render
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

    # تشغيل البوت الأساسي
    await start_bot()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
