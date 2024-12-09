
# Word2PDF Telegram Bot 📄➡️📑

A handy Telegram bot that converts Word documents (`.docx`) into PDF files. Simplify document sharing by converting files directly within Telegram!

## 🚀 Features
- **Word to PDF Conversion**: Effortlessly convert `.docx` files to `.pdf` format.
- **Telegram Integration**: Users interact with the bot through Telegram, making the process seamless.
- **Secure and Fast**: Documents are processed quickly and securely.
- **User-Friendly**: Simple and intuitive commands.

## 📋 Table of Contents
- [Getting Started](#getting-started)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## 🛠️ Getting Started
Follow these instructions to set up and run the Word2PDF Telegram Bot.

### Prerequisites
- [Python](https://www.python.org/) (version 3.7 or later)
- Telegram Bot API token
- Required libraries (specified in `requirements.txt`)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/The-Samyar/word2pdf-telegram-bot.git
   cd word2pdf-telegram-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the `.env` file:
   - Create a `.env` file in the root directory.
   - Add the following variable:
     ```env
     TELEGRAM_BOT_TOKEN=your_telegram_bot_token
     ```

4. Run the bot:
   ```bash
   python bot.py
   ```

## 💡 System Requirements
- **Software**:
  - Python 3.7 or later.
  - Libraries: `python-telegram-bot`, `python-docx`, `reportlab` (included in `requirements.txt`).

## 🖥️ Usage
1. Start the bot:
   ```bash
   python bot.py
   ```

2. Interact with the bot via Telegram:
   - Send a `.docx` file to the bot.
   - The bot processes the file and sends back the converted PDF.

3. To stop the bot, interrupt the script (`Ctrl+C`).


## 📝 License
This project is licensed under the [MIT License](LICENSE).

### 🙌 Let's Build Together!  
If you find this project helpful, give it a ⭐ and share it with others!
