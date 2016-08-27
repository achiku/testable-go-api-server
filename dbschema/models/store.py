# -*- coding: utf-8 -*-
from sqlalchemy import Column, DateTime, ForeignKey, Date, Boolean
from sqlalchemy.dialects.postgresql import BIGINT, TEXT, NUMERIC
from sqlalchemy.orm import backref, relationship

from . import Base


class Username(Base):

    __tablename__ = 'username'

    account_id = Column(BIGINT, ForeignKey('user_account.id'), primary_key=True)
    lower_name = Column(TEXT, nullable=False, unique=True)
    display_name = Column(TEXT, nullable=False)

    account = relationship('UserAccount', backref=backref('name'))


class UserAccount(Base):

    __tablename__ = 'user_account'

    id = Column(BIGINT, primary_key=True)
    email = Column(TEXT, nullable=False)
    gender = Column(TEXT, nullable=False)
    birthday = Column(Date, nullable=False)
    password = Column(TEXT, nullable=False)
    registered_at = Column(DateTime(timezone=True), nullable=False)


class AccessToken(Base):

    __tablename__ = 'access_token'

    account_id = Column(BIGINT, ForeignKey('user_account.id'), primary_key=True)
    token = Column(TEXT, nullable=False, unique=True)
    is_valid = Column(Boolean, nullable=False)
    generated_at = Column(DateTime(timezone=True), nullable=False)

    account = relationship('UserAccount', backref=backref('token'))


class Item(Base):

    __tablename__ = 'item'

    id = Column(BIGINT, primary_key=True)
    name = Column(TEXT, nullable=False)
    price = Column(NUMERIC, nullable=True)
    description = Column(TEXT(), nullable=True)


class Sale(Base):

    __tablename__ = 'sale'

    id = Column(BIGINT, primary_key=True)
    account_id = Column(BIGINT, ForeignKey('user_account.id'), nullable=False)
    item_id = Column(BIGINT, ForeignKey('item.id'), nullable=False)
    paid_amount = Column(NUMERIC, nullable=False)
    sold_at = Column(DateTime(timezone=True), nullable=False)

    account = relationship('UserAccount', backref=backref('sales'))
    item = relationship('Item', backref=backref('sales'))
