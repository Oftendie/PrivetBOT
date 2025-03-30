from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = '7614171110:AAHSYhzB79XtEVaHqlGVDW9Nk6HUwXi_5Ws'

async def reply_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_hello))

print("Бот запущен...")
app.run_polling()