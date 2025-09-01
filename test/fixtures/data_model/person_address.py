#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope='session')
def person_address_list_string() -> str:
    return """
        {
            "results": [
                {
                    "uuid": "2666d548-1da2-4058-96b1-b1eedb49fe80",
                    "address1": "Adress 1",
                    "cityVillage": "Palma",
                    "stateProvince": "Mallorca",
                    "country": "ES",
                    "postalCode": "12345",
                    "preferred": true,
                    "voided": false
                },
                {
                    "uuid": "eb94b55c-d75a-44a3-b357-d0d8bc5bd8a1",
                    "address1": "qqq",
                    "cityVillage": "Madrid",
                    "stateProvince": "Madrid",
                    "country": "ES",
                    "postalCode": "28288",
                    "preferred": false,
                    "voided": false
                }
            ]
        }
    """


@pytest.fixture(scope='session')
def person_address_element_string() -> str:
    return """
        {
            "uuid": "2666d548-1da2-4058-96b1-b1eedb49fe80",
            "address1": "Carrer de la Rossi",
            "cityVillage": "Palma",
            "stateProvince": "Mallorca",
            "country": "ES",
            "postalCode": "12345",
            "preferred": false,
            "voided": false
        }
    """