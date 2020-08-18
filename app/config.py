# -*- coding: utf-8 -*-
"""Application configuration.

Locally these variables can be set with `source .env`
"""
from pathlib import Path

from environs import Env

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="production")
DEBUG = ENV == "development"
SECRET_KEY = env.str("SECRET_KEY")
SEND_FILE_MAX_AGE_DEFAULT = env.int("SEND_FILE_MAX_AGE_DEFAULT")
BCRYPT_LOG_ROUNDS = env.int("BCRYPT_LOG_ROUNDS", default=13)
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False
CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.
# File paths
ROOT_PATH = str(Path(__file__).absolute().parent.parent)
CONF_DIR = ROOT_PATH + "/etc"
# Mail service
MAIL_SERVER = "send.one.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = False
MAIL_USERNAME = env.str("MAIL_USERNAME")
MAIL_PASSWORD = env.str("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = "contact@brianthomasross.com"
MAIL_SUPPRESS_SEND = False
TESTING = False
