import logging
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- TOKENINGIZNI SHU YERGA QO'YING ---
TOKEN = "BOT_TOKENINGIZNI_SHU_YERGA_YOZING"

logging.basicConfig(level=logging.INFO)

app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Xojobod Bot Ishlamoqda!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! 👋\n\nXojobod botiga xush kelibsiz!\n\n/start - Boshlash"
    )

def run_flask():
    app_flask.run(host='0.0.0.0', port=10000)

def main():
    # Flask ni alohida ishga tushirish
    Thread(target=run_flask).start()
    
    # Telegram bot
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == '__main__':
    main()
