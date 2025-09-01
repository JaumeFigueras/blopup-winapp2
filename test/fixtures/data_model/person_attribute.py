#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope='session')
def person_attribute_list_string() -> str:
    return """{
    "results": [
        {
            "uuid": "7b4d6c23-c3bd-4e0e-ab20-ad2aacb527bc",
            "value": "SPAIN",
            "attributeType": {
                "uuid": "6aba6deb-b260-4117-9a50-37c8e1a76a45",
                "name": "Nationality"
            }
        },
        {
            "uuid": "8d871f2a-c2cc-11de-8d13-aa10c6dffd0f",
            "value": "+341234567",
            "attributeType": {
                "uuid": "14d4f066-15f5-102d-96e4-000c29c2a5d7",
                "name": "Telephone Number"
            }
        }
    ]
}"""