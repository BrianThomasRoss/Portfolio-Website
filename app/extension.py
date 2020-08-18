# -*- coding: utf-8 -*-.
"""Extensions module.

Each extension initialization occurs in the app factory.
"""

from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_static_digest import FlaskStaticDigest
from flask_wtf.csrf import CSRFProtect

bcrypt = Bcrypt()
csrf_protect = CSRFProtect()
cache = Cache()
debug_toolbar = DebugToolbarExtension()
flask_static_digest = FlaskStaticDigest()
