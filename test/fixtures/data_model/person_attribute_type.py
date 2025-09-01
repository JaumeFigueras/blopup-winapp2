#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope='session')
def person_attribute_type_list_string() -> str:
    return """{
    "results": [
        {
            "uuid": "8d8718c2-c2cc-11de-8d13-0010c6dffd0f",
            "name": "Birthplace"
        },
        {
            "uuid": "8d871afc-c2cc-11de-8d13-0010c6dffd0f",
            "name": "Citizenship"
        },
        {
            "uuid": "8d871f2a-c2cc-11de-8d13-0010c6dffd0f",
            "name": "Civil Status"
        },
        {
            "uuid": "8d87236c-c2cc-11de-8d13-0010c6dffd0f",
            "name": "Health Center"
        },
        {
            "uuid": "8d872150-c2cc-11de-8d13-0010c6dffd0f",
            "name": "Health District"
        },
        {
            "uuid": "8d871d18-c2cc-11de-8d13-0010c6dffd0f",
            "name": "Mother's Name"
        },
        {
            "uuid": "8d871386-c2cc-11de-8d13-0010c6dffd0f",
            "name": "Race"
        },
        {
            "uuid": "14d4f066-15f5-102d-96e4-000c29c2a5d7",
            "name": "Telephone Number"
        },
        {
            "uuid": "4f07985c-88a5-4abd-aa0c-f3ec8324d8e7",
            "name": "Test Patient"
        },
        {
            "uuid": "6aba6deb-b260-4117-9a50-37c8e1a76a45",
            "name": "Nationality"
        },
        {
            "uuid": "b8cb9abe-f0cd-4b09-b6db-69cd54ba22d7",
            "name": "Legal Consent"
        },
        {
            "uuid": "1dc673bd-1d70-428a-8aae-26d80ccb0e17",
            "name": "Skin color Fitzpatrick"
        },
        {
            "uuid": "2757e503-5453-4cb9-92fe-9339bf60f806",
            "name": "Comments"
        }
    ]
}"""