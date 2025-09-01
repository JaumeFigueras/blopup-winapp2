#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

import pytest

test_folder = Path(__file__).parent
project_folder = test_folder.parent

pytest_plugins = [
    'test.fixtures.data_model.person',
    'test.fixtures.data_model.person_name',
    'test.fixtures.data_model.person_address',
    'test.fixtures.data_model.person_attribute',
    'test.fixtures.data_model.person_attribute_type',
    # 'test.fixtures.data_model.person',
    # 'test.fixtures.data_model.person_attribute_type',
    # 'test.fixtures.data_model.person_attribute',
    # 'test.fixtures.data_model.location',
    # 'test.fixtures.data_model.patient',
    # 'test.fixtures.data_model.patient_identifier_type',
    # 'test.fixtures.data_model.patient_identifier',
    # 'test.fixtures.database.sqlite',
    'test.fixtures.ui.application',
    'test.fixtures.ui.dialogs.settings',
    # 'test.fixtures.remote_api.session',
    # 'test.fixtures.remote_api.patient',
    # 'test.fixtures.remote_api.person',
    # 'test.fixtures.remote_api.person_name',
    # 'test.fixtures.remote_api.person_address',
    # 'test.fixtures.blopup_application',
    # 'test.fixtures.patient_document_type',
    # 'test.fixtures.location',
    # 'test.fixtures.session',
    # 'test.fixtures.search_patient',
]


@pytest.fixture(scope='module')
def sqlite_files():
    return [
        str(project_folder) + '/src/data_models/databases/model.sqlite3.sql',
    ]


@pytest.fixture(scope='module')
def sql_data_files():
    return [
        str(project_folder) + '/test/data/application_data.sql',
    ]

