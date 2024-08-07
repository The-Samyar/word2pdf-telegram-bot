from telegram import Update
from telegram.ext import ContextTypes
from constants import *
from pprint import pprint
import requests
ContextTypes

async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Yo yo",
    )

async def file_message(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Send the file. Make sure it ends with '.docx' ."
    )

async def convert(update:Update, context:ContextTypes): ...
