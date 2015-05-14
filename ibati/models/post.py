# -*- coding: utf-8 -*-
from ibati.db import sadb as db
import datetime

class Category(db.Model):
    __tablename__ = 'ibati_category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    cname = db.Column(db.Unicode(20))
    parent_id = db.Column(db.Integer, db.ForeignKey('ibati_category.id'))
    parent = db.relationship('Category', backref='children', remote_side=[id])
    order = db.Column(db.Integer)


class Post(db.Model):

    __tablename__ = 'ibati_posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(255))
    content = db.Column(db.UnicodeText)
    # author = 
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)
    update_date = db.Column(db.DateTime, default=datetime.datetime.now)
    status = db.Column(db.String(16))

    category_id = db.Column(db.Integer, db.ForeignKey('ibati_category.id'))
    category = db.relationship('Category', backref='posts')

