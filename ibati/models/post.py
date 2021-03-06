# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from ..extensions import db


class Category(db.Model):
    __tablename__ = 'ibati_category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    cname = db.Column(db.Unicode(20))
    order = db.Column(db.Integer)
    labels = db.relationship('Label', backref='category', order_by='Label.order')


class Label(db.Model):
    __tablename__ = 'ibati_label'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    cname = db.Column(db.Unicode(20))
    category_id = db.Column(db.Integer, db.ForeignKey('ibati_category.id', ondelete='CASCADE'))
    # category = db.relationship('Category', backref='labels')
    order = db.Column(db.Integer)
    custom = db.Column(db.Boolean, default=False)


class Post(db.Model):

    __tablename__ = 'ibati_post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(255))
    content = db.Column(db.UnicodeText)
    # author = 
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)
    update_date = db.Column(db.DateTime, default=datetime.datetime.now)
    status = db.Column(db.String(16), default='公开')

    category_id = db.Column(db.Integer, db.ForeignKey('ibati_category.id', ondelete='CASCADE'))
    category = db.relationship('Category', backref='posts')

    label_id = db.Column(db.Integer, db.ForeignKey('ibati_label.id'))
    label = db.relationship('Label', backref='posts')

    thumbnail = db.Column(db.String(255))
    click_count = db.Column(db.Integer, default=0)

