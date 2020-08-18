# -*- coding: utf-8 -*-
"""Asynchronous Mail Serive."""
from flask_mail import Message

from app.extension import mail


# @async
# def send_email_async(app, msg):
#     with app.app_context():
#         mail.send(msg)
#
#
# def send_email(text_body):
#     msg = Message('New Portfolio Response',
#                   recipients=['contact@brianthomasross.com'],
#                   body=text_body,
#                   )
#     send_email_async(app, msg)