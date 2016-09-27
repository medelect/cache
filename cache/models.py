from __future__ import unicode_literals
#from django.db import models


from sqlalchemy import Boolean,Time,Date, DateTime, String, Integer, ForeignKey, func
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Language(Base):
    __tablename__ = 'languages'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    extension = Column(String(50))

    def __init__(self, name, extension):
        self.name = name
        self.extension = extension

    def __repr__(self):
        return u'Language(%s, %s)' % (self.name, self.extension)


class Bill(Base):
    __tablename__ = 'u_bill'
    id = Column(Integer, primary_key=True)
    article = Column(Integer)
    waranty =Column(Integer)
    dateIn = Column(Date)
    dateOut = Column(Date)
    dateBuy = Column(Date)
    favour = Column(Integer)
    coast = Column(Integer)
    usable = Column(Integer)
    converce =Column(Boolean)
    comment = Column(String(50))

    def __init__(self, **kargs ):
        self.article = kargs['article']
        self.waranty = kargs['waranty']
        self.dateIn = kargs['dateIn']
        self.dateOut = kargs['dateOut']
        self.dateBuy = kargs['dateBuy']
        self.favour = kargs['favour']
        self.coast = kargs['coast']
        self.usable = kargs['usable']
        self.converce = kargs['converce']
        self.comment = kargs['comment']

    def __repr__(self):
         return u'Bill(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)' % (
                 self.article, self.waranty, self.dateIn, self.dateOut,
                 self.dateBuy, self.favour, self.coast, self.usable,
                 self.converce, self.comment
                )

class Income(Base):
    __tablename__ = 'u_income'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    quantas =  Column(Integer)

    def __init__(self, **kargs):
        self.date = kargs['date']
        self.quantas = kargs['quantas']

    def __repr__(self):
        return u'Income(%s, %s, %s)' % (self.id, self.date, self.quantas)


class Inflow(Base):
    __tablename__ = 'u_inflow'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    source = Column(String(100))
    amount = Column(Integer)

    def __init__(self, **kargs):
       self.date = kargs['date']
       self.source = kargs['source']
       self.amount = kargs['amount']

    def __repr__(self):
        return u'Inflow(%s, %s, %s)' % (self.date, self.source, self.amount)


class Groups(Base):
    __tablename__ = 'u_groups'
    id = Column(Integer, primary_key=True)
    parent = Column(Integer) 
    name = Column(String(50))
    usable = Column(Integer)
    division = Column(Integer)
    color =  Column(Integer)
    plane =  Column(Integer)
    
    def __init__(self, **kargs):
        self.parent = kargs['parent']
        self.name = kargs['name']
        self.usable = kargs['usable']
        self.division = kargs['division']
        self.color = kargs['color']
        self.plane = kargs['plane']

    def __str__(self):
        return u'Group(%s, %s, %s, %s, %s, %s)' % (parent,
                name, usable, division, color, plane)


