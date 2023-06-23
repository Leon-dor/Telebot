from telegram.ext import ContextTypes, Application

TOKEN = "6156730475:AAFUHqGhJscVxcux6DM1EKguGMH25ABFVJ8"


async def callback_minute(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id='@Sigma_Rules_Bot', text='One message every minute')


application = Application.builder().token(TOKEN).build()
job_queue = application.job_queue

job_minute = job_queue.run_repeating(interval=60, first=10)

application.run_polling()

