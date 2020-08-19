# -*- coding: utf-8 -*-
"""Routes included here.

/                   the application homepage

/about/             standard about page

/contributors/      information about contributors or how to begin contributing
"""
from flask import current_app, render_template, request, send_file
from flask_mail import Message

from app.blueprints import homepage_index
from app.extension import mail
from app.index.form import ContactMe


@homepage_index.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    current_app.logger.info("Hello from the home page!")
    form = ContactMe()
    if request.method == "POST":
        # if not form.validate():
        #     return render_template('home.html', form=form)
        # else:
        msg = Message(
            "New Portfolio Response",
            sender="contact@brianthomasross.com",
            recipients=["contact@brianthomasross.com"],
        )
        msg.body = """
              From: %s <%s>
              %s
              """ % (
            form.name.data,
            form.email.data,
            form.message.data,
        )
        mail.send(msg)
        return render_template("thanks.html")
    elif request.method == "GET":
        return render_template("home.html", form=form)


@homepage_index.route("/download-cv")
def download_resume():
    path = "index/docs/Brian-Ross.pdf"
    return send_file(path, as_attachment=True)
