from aiogram import Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from services.event_api import get_similar_events
from keyboards.event_suggestions import create_event_suggestions_keyboard

router = Router()

@router.message(F.text)
async def handle_input_event(message: types.Message):
    user_id = message.from_user.id
    raw_text = message.text.strip()

    # Запрос к API: похожие события
    suggestions = await get_similar_events(user_id=user_id, query=raw_text)

    if suggestions:
        keyboard = create_event_suggestions_keyboard(suggestions, raw_text)
        await message.answer("Это похоже на одно из этих событий:", reply_markup=keyboard)
    else:
        # Предложить создать новое
        keyboard = create_event_suggestions_keyboard([], raw_text)
        await message.answer("Не нашёл похожих событий. Создать новое?", reply_markup=keyboard)
