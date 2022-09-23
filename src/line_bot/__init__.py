from flask import Blueprint

api_bp = Blueprint('api', __name__)

from src.line_bot.bot import *
