import logging
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Конфигурация
BOT_TOKEN = "7020279588:AAER0SU6QqAeqTPQfHfijWNJ5fOeKsVLXrk"
USER_ID = 1688425359

# Обработчики команд
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! I'm the HAIL bot. Every day at 1:00 PM (EDT), I send a hail forecast across the U.S., including cities, dealerships, and potential damage estimates. Stay one step ahead of the storm!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start – Welcome message\n"
        "/forecast – Get the latest hail forecast\n"
        "/help – Show available commands"
    )

async def forecast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "This is a sample forecast. Full automation will deliver real-time hail reports here every day at 13:00 EDT.")

# Основной запуск
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("forecast", forecast))
    app.run_polling()

if __name__ == "__main__":
    main()
