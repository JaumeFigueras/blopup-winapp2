#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations  # Needed to allow returning type of enclosing class PEP 563

from src.data_model import Base
from src.data_model.person import Person
from src.data_model.person import PersonParams

from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

import datetime

from typing import Optional
from typing import Union
from typing import TypedDict
from typing import NotRequired
from typing import Unpack

class UserParams(PersonParams):
    username: Optional[str]
    password: Optional[str]

class User(Person):
    """
    Class to model a user. Is using SQLAlchemy for future database usage
    """
    __tablename__ = 'user'
    # Data
    open_mrs_uid: Mapped[str] = mapped_column(ForeignKey("person.open_mrs_uuid"), primary_key=True)
    username: Mapped[str] = mapped_column('username', String, nullable=False)
    password: Mapped[str] = mapped_column('password', String, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "user",
    }

    def __init__(self,**kwargs: Unpack[UserParams]) -> None:
        super().__init__(**kwargs)
        for key, value in kwargs.items():
            if hasattr(self, key) and not Base.is_defined_in_parents(User, key):
                setattr(self, key, value)


    def __str__(self) -> str:
        """
        Convert a user to string

        :return: str
        """
        txt: str = super().__str__()
        txt += "User:\n"
        txt += "  Username: " + (self.username if self.username is not None else "None") + "\n"
        txt += "  Password: " + (self.password if self.password is not None else "None") + "\n"
        return txt

    def __eq__(self, other) -> bool:
        """
        Tests the equality of two users

        :param other:
        :return: True if both users are identical, False otherwise
        :rtype: bool
        """
        equals: bool = super().__eq__(other)
        if not equals or not isinstance(other, User):
            return False
        equals = equals and (self.username == other.username)
        equals = equals and (self.password == other.password)
        return equals
