from aiogram import Router, types
from aiogram.types import Message

router = Router()

@router.message(commands=["start"])
async def cmd_start(message: Message):
    await message.answer("👋 Привет! Введите событие, которое вы только что сделали:")
