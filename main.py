import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart


TOKEN = "8837299627:AAHgBPggMASHbOqQQv-OYH5P2WuFkct7K9w"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer(f"مرحباً بك في بوت متجر سهل الجامعي، {message.from_user.full_name}! الخدمة تعمل الآن على مدار الساعة.")

async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
