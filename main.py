import cloudconvert.job
from telegram import Update
from telegram.ext import ContextTypes, Application, MessageHandler, filters, CommandHandler
from constants import *
import os, shutil
import cloudconvert



async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Send me a file. Make sure it ends with '.docx' .",
    )


async def converter_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    try:
        # Logger
        user_text = f"({update.effective_user.username}){update.effective_user.full_name}:"
        print(user_text)

        # Receive the docx file
        user_dir = f"./user_db/{update.effective_user.id}/"
        os.makedirs(user_dir, exist_ok=True)

        file_id = update.effective_message.effective_attachment.file_id
        file = await context.bot.get_file(file_id=file_id)
        await file.download_to_drive(f"{user_dir}document.docx")

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Processing..."
        )



        # Try for multiple users first. If there was concurrency problems, You need to create a job each time for each user. Then at the end of the code delete the job using cloudconvert.Job.delete() or https://cloudconvert.com/api/v2/jobs#jobs-delete:
        # Conversion
        cloudconvert.configure(api_key=API_KEY, sandbox=False)
        job = cloudconvert.Job.create(payload={
                "tasks": {
                    "import": {
                        "operation": "import/upload"
                    },
                    "convert": {
                        "operation": "convert",
                        "input_format": "docx",
                        "output_format": "pdf",
                        "engine": "libreoffice",
                        "input": [
                            "import"
                        ],
                        "pdf_a": True,
                        "filename": "document.pdf"
                    },
                    "export": {
                        "operation": "export/url",
                        "input": [
                            "convert"
                        ],
                        "inline": False,
                        "archive_multiple_files": False
                    }
                },
                "tag": "jobbuilder"
            })

        if job['tasks'][0]['name'] == 'import':
            import_task = job['tasks'][0]
            import_task_id = import_task['id']
        else:
            raise Exception("1")
        
        if job['tasks'][2]['name'] == 'export':
            export_task = job['tasks'][2]
            export_task_id = export_task['id']
        else:
            raise Exception("2")
        
        cloudconvert.Task.upload(
            file_name=f"{user_dir}document.docx",
            task=import_task
            )
        tasker = cloudconvert.Task.wait(id=export_task_id)
        
        file = tasker['result']['files'][0]

        cloudconvert.download(filename=f"{user_dir}document.pdf", url=file['url'])


        
        
        # Send pdf file
        await context.bot.send_document(
            chat_id=update.effective_chat.id,
            document=f"{user_dir}document.pdf")
    except Exception as e:
        
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"An error occured while converting your file, try again.")
        print(f"Error message:\n{repr(e)}")

    if os.path.isdir(user_dir):
        shutil.rmtree(user_dir)
    cloudconvert.Job.delete(id=job['id'])

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handlers([
        CommandHandler('start', start),
        MessageHandler(filters.Document.DOCX, converter_command)
    ])

    app.run_polling()

if __name__ == '__main__':
    main()
