#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from src.json_decoders.no_none_in_list import NoNoneInList
from src.data_model.person_address import PersonAddress

def test_init_00() -> None:
    person_address = PersonAddress(
        open_mrs_uuid='test_uuid',
        address='test_address',
        city_village='test_village',
        state_province='test_state',
        country_code='test_country_code',
        postal_code='test_postal_code',
        preferred=True,
        person='test_uuid'
    )
    assert person_address.open_mrs_uuid == 'test_uuid'
    assert person_address.address == 'test_address'
    assert person_address.city_village == 'test_village'
    assert person_address.state_province == 'test_state'
    assert person_address.country_code == 'test_country_code'
    assert person_address.postal_code == 'test_postal_code'
    assert person_address.preferred
    assert person_address.person_open_mrs_uuid == 'test_uuid'
    assert person_address.person is None

def test_init_01() -> None:
    """
    Tests the default class constructor without values
    """
    person_address = PersonAddress()  # type: ignore
    assert person_address.open_mrs_uuid is None
    assert person_address.address is None
    assert person_address.city_village is None
    assert person_address.state_province is None
    assert person_address.country_code is None
    assert person_address.postal_code is None
    assert not person_address.preferred
    assert person_address.person_open_mrs_uuid is None
    assert person_address.person is None

def test_init_02() -> None:
    """
    Tests the class constructor of a PersonName with unexpected attribute
    """
    person_address = PersonAddress(
        open_mrs_uuid='test_uuid',
        address='test_address',
        city_village='test_village',
        state_province='test_state',
        country_code='test_country_code',
        postal_code='test_postal_code',
        preferred=True,
        unexpected='test_unexpected'  # type: ignore
    )
    assert person_address.open_mrs_uuid == 'test_uuid'
    assert person_address.address == 'test_address'
    assert person_address.city_village == 'test_village'
    assert person_address.state_province == 'test_state'
    assert person_address.country_code == 'test_country_code'
    assert person_address.postal_code == 'test_postal_code'
    assert person_address.preferred
    assert person_address.person_open_mrs_uuid is None
    assert person_address.person is None
    assert getattr(person_address, 'unexpected', None) is None

def test_equals_01() -> None:
    """
    Tests the equality and inequality of two names

    :return: None
    """
    person_addresses = [
        PersonAddress(
            open_mrs_uuid='test_uuid',
            address='test_address',
            city_village='test_village',
            state_province='test_state',
            country_code='test_country_code',
            postal_code='test_postal_code',
            preferred=True
        ),
        PersonAddress(
            open_mrs_uuid='test_uuid',
            address='test_address',
            city_village='test_village',
            state_province='test_state',
            country_code='test_country_code',
            postal_code='test_postal_code',
            preferred=True
        ),
        PersonAddress(
            open_mrs_uuid='test_uui',
            address='test_address',
            city_village='test_village',
            state_province='test_state',
            country_code='test_country_code',
            postal_code='test_postal_code',
            preferred=True
        ),
        PersonAddress(
            open_mrs_uuid='test_uuid',
            address='test_addres',
            city_village='test_village',
            state_province='test_state',
            country_code='test_country_code',
            postal_code='test_postal_code',
            preferred=True
        ),
        PersonAddress(
            open_mrs_uuid='test_uuid',
            address='test_address',
            city_village='test_villag',
            state_province='test_state',
            country_code='test_country_code',
            postal_code='test_postal_code',
            preferred=True
        ),
        PersonAddress(
            open_mrs_uuid='test_uuid',
            address='test_address',
            city_village='test_village',
            state_province='test_stat',
            country_code='test_country_code',
            postal_code='test_postal_code',
            preferred=True
        ),
        PersonAddress(
            open_mrs_uuid='test_uuid',
            address='test_address',
            city_village='test_village',
            state_province='test_state',
            country_code='test_country_cod',
            postal_code='test_postal_code',
            preferred=True
        ),
        PersonAddress(
            open_mrs_uuid='test_uuid',
            address='test_address',
            city_village='test_village',
            state_province='test_state',
            country_code='test_country_code',
            postal_code='test_postal_cod',
            preferred=True
        ),
        PersonAddress(
            open_mrs_uuid='test_uuid',
            address='test_address',
            city_village='test_village',
            state_province='test_state',
            country_code='test_country_code',
            postal_code='test_postal_code',
            preferred=False
        ),
    ]
    assert person_addresses[0] != 'qwerty'
    assert person_addresses[0] == person_addresses[1]
    assert person_addresses[0] != person_addresses[2]
    assert person_addresses[0] != person_addresses[3]
    assert person_addresses[0] != person_addresses[4]
    assert person_addresses[0] != person_addresses[5]
    assert person_addresses[0] != person_addresses[6]
    assert person_addresses[0] != person_addresses[7]
    assert person_addresses[0] != person_addresses[8]

def test_display_01() -> None:
    person_addresses = [
        PersonAddress(
            open_mrs_uuid='test_uuid',
            address='test_address',
            city_village='test_village',
            state_province=None,
            country_code=None,
            postal_code='test_postal_code',
            preferred=True
        ),
        PersonAddress(
            open_mrs_uuid='test_uuid',
            address=None,
            city_village='test_village',
            state_province=None,
            country_code=None,
            postal_code='test_postal_code',
            preferred=True
        ),
        PersonAddress(
            open_mrs_uuid='test_uuid',
            address='test_address',
            city_village=None,
            state_province=None,
            country_code=None,
            postal_code='test_postal_code',
            preferred=True
        ),
        PersonAddress(
            open_mrs_uuid='test_uuid',
            address='test_address',
            city_village='test_village',
            state_province=None,
            country_code=None,
            postal_code=None,
            preferred=True
        ),
        PersonAddress(
            open_mrs_uuid='test_uuid',
            address=None,
            city_village=None,
            state_province=None,
            country_code=None,
            postal_code='test_postal_code',
            preferred=True
        ),
        PersonAddress(
            open_mrs_uuid='test_uuid',
            address=None,
            city_village='test_village',
            state_province=None,
            country_code=None,
            postal_code=None,
            preferred=True
        ),
        PersonAddress(
            open_mrs_uuid='test_uuid',
            address='test_address',
            city_village=None,
            state_province=None,
            country_code=None,
            postal_code=None,
            preferred=True
        ),
        PersonAddress(
            open_mrs_uuid='test_uuid',
            address=None,
            city_village=None,
            state_province=None,
            country_code=None,
            postal_code=None,
            preferred=True
        ),
    ]
    assert person_addresses[0].display == 'test_address ; test_village ; test_postal_code'
    assert person_addresses[1].display == '- ; test_village ; test_postal_code'
    assert person_addresses[2].display == 'test_address ;- ; test_postal_code'
    assert person_addresses[3].display == 'test_address ; test_village ;-'
    assert person_addresses[4].display == '- ;- ; test_postal_code'
    assert person_addresses[5].display == '- ; test_village ;-'
    assert person_addresses[6].display == 'test_address ;- ;-'
    assert person_addresses[7].display == '- ;- ;-'


def test_str_01() -> None:
    person_address = PersonAddress(
        open_mrs_uuid='test_uuid',
        address='test_address',
        city_village='test_village',
        state_province='test_state',
        country_code='test_country_code',
        postal_code='test_postal_code',
        preferred=True
    )
    txt = ("Address:\n"
           "  UUID: test_uuid\n"
           "  Address: test_address\n"
           "  City / Village: test_village\n"
           "  State / Province: test_state\n"
           "  Country code: test_country_code\n"
           "  Postal code: test_postal_code\n"
           "  Preferred: True\n")
    assert str(person_address) == txt


def test_str_02() -> None:
    """
    Tests the string conversion of a PersonAddress with None values in the class attributes
    """
    person_address = PersonAddress(
        open_mrs_uuid='test_uuid',
        address=None,
        city_village=None,
        state_province=None,
        country_code=None,
        postal_code=None,
        preferred=False
    )
    txt = ("Address:\n"
           "  UUID: test_uuid\n"
           "  Address: None\n"
           "  City / Village: None\n"
           "  State / Province: None\n"
           "  Country code: None\n"
           "  Postal code: None\n"
           "  Preferred: False\n")
    assert str(person_address) == txt


def test_parse_list_00(person_address_list_string: str) -> None:
    """
    Tests the JSON parse of a list of person addresses.

    :param person_address_list_string: The response generated by OpenRMS when a Person address subresource list query is
    issued. The response has been generated using a real setup using postman from the request:

    https://blopup-dev.upc.edu/openmrs/ws/rest/v1/person/df290974-a2b3-42dc-96c0-ee3a67842a2f/address?v=custom:(uuid,address1,cityVillage,stateProvince,country,postalCode,preferred,voided)

    :type person_address_list_string: str
    """
    person_addresses = json.loads(person_address_list_string, cls=NoNoneInList, object_hook=PersonAddress.object_hook_list_custom)
    assert person_addresses is not None
    assert type(person_addresses) is list
    assert len(person_addresses) == 2
    for address in person_addresses:
        assert isinstance(address, PersonAddress)


def test_parse_element_01(person_address_element_string: str) -> None:
    """

    :param person_address_element_string:
    :return:
    """
    person_address = json.loads(person_address_element_string, object_hook=PersonAddress.object_hook_element_custom)
    assert person_address is not None
    assert isinstance(person_address, PersonAddress)
