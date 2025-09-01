#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations  # Needed to allow returning type of enclosing class PEP 563

from src.data_model import Base
from src.data_model.person import Person

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from typing import List
from typing import Dict
from typing import Union
from typing import Optional
from typing import Any
from typing import TypedDict
from typing import NotRequired
from typing import Unpack


class PersonNameParams(TypedDict):
    open_mrs_uuid: NotRequired[str]
    given_name: Optional[str]
    family_name: Optional[str]
    preferred: Optional[bool]
    person: NotRequired[Union[Person, str]]


class PersonName(Base):
    __tablename__ = 'person_name'
    open_mrs_uuid: Mapped[str] = mapped_column('open_mrs_uuid', String, primary_key=True)
    given_name: Mapped[str] = mapped_column('given_name', String, default=None, nullable=True)
    family_name: Mapped[str] = mapped_column('family_name', String, default=None, nullable=True)
    preferred: Mapped[bool] = mapped_column('preferred', Boolean, default=False, nullable=False)
    person_open_mrs_uuid: Mapped[str] = mapped_column(ForeignKey("person.open_mrs_uuid"))
    person: Mapped[Person] = relationship(back_populates="names")

    def __init__(self, **kwargs: Unpack[PersonNameParams]) -> None:
        super().__init__()
        for key, value in kwargs.items(): # type: ignore[attr-defined]
            if hasattr(self, key):
                if key == "person" and isinstance(value, str):
                    self.person_open_mrs_uuid = value
                else:
                    setattr(self, key, value)

    @property
    def display(self) -> str:
        txt = list()
        txt.append(self.given_name) if self.given_name is not None else None
        txt.append(self.family_name) if self.family_name is not None else None
        return ' '.join(txt)

    def __str__(self) -> str:
        """
        Default string conversion

        :return:  str
        """
        txt: str = "Name:\n"
        txt += "  UUID: " + (self.open_mrs_uuid if self.open_mrs_uuid is not None else "None") + "\n"
        txt += "  Given Name: " + (self.given_name if self.given_name is not None else "None") + "\n"
        txt += "  Family Name: " + (self.family_name if self.family_name is not None else "None") + "\n"
        txt += "  Is the preferred name: " + str(self.preferred) + "\n"
        return txt

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, PersonName):
            return False
        equal = True
        equal = equal and self.open_mrs_uuid == other.open_mrs_uuid
        equal = equal and self.given_name == other.given_name
        equal = equal and self.family_name == other.family_name
        equal = equal and self.preferred == other.preferred
        return equal


    @staticmethod
    def object_hook_list_custom(dct: Dict[str, Any]) -> Union[Any, List[PersonName]]:
        """
        Decodes a JSON originated dict from an API call to get the full name of a person

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: Dict[str, Any]
        :return: Union[Any, PatientName]
        """
        if 'results' in dct:
            return dct['results']
        if all(k in dct for k in ('uuid', 'givenName', 'familyName', 'preferred', 'voided')):
            if not dct['voided']:
                elem: PersonName = PersonName(
                    open_mrs_uuid=dct['uuid'],
                    given_name=dct['givenName'],
                    family_name=dct['familyName'],
                    preferred=dct['preferred'],
                )
                return elem
        return None  # pragma: no cover

    @staticmethod
    def object_hook_element_custom(dct: Dict[str, Any]) -> Union[Any, List[PersonName]]:
        """
        Decodes a JSON originated dict from an API call to get the full name of a person

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: Dict[str, Any]
        :return: Union[Any, PatientName]
        """
        if all(k in dct for k in ('uuid', 'givenName', 'familyName', 'preferred', 'voided')):
            if not dct['voided']:
                elem: PersonName = PersonName(
                    open_mrs_uuid=dct['uuid'],
                    given_name=dct['givenName'],
                    family_name=dct['familyName'],
                    preferred=dct['preferred'],
                )
                return elem
        return None  # pragma: no cover

