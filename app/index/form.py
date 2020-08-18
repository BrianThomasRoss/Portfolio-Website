# -*- coding: utf-8 -*-
"""Email contact form."""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class ContactMe(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    company = StringField("Company", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = StringField("Message", validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create an instance."""
        super(ContactMe, self).__init__(*args, **kwargs)
        self.user = None

