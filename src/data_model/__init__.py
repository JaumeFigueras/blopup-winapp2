#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):

    @staticmethod
    def is_defined_in_parents(cls, attr):
        return any(attr in base.__dict__ for base in cls.__bases__)

from src.data_model.person import Person
from src.data_model.person_name import PersonName
from src.data_model.person_address import PersonAddress
from src.data_model.person_attribute import PersonAttribute

from src.data_model.person_attribute_type import PersonAttributeType