#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import pytest

from freezegun import freeze_time

from typing import Tuple

from src.json_decoders.no_none_in_list import NoNoneInList
from src.data_model.person import Person
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
    person = Person(
        open_mrs_uuid='test_uuid',
        gender=GenderCategory.M,
        birth_date=datetime.date(1970, 1, 1),
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
    )
    assert person.open_mrs_uuid == 'test_uuid'
    assert person.gender == GenderCategory.M
    assert person.birth_date == datetime.date(1970, 1, 1)
    assert not person.birth_date_estimated
    assert not person.dead
    assert person.death_date is None
    assert not person.death_date_estimated
    assert not person.voided


def test_init_01() -> None:
    """
    Tests the default class constructor without values
    """
    person = Person()  # type: ignore
    assert person.open_mrs_uuid is None
    assert person.gender is None
    assert person.birth_date is None
    assert not person.birth_date_estimated
    assert not person.dead
    assert person.death_date is None
    assert not person.death_date_estimated
    assert not person.voided

def test_init_02() -> None:
    """
    Tests the class constructor of a PersonName with unexpected attribute
    """
    person = Person(
        open_mrs_uuid='test_uuid',
        gender=GenderCategory.M,
        birth_date=datetime.date(1970, 1, 1),
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
        unexpected="test_unexpected"  # type: ignore
    )
    assert person.open_mrs_uuid == 'test_uuid'
    assert person.gender == GenderCategory.M
    assert person.birth_date == datetime.date(1970, 1, 1)
    assert not person.birth_date_estimated
    assert not person.dead
    assert person.death_date is None
    assert not person.death_date_estimated
    assert not person.voided
    assert getattr(person, 'unexpected', None) is None


def test_str_01() -> None:
    """
    Tests the string conversion of a Person with all values set in the class attributes
    """
    person = Person(
        open_mrs_uuid='test_uuid',
        gender=GenderCategory.M,
        birth_date=datetime.date(1970, 1, 1),
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
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
           "    None\n")
    assert str(person) == txt

def test_str_02() -> None:
    """
    Tests the string conversion of a Person with all values set in the class attributes
    """
    person = Person(
        open_mrs_uuid=None,
        gender=GenderCategory.N,
        birth_date=None,
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
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
           "    None\n")
    assert str(person) == txt


def test_str_03() -> None:
    """
    Tests the string conversion of a Person with all values and relation set in the class attributes
    """
    person = Person(
        open_mrs_uuid='test_uuid',
        gender=GenderCategory.M,
        birth_date=datetime.date(1970, 1, 1),
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
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
    person.names = [name_1, name_2]
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
    person.addresses = [address_1, address_2]
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
    person.attributes = [person_attribute_1, person_attribute_2]
    txt = ("Person:\n"
           "  UUID: test_uuid\n"
           "  Gender: Male\n"
           "  Birthday: 1970-01-01\n"
           "  Birthday estimated: False\n"
           "  Dead: False\n"
           "  Death date: None\n"
           "  Death date estimated: False\n"
           "  Name #1:\n"
           "    UUID: test_uuid1\n"
           "    Given Name: Given1\n"
           "    Family Name: Family1\n"
           "    Is the preferred name: False\n"
           "  Name #2:\n"
           "    UUID: test_uuid2\n"
           "    Given Name: Given2\n"
           "    Family Name: Family2\n"
           "    Is the preferred name: True\n"
           "  Address #1:\n"
           "    UUID: test_uuid1\n"
           "    Address: test address1\n"
           "    City / Village: test village1\n"
           "    State / Province: None\n"
           "    Country code: None\n"
           "    Postal code: test 12341\n"
           "    Preferred: False\n"
           "  Address #2:\n"
           "    UUID: test_uuid2\n"
           "    Address: test address2\n"
           "    City / Village: test village2\n"
           "    State / Province: None\n"
           "    Country code: None\n"
           "    Postal code: test 12342\n"
           "    Preferred: True\n"
           "  Attribute #1:\n"
           "    UUID: test_uuid\n"
           "    Attribute type name: test_name\n"
           "    Value: test_value\n"
           "  Attribute #2:\n"
           "    UUID: test_uuid2\n"
           "    Attribute type name: test_name\n"
           "    Value: test_value\n")
    assert str(person) == txt


def test_equal_00() -> None:
    """
    Tests the string conversion of a Person with all values and relation set in the class attributes
    """
    person_1 = Person(
        open_mrs_uuid='test_uuid',
        gender=GenderCategory.M,
        birth_date=datetime.date(1970, 1, 1),
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
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
    person_1.names = [name_1, name_2]
    person_1.addresses = [address_1, address_2]
    person_1.attributes = [person_attribute_1, person_attribute_2]
    person_2 = Person()
    person_3 = Person(
        open_mrs_uuid='test_uuid',
        gender=GenderCategory.M,
        birth_date=datetime.date(1970, 1, 1),
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
    )
    person_3.names = [name_4, name_3]
    person_3.addresses = [address_4, address_3]
    person_3.attributes = [person_attribute_4, person_attribute_3]
    assert person_1 != 'test'
    assert person_1 != person_2
    assert person_1 == person_3


def test_name_01() -> None:
    """
    Tests the name property of a person
    """
    person = Person()  # type: ignore
    assert person.name is None


def test_name_02() -> None:
    """
    Tests the name property of a person
    """
    person = Person(
        open_mrs_uuid='test_uuid',
        gender=GenderCategory.M,
        birth_date=datetime.date(1970, 1, 1),
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
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
    person.names = [name_1, name_2]
    assert person.name.display == 'Given2 Family2'


def test_name_03() -> None:
    """
    Tests the name property of a person
    """
    person = Person(
        open_mrs_uuid='test_uuid',
        gender=GenderCategory.M,
        birth_date=datetime.date(1970, 1, 1),
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
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
        preferred=False
    )
    person.names = [name_1, name_2]
    assert person.name is None


@freeze_time('2025-12-31')
def test_age_01() -> None:
    """

    :return: None
    """
    person = Person(
        open_mrs_uuid='test_uuid',
        gender=GenderCategory.M,
        birth_date=datetime.date(1970, 1, 1),
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
    )
    assert person.age == 55


@freeze_time('2025-01-01')
def test_age_02() -> None:
    """

    :return: None
    """
    person = Person(
        open_mrs_uuid='test_uuid',
        gender=GenderCategory.M,
        birth_date=datetime.date(1970, 1, 1),
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
    )
    assert person.age == 55


@freeze_time('2025-12-12')
def test_age_03() -> None:
    """

    :return: None
    """
    person = Person()
    assert person.age is None


def test_address_01() -> None:
    """
    Tests the name property of a person
    """
    person = Person(
        open_mrs_uuid='test_uuid',
        gender=GenderCategory.M,
        birth_date=datetime.date(1970, 1, 1),
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
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
    person.addresses = [address_1, address_2]
    assert person.address == address_2
    assert person.address.display == "test address2 ; test village2 ; test 12342"


def test_address_02() -> None:
    """
    Tests the name property of a person
    """
    person = Person()
    assert person.address is None


def test_address_03() -> None:
    """
    Tests the name property of a person
    """
    person = Person(
        open_mrs_uuid='test_uuid',
        gender=GenderCategory.M,
        birth_date=datetime.date(1970, 1, 1),
        birth_date_estimated=False,
        dead=False,
        death_date=None,
        death_date_estimated=False,
        voided=False,
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
        preferred=False
    )
    person.addresses = [address_1, address_2]
    assert person.address is None


def test_parse_element_01(person_element_string: str) -> None:
    """
    Tests the JSON parse of a person element.

    :param person_element_string: The response generated by OpenRMS when a Person query is issued. The response has
    been generated using a real setup using postman from the request:

    https://blopup-dev.upc.edu/openmrs/ws/rest/v1/person/df290974-a2b3-42dc-96c0-ee3a67842a2f?v=custom:(uuid,gender,birthdate,birthdateEstimated,dead,deathDate,deathdateEstimated,voided)

    :type person_element_string: str
    """
    person = json.loads(person_element_string, object_hook=Person.object_hook_element_custom)
    assert person is not None
    assert type(person) is Person
    assert isinstance(person, Person)
    assert isinstance(person.birth_date, datetime.date)
    assert isinstance(person.death_date, datetime.date) or person.death_date is None
    assert isinstance(person.gender, GenderCategory)


def test_parse_element_02(person_update_element_string: str) -> None:
    """
    Tests the JSON parse of a person element after a POST to the network doing an UPDATE action.

    :param person_update_element_string: The response generated by OpenRMS when a Person UPDATE (POST) query is issued.
    The response has been generated using a real setup using postman from the request:

    https://blopup-dev.upc.edu/openmrs/ws/rest/v1/person/df290974-a2b3-42dc-96c0-ee3a67842a2f

    :type person_element_string: str
    """
    person = json.loads(person_update_element_string, object_hook=Person.object_hook_element_custom)
    assert person is not None
    assert type(person) is Person
    assert isinstance(person, Person)
    assert person.birth_date == datetime.date(1972, 1, 2)
    assert person.gender == GenderCategory.F
    assert person.birth_date_estimated
    assert person.dead
    assert person.death_date == datetime.date(2021, 2, 3)
    assert not person.death_date_estimated