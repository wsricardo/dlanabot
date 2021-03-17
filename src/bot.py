#!/usr/bin/env python
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

"""
    Get data from files with output messages for bot.
    Using database mongodb or sql and json file.
"""

import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from commandsBot import*
import dataBot

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def main():
    """Start the bot."""
    import configBot
    print(configBot.confbot['bot_name'],configBot.confbot['info'], configBot.confbot['token'])
    
    
    # Create the Updater and pass it your bot's token.
    #updater = Updater("TOKEN")
    updater = Updater(configBot.confbot['token'])
    # State bot ask or normal. "0" for normal and "1" for 'ask' bot questions.
    stateBot = 0
    registerBot(configBot, updater, stateBot)
    

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ajuda", help_command))
    dispatcher.add_handler(CommandHandler("name", getName))
    dispatcher.add_handler(CommandHandler("listar", listar))
    dispatcher.add_handler(CommandHandler("menu", mainMenu))
    dispatcher.add_handler(CommandHandler("pesquisar", search))
    dispatcher.add_handler(CommandHandler("retirada", retirada))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler((Filters.text & ~Filters.command), echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
