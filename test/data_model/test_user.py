#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import pytest

from freezegun import freeze_time

from typing import Tuple

from sqlalchemy.testing.suite.test_reflection import users

from src.json_decoders.no_none_in_list import NoNoneInList
from src.data_model.user import User
from src.data_model.person import GenderCategory
from src.data_model.person_name import PersonName
from src.data_model.person_address import PersonAddress
from src.data_model.person_attribute_type import PersonAttributeType
from src.data_model.person_attribute import PersonAttribute

import datetime

from typing import List

def test_init_00() -> None:
    """
    Tests the class constructor of a PersonName with all values
    """
    user = User(
        open_mrs_uuid='test_uuid',
        gender=GenderCategory.M,
        birth_date=datetime.date(1970, 1, 1),
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
        username='test_username',
        password='test_password',
    )
    assert user.open_mrs_uuid == 'test_uuid'
    assert user.gender == GenderCategory.M
    assert user.birth_date == datetime.date(1970, 1, 1)
    assert not user.birth_date_estimated
    assert not user.dead
    assert user.death_date is None
    assert not user.death_date_estimated
    assert not user.voided
    assert user.username == 'test_username'
    assert user.password == 'test_password'


def test_init_01() -> None:
    """
    Tests the default class constructor without values
    """
    user = User()  # type: ignore
    assert user.open_mrs_uuid is None
    assert user.gender is None
    assert user.birth_date is None
    assert not user.birth_date_estimated
    assert not user.dead
    assert user.death_date is None
    assert not user.death_date_estimated
    assert not user.voided
    assert user.username is None
    assert user.password is None

def test_init_02() -> None:
    """
    Tests the class constructor of a PersonName with unexpected attribute
    """
    user = User(
        open_mrs_uuid='test_uuid',
        gender=GenderCategory.M,
        birth_date=datetime.date(1970, 1, 1),
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
        username='test_username',
        password='test_password',
        unexpected="test_unexpected"  # type: ignore
    )
    assert user.open_mrs_uuid == 'test_uuid'
    assert user.gender == GenderCategory.M
    assert user.birth_date == datetime.date(1970, 1, 1)
    assert not user.birth_date_estimated
    assert not user.dead
    assert user.death_date is None
    assert not user.death_date_estimated
    assert not user.voided
    assert user.username == 'test_username'
    assert user.password == 'test_password'
    assert getattr(user, 'unexpected', None) is None


def test_str_01() -> None:
    """
    Tests the string conversion of a Person with all values set in the class attributes
    """
    user = User(
        open_mrs_uuid='test_uuid',
        gender=GenderCategory.M,
        birth_date=datetime.date(1970, 1, 1),
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
        username='test_username',
        password='test_password',
    )
    txt = ("Person:\n"
           "  UUID: test_uuid\n"
           "  Gender: Male\n"
           "  Birthday: 1970-01-01\n"
           "  Birthday estimated: False\n"
           "  Dead: False\n"
           "  Death date: None\n"
           "  Death date estimated: False\n"
           "  Names:\n"
           "    None\n"
           "  Addresses:\n"
           "    None\n"
           "  Attributes:\n"
           "    None\n"           
           "User:\n"           
           "  Username: test_username\n"
           "  Password: test_password\n")
    assert str(user) == txt

def test_str_02() -> None:
    """
    Tests the string conversion of a Person with all values set in the class attributes
    """
    user = User(
        open_mrs_uuid=None,
        gender=GenderCategory.N,
        birth_date=None,
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
        username=None,
        password=None,
    )
    txt = ("Person:\n"
           "  UUID: None\n"
           "  Gender: Undefined gender\n"
           "  Birthday: None\n"
           "  Birthday estimated: False\n"
           "  Dead: False\n"
           "  Death date: None\n"
           "  Death date estimated: False\n"
           "  Names:\n"
           "    None\n"
           "  Addresses:\n"
           "    None\n"
           "  Attributes:\n"
           "    None\n"
           "User:\n"
           "  Username: None\n"
           "  Password: None\n")
    assert str(user) == txt


def test_equal_00() -> None:
    """
    Tests the string conversion of a Person with all values and relation set in the class attributes
    """
    user_1 = User(
        open_mrs_uuid='test_uuid',
        gender=GenderCategory.M,
        birth_date=datetime.date(1970, 1, 1),
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
        username='test_username',
        password='test_password',
    )
    name_1 = PersonName(
        open_mrs_uuid='test_uuid1',
        given_name='Given1',
        family_name='Family1',
        preferred=False
    )
    name_2 = PersonName(
        open_mrs_uuid='test_uuid2',
        given_name='Given2',
        family_name='Family2',
        preferred=True
    )
    name_3 = PersonName(
        open_mrs_uuid='test_uuid1',
        given_name='Given1',
        family_name='Family1',
        preferred=False
    )
    name_4 = PersonName(
        open_mrs_uuid='test_uuid2',
        given_name='Given2',
        family_name='Family2',
        preferred=True
    )
    address_1 = PersonAddress(
        open_mrs_uuid='test_uuid1',
        address='test address1',
        postal_code='test 12341',
        city_village='test village1',
        preferred=False
    )
    address_2 = PersonAddress(
        open_mrs_uuid='test_uuid2',
        address='test address2',
        postal_code='test 12342',
        city_village='test village2',
        preferred=True
    )
    address_3 = PersonAddress(
        open_mrs_uuid='test_uuid1',
        address='test address1',
        postal_code='test 12341',
        city_village='test village1',
        preferred=False
    )
    address_4 = PersonAddress(
        open_mrs_uuid='test_uuid2',
        address='test address2',
        postal_code='test 12342',
        city_village='test village2',
        preferred=True
    )
    person_attribute_type_1 = PersonAttributeType(
        open_mrs_uuid='test_uuid',
        name='test_name',
    )
    person_attribute_1 = PersonAttribute(
        open_mrs_uuid='test_uuid',
        value='test_value',
        attribute_type=person_attribute_type_1,
    )
    person_attribute_type_2 = PersonAttributeType(
        open_mrs_uuid='test_uuid2',
        name='test_name',
    )
    person_attribute_2 = PersonAttribute(
        open_mrs_uuid='test_uuid2',
        value='test_value',
        attribute_type=person_attribute_type_2,
    )
    person_attribute_3 = PersonAttribute(
        open_mrs_uuid='test_uuid',
        value='test_value',
        attribute_type=person_attribute_type_1,
    )
    person_attribute_4 = PersonAttribute(
        open_mrs_uuid='test_uuid2',
        value='test_value',
        attribute_type=person_attribute_type_2,
    )
    user_1.names = [name_1, name_2]
    user_1.addresses = [address_1, address_2]
    user_1.attributes = [person_attribute_1, person_attribute_2]
    user_2 = User()
    user_3 = User(
        open_mrs_uuid='test_uuid',
        gender=GenderCategory.M,
        birth_date=datetime.date(1970, 1, 1),
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
        username='test_username',
        password='test_password',
    )
    user_3.names = [name_4, name_3]
    user_3.addresses = [address_4, address_3]
    user_3.attributes = [person_attribute_4, person_attribute_3]
    assert user_1 != 'test'
    assert user_1 != user_2
    assert user_1 == user_3

