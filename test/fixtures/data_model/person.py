#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope='session')
def person_element_string() -> str:
    return """
        {
            "uuid": "df290974-a2b3-42dc-96c0-ee3a67842a2f",
            "gender": "F",
            "birthdate": "1973-11-10T00:00:00.000+0000",
            "birthdateEstimated": true,
            "dead": false,
            "deathDate": null,
            "deathdateEstimated": false,
            "voided": false
        }
    """

@pytest.fixture(scope='session')
def person_update_element_string() -> str:
    return """
        {
            "uuid": "df290974-a2b3-42dc-96c0-ee3a67842a2f",
            "display": "100FYG - Rosiy De Palma",
            "identifiers": [
                {
                    "uuid": "cb79c36a-16fa-4a53-a573-bb24fec761ce",
                    "display": "OpenMRS ID = 100FYG",
                    "links": [
                        {
                            "rel": "self",
                            "uri": "http://blopup-dev.upc.edu/openmrs/ws/rest/v1/patient/df290974-a2b3-42dc-96c0-ee3a67842a2f/identifier/cb79c36a-16fa-4a53-a573-bb24fec761ce",
                            "resourceAlias": "identifier"
                        }
                    ]
                },
                {
                    "uuid": "68f5820a-37ea-43d1-9e55-c60e5259df7d",
                    "display": "Spanish - DNI = 12345678q",
                    "links": [
                        {
                            "rel": "self",
                            "uri": "http://blopup-dev.upc.edu/openmrs/ws/rest/v1/patient/df290974-a2b3-42dc-96c0-ee3a67842a2f/identifier/68f5820a-37ea-43d1-9e55-c60e5259df7d",
                            "resourceAlias": "identifier"
                        }
                    ]
                },
                {
                    "uuid": "3675ab08-0b1f-402d-a0b1-87d713fb127c",
                    "display": "CatSalut - CIP = 123456",
                    "links": [
                        {
                            "rel": "self",
                            "uri": "http://blopup-dev.upc.edu/openmrs/ws/rest/v1/patient/df290974-a2b3-42dc-96c0-ee3a67842a2f/identifier/3675ab08-0b1f-402d-a0b1-87d713fb127c",
                            "resourceAlias": "identifier"
                        }
                    ]
                }
            ],
            "person": {
                "uuid": "df290974-a2b3-42dc-96c0-ee3a67842a2f",
                "display": "Rosiy De Palma",
                "gender": "F",
                "age": 49,
                "birthdate": "1972-01-02T00:00:00.000+0000",
                "birthdateEstimated": true,
                "dead": true,
                "deathDate": "2021-02-03T00:00:00.000+0000",
                "causeOfDeath": null,
                "preferredName": {
                    "uuid": "54c3cc06-8c25-4ad6-b8e0-84238a3ce2e7",
                    "display": "Rosiy De Palma",
                    "links": [
                        {
                            "rel": "self",
                            "uri": "http://blopup-dev.upc.edu/openmrs/ws/rest/v1/person/df290974-a2b3-42dc-96c0-ee3a67842a2f/name/54c3cc06-8c25-4ad6-b8e0-84238a3ce2e7",
                            "resourceAlias": "name"
                        }
                    ]
                },
                "preferredAddress": {
                    "uuid": "9040f684-6e84-44b1-9bcd-182b8d167f72",
                    "display": "Carrer de la Rossiy",
                    "links": [
                        {
                            "rel": "self",
                            "uri": "http://blopup-dev.upc.edu/openmrs/ws/rest/v1/person/df290974-a2b3-42dc-96c0-ee3a67842a2f/address/9040f684-6e84-44b1-9bcd-182b8d167f72",
                            "resourceAlias": "address"
                        }
                    ]
                },
                "attributes": [
                    {
                        "uuid": "7b4d6c23-c3bd-4e0e-ab20-ad2aacb527bc",
                        "display": "Nationality = SPAIN",
                        "links": [
                            {
                                "rel": "self",
                                "uri": "http://blopup-dev.upc.edu/openmrs/ws/rest/v1/person/df290974-a2b3-42dc-96c0-ee3a67842a2f/attribute/7b4d6c23-c3bd-4e0e-ab20-ad2aacb527bc",
                                "resourceAlias": "attribute"
                            }
                        ]
                    }
                ],
                "voided": false,
                "birthtime": null,
                "deathdateEstimated": false,
                "links": [
                    {
                        "rel": "self",
                        "uri": "http://blopup-dev.upc.edu/openmrs/ws/rest/v1/person/df290974-a2b3-42dc-96c0-ee3a67842a2f",
                        "resourceAlias": "person"
                    },
                    {
                        "rel": "full",
                        "uri": "http://blopup-dev.upc.edu/openmrs/ws/rest/v1/person/df290974-a2b3-42dc-96c0-ee3a67842a2f?v=full",
                        "resourceAlias": "person"
                    }
                ],
                "resourceVersion": "1.11"
            },
            "voided": false,
            "links": [
                {
                    "rel": "self",
                    "uri": "http://blopup-dev.upc.edu/openmrs/ws/rest/v1/patient/df290974-a2b3-42dc-96c0-ee3a67842a2f",
                    "resourceAlias": "patient"
                },
                {
                    "rel": "full",
                    "uri": "http://blopup-dev.upc.edu/openmrs/ws/rest/v1/patient/df290974-a2b3-42dc-96c0-ee3a67842a2f?v=full",
                    "resourceAlias": "patient"
                }
            ],
            "resourceVersion": "1.8"
        }
    """