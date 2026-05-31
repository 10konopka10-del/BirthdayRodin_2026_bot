from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

DINNERS = 9

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if "left" not in context.user_data:
        context.user_data["left"] = DINNERS

    left = context.user_data["left"]

    keyboard = [[InlineKeyboardButton("🍽 Заказать минт", callback_data="dinner")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"""🎉 С днём рождения, моя нежная Любовь!

Тебе подарено 9 минт.

Осталось минт: {left}""",
        reply_markup=reply_markup,
    )

async def dinner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    left = context.user_data.get("left", DINNERS)

    if left > 0:
        left -= 1
        context.user_data["left"] = left

        if left > 0:
            text = f"✅ Заказ принят!\n\nОсталось минт: {left}"
        else:
            text = "❤️ Все 9 минт использованы!"
    else:
        text = "❤️ Все 9 минт уже использованы!"

    keyboard = [[InlineKeyboardButton("🍽 Заказать минт", callback_data="dinner")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(text=text, reply_markup=reply_markup)

def main():
    TOKEN = "8993150538:AAHV8zEpOzgDLRIrSpfu_ve0-wL3ze6ZVrA"

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(dinner))

    app.run_polling()

if __name__ == "__main__":
    main()
