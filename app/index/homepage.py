# -*- coding: utf-8 -*-
"""Routes included here.

/                   the application homepage

/about/             standard about page

/contributors/      information about contributors or how to begin contributing
"""
from flask import current_app, flash, redirect, render_template, request, \
    url_for, send_file

from app.blueprints import homepage_index
from app.util import flash_errors
from app.index.form import ContactMe

@homepage_index.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    current_app.logger.info("Hello from the home page!")
    form = ContactMe()
    return render_template("home.html", form=form)


@homepage_index.route("/download-cv")
def download_resume():
    path = "index/docs/Brian-Ross.pdf"
    return send_file(path, as_attachment=True)
