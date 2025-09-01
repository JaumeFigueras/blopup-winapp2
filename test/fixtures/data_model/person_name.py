#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope='session')
def person_name_list_string() -> str:
    return """{
    "results": [
        {
            "uuid": "54c3cc06-8c25-4ad6-b8e0-84238a3ce2e7",
            "givenName": "Rosi",
            "familyName": "De Palma",
            "preferred": true,
            "voided": false
        },
        {
            "uuid": "9427b196-dd70-444b-aa44-58bf5aa53620",
            "givenName": "Rossi",
            "familyName": "Palma",
            "preferred": false,
            "voided": false
        },
        {
            "uuid": "c9236e02-5f4a-4b1a-b6f6-c518869a1f44",
            "givenName": "Rosi",
            "familyName": "De Palma",
            "preferred": false,
            "voided": true
        }
    ]
}"""


@pytest.fixture(scope='session')
def person_name_element_string() -> str:
    return """
        {
            "uuid": "54c3cc06-8c25-4ad6-b8e0-84238a3ce2e7",
            "givenName": "Rosiy",
            "familyName": "De Palma",
            "preferred": true,
            "voided": false
        }    
    """