import logging
import os
from dotenv import load_dotenv
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext, ConversationHandler


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)
load_dotenv()

# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_text("Hello!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

import ai
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    chatgpt_response = await ai.ai_kuakua(update.message.text)
    await update.message.reply_text(chatgpt_response)


async def handle_rainbow(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    chatgpt_response = await ai.ai_rainbow(update.message.text)
    await update.message.reply_text(chatgpt_response)


def main() -> None:
    """Start the bot."""
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("rainbow", handle_rainbow))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()