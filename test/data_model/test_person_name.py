#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from src.json_decoders.no_none_in_list import NoNoneInList
from src.data_model.person_name import PersonName


def test_init_00() -> None:
    """
    Tests the class constructor of a PersonName with all values
    """
    person_name = PersonName(
        open_mrs_uuid='test_uuid',
        given_name='John',
        family_name='Doe',
        preferred=True,
        person='test_uuid'
    )
    assert person_name.open_mrs_uuid == 'test_uuid'
    assert person_name.given_name == 'John'
    assert person_name.family_name == 'Doe'
    assert person_name.preferred
    assert person_name.person_open_mrs_uuid == 'test_uuid'
    assert person_name.person is None

def test_init_01() -> None:
    """
    Tests the default class constructor without values
    """
    person_name = PersonName()  # type: ignore
    assert person_name.open_mrs_uuid is None
    assert person_name.given_name is None
    assert person_name.family_name is None
    assert not person_name.preferred
    assert person_name.person_open_mrs_uuid is None
    assert person_name.person is None

def test_init_02() -> None:
    """
    Tests the class constructor of a PersonName with unexpected attribute
    """
    person_name = PersonName(
        open_mrs_uuid='test_uuid',
        given_name='John',
        family_name='Doe',
        preferred=True,
        unexpected='test_unexpected'  # type: ignore
    )
    assert person_name.open_mrs_uuid == 'test_uuid'
    assert person_name.given_name == 'John'
    assert person_name.family_name == 'Doe'
    assert person_name.preferred
    assert person_name.person_open_mrs_uuid is None
    assert person_name.person is None
    assert getattr(person_name, 'unexpected', None) is None

def test_equals_01() -> None:
    """
    Tests the equality and inequality of two names

    :return: None
    """
    person_name_1 = PersonName(
        open_mrs_uuid='test_uuid',
        given_name='John',
        family_name='Doe',
        preferred=True
    )
    person_name_2 = PersonName(
        open_mrs_uuid='test_uuid',
        given_name='John',
        family_name='Doe',
        preferred=True
    )
    person_name_3 = PersonName(
        open_mrs_uuid='test_uuid',
        given_name='John',
        family_name='Doe',
        preferred=False
    )
    person_name_4 = PersonName(
        open_mrs_uuid='test_uuid',
        given_name='John',
        family_name='Do',
        preferred=True
    )
    person_name_5 = PersonName(
        open_mrs_uuid='test_uuid',
        given_name='Joh',
        family_name='Doe',
        preferred=True
    )
    person_name_6 = PersonName(
        open_mrs_uuid='uuid',
        given_name='John',
        family_name='Doe',
        preferred=True
    )
    assert person_name_1 != 'qwerty'
    assert person_name_1 == person_name_2
    assert person_name_1 != person_name_3
    assert person_name_1 != person_name_4
    assert person_name_1 != person_name_5
    assert person_name_1 != person_name_6


def test_display_01() -> None:
    """
    Tests the string conversion of a PersonName with all values set in the class attributes

    :return: None
    """
    person_name = PersonName(
        open_mrs_uuid='test_uuid',
        given_name='John',
        family_name='Doe',
        preferred=True
    )
    assert person_name.display == 'John Doe'
    person_name = PersonName(
        open_mrs_uuid='test_uuid',
        given_name='John',
        family_name=None,
        preferred=True
    )
    assert person_name.display == 'John'
    person_name = PersonName(
        open_mrs_uuid='test_uuid',
        given_name=None,
        family_name='Doe',
        preferred=True
    )
    assert person_name.display == 'Doe'
    person_name = PersonName(
        open_mrs_uuid='test_uuid',
        given_name=None,
        family_name=None,
        preferred=True
    )
    assert person_name.display == ''


def test_str_01() -> None:
    """
    Tests the string conversion of a PersonName with all values set in the class attributes

    :return: None
    """
    person_name = PersonName(
        open_mrs_uuid='test_uuid',
        given_name='John',
        family_name='Doe',
        preferred=True
    )
    txt = ("Name:\n"
           "  UUID: test_uuid\n"
           "  Given Name: John\n"
           "  Family Name: Doe\n"
           "  Is the preferred name: True\n")
    assert str(person_name) == txt


def test_str_02() -> None:
    """
    Tests the string conversion of a PersonName with None values in the class attributes

    :return: None
    """
    person_name = PersonName(
        open_mrs_uuid='test_uuid',
        given_name='John',
        family_name=None,
        preferred=True
    )
    txt = ("Name:\n"
           "  UUID: test_uuid\n"
           "  Given Name: John\n"
           "  Family Name: None\n"
           "  Is the preferred name: True\n")
    assert str(person_name) == txt


def test_parse_list_00(person_name_list_string: str) -> None:
    """
    Tests the JSON parse of a list of person names.

    :param person_name_list_string: The response generated by OpenRMS when a Person name subresource list query is
    issued. The response has been generated using a real setup using postman from the request:

    https://blopup-dev.upc.edu/openmrs/ws/rest/v1/person/df290974-a2b3-42dc-96c0-ee3a67842a2f/name?v=custom:(uuid,givenName,familyName,preferred,voided)

    :type person_name_list_string: str

    :return: None
    """
    person_names = json.loads(person_name_list_string, cls=NoNoneInList, object_hook=PersonName.object_hook_list_custom)
    assert person_names is not None
    assert type(person_names) is list
    assert len(person_names) == 2
    for name in person_names:
        assert isinstance(name, PersonName)


def test_parse_element_01(person_name_element_string: str) -> None:
    """
    Tests the JSON parse of a list of person names.

    :param person_name_list_string: The response generated by OpenRMS when a Person name subresource list query is
    issued. The response has been generated using a real setup using postman from the request:

    https://blopup-dev.upc.edu/openmrs/ws/rest/v1/person/df290974-a2b3-42dc-96c0-ee3a67842a2f/name?v=custom:(uuid,givenName,familyName,preferred,voided)

    :type person_name_list_string: str

    :return: None
    """
    person_name = json.loads(person_name_element_string, object_hook=PersonName.object_hook_element_custom)
    assert person_name is not None
    assert isinstance(person_name, PersonName)
    assert person_name.open_mrs_uuid == '54c3cc06-8c25-4ad6-b8e0-84238a3ce2e7'
    assert person_name.given_name == 'Rosiy'
    assert person_name.family_name == 'De Palma'
    assert person_name.preferred


