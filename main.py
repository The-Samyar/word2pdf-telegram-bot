from telegram import Update, File
from telegram.ext import ContextTypes, Application, MessageHandler, filters, CommandHandler
from constants import *
from pprint import pprint
from docx2pdf import convert
import requests
import os, shutil

async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Send me a file. Make sure it ends with '.docx' .",
    )


async def rec_con(update:Update, context:ContextTypes.DEFAULT_TYPE):
    # try:
    #     user_dir = f"./user_db/{update.effective_user.id}/"
    #     file_id = update.effective_message.effective_attachment.file_id
    #     file = await context.bot.get_file(file_id=file_id)
    #     os.makedirs(user_dir, exist_ok=True)
    #     await file.download_to_drive(f"{user_dir}document.docx")
    #     await context.bot.send_message(
    #         chat_id=update.effective_chat.id,
    #         text="File is being processed..."
    #     )

    #     convert(f"{user_dir}document.docx", f"{user_dir}document.pdf")

    #     await context.bot.send_document(
    #         chat_id=update.effective_chat.id,
    #         document=f"{user_dir}document.pdf")
    # except:
    #     await context.bot.send_message(
    #         chat_id=update.effective_chat.id,
    #         document=f"An error occured while converting your file, try again.")

    # if os.path.isdir(user_dir):
    #     shutil.rmtree(user_dir)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        document=f"An error occured while converting your file, try again.")
    

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handlers([
        CommandHandler('start', start),
        MessageHandler(filters.Document.DOCX, rec_con)
    ])

    app.run_polling()

if __name__ == '__main__':
    main()
