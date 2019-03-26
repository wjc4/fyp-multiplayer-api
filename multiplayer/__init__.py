import os
import logging
import sys
from flask import Flask
application = Flask(__name__)

from .game_round import *

import multiplayer.routes.command
