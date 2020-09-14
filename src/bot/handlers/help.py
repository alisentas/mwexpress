from telegram import Update, ParseMode

from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.user_helper import reply_to
from database import database
from i18n import Token
from models import User


def help_handler(user: User, update: Update) -> None:
    session = database.get_session()
    if not user.viewed_help:
        user.viewed_help = True
        session.commit()
    reply_to(user, update,
             user.language.get(Token.HELP_MESSAGE),
             Keyboard.main(user.language))
