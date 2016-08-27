# -*- coding: utf-8 -*-
import random
from datetime import datetime, timezone

import factory
import factory.fuzzy
from factory.alchemy import SQLAlchemyModelFactory

from models import session, store


class UsernameFactory(SQLAlchemyModelFactory):
    class Meta:
        model = store.Username
        sqlalchemy_session = session

    display_name = factory.Faker('user_name')
    lower_name = factory.SelfAttribute('display_name')

    account = factory.SubFactory('factories.store.UserAccountFactory')


class UserAccountFactory(SQLAlchemyModelFactory):
    class Meta:
        model = store.UserAccount
        sqlalchemy_session = session

    email = factory.Faker('email')
    birthday = factory.fuzzy.FuzzyDate(datetime(1980, 1, 1), datetime(2017, 1, 1))
    gender = factory.fuzzy.FuzzyChoice(['male', 'female'])
    password = 'pass'
    registered_at = factory.fuzzy.FuzzyDateTime(
        datetime(2010, 1, 1, tzinfo=timezone.utc), datetime(2017, 1, 1, tzinfo=timezone.utc))


class AccessTokenFactory(SQLAlchemyModelFactory):
    class Meta:
        model = store.AccessToken
        sqlalchemy_session = session

    token = factory.Faker('md5')
    is_valid = True
    generated_at = factory.LazyFunction(datetime.now)

    account = factory.SubFactory('factories.store.UserAccountFactory')


class ItemFactory(SQLAlchemyModelFactory):
    class Meta:
        model = store.Item
        sqlalchemy_session = session

    name = factory.Sequence(lambda n: 'item %03d' % n)
    price = factory.LazyAttribute(lambda n: random.randint(1000, 10000))
    description = factory.Sequence(lambda n: 'item %03d description' % n)


class SaleFactory(SQLAlchemyModelFactory):
    class Meta:
        model = store.Sale
        sqlalchemy_session = session

    paid_amount = factory.LazyAttribute(lambda n: random.randint(1000, 10000))
    sold_at = factory.fuzzy.FuzzyDateTime(
        datetime(2015, 1, 1, tzinfo=timezone.utc), datetime(2017, 1, 1, tzinfo=timezone.utc))

    account = factory.SubFactory('factories.store.UserAccountFactory')
    item = factory.SubFactory('factories.store.ItemFactory')
