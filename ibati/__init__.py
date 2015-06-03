# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, flash, redirect, url_for
from flask.ext.login import LoginManager, current_user
from flask.ext.uploads import configure_uploads, patch_request_class
import logging
from logging import FileHandler, Formatter

from ibati import views
from ibati.extensions import db, upload_set
from ibati.models import Category, User, Link


def create_app(config=None):
    app = Flask(__name__)

    # config
    app.config.from_object(config)

    # blueprint
    app.register_blueprint(views.home)
    app.register_blueprint(views.post)
    app.register_blueprint(views.member)
    app.register_blueprint(views.admin)
    #app.register_blueprint(views.error_log)
    #app.register_blueprint(views.error_log_status)

    # database
    db.init_app(app)

    # logger
    init_app_logger(app)

    # app context
    init_app_context(app)

    # flask-login
    configure_login(app)

    # flask-uploads
    configure_uploads(app, (upload_set, ))
    patch_request_class(app)    # default 16M limit

    return app


def init_app_logger(app):
    # logging

    file_handler = FileHandler('flask.log')

    file_handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
    ))

    file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(file_handler)


def init_app_context(app):

    @app.context_processor
    def inject_categories():
        categories = Category.query.order_by(Category.order.asc()).all()
        return dict(categories=categories)

    @app.context_processor
    def inject_links():
        links = Link.query.order_by(Link.order.asc()).all()
        return dict(links=links)


def configure_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # print user_id
        return User.query.get(user_id)

    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for('admin.login'))
