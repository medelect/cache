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
    dateIn = Column(DateTime, default=func.now())
    dateOut = Column(DateTime, default=func.now())
    dateBuy = Column(DateTime, default=func.now())
    favor = Column(Integer)
    coast = Column(Integer)
    usable = Column(Integer)
    converce =Column(Boolean)
    comment = Column(String(50))

    def __init__(self, article, waranty, dateIn, dateOut,
                 dateBuy, favour, coast, usable, converce, comment
                ):
        self.article = article
        self.waranty = waranty
        self.dateIn = dateIn
        self.dateOut = dateOut
        self.dateBuy = dateBuy
        self.favour = favour
        self.coast = coast
        self.usable = usable
        self.converce = converce
        self.comment = comment

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

    def __init__(self, date, quantas):
        self.date = date
        self.quantas = quantas

    def __repr__(self):
        return u'Income(%s, %s, %s)' % (self.id, self.date, self.quantas)


class Inflow(Base):
    __tablename__ = 'u_inflow'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    source = Column(String(100))
    amount = Column(Integer)

    def __init__(self, date, source, amount):
       self.date = date
       self.source = source
       self.amount = amount

    def __repr__(self):
        return u'Inflow(%s, %s, %s)' % (self.date, self.source, self.amount)


class Groups(Base):
    __tablename__ = 'u_groups'
    id = Column(Integer, primary_key=True)
    level = Column(Integer) # 0-base, 1-sub, 2-subsub
    name = Column(String(50))
    usable = Column(Integer)
    division = Column(Integer)
    color =  Column(Integer)
    plane =  Column(Integer)

    def __init__(self, level, name, usable, division, color, plane):
        self.level = level
        self.name = name
        self.usable = usable
        self.division = devision
        self.color = color
        self.plane = plane

    def __str__(self):
        return u'Group(%s, %s, %s, %s, %s, %s)' % (level,
                name, usable, division, color, plane)


