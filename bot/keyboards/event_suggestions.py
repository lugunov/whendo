from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_event_suggestions_keyboard(suggestions, raw_input):
    buttons = []

    for event in suggestions:
        buttons.append([
            InlineKeyboardButton(
                text=event["title"],
                callback_data=f"select_event:{event['id']}:{raw_input}"
            )
        ])

    buttons.append([
        InlineKeyboardButton(
            text="➕ Создать новое событие",
            callback_data=f"create_event:{raw_input}"
        )
    ])

    return InlineKeyboardMarkup(inline_keyboard=buttons)
