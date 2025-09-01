#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations  # Needed to allow returning type of enclosing class PEP 563

from src.data_model import Base
from src.data_model.categories.person_attributes_categories import GenderCategory

from sqlalchemy import Enum
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy.ext.hybrid import hybrid_property

import datetime

from typing import List
from typing import Dict
from typing import Union
from typing import Optional
from typing import Any
from typing import Iterator
from typing import Tuple
from typing import TypedDict
from typing import NotRequired
from typing import Unpack

from typing import TYPE_CHECKING
if TYPE_CHECKING:  # pragma: no cover
    from src.data_model.person_name import PersonName
    from src.data_model.person_address import PersonAddress
    from src.data_model.person_attribute import PersonAttribute

class PersonParams(TypedDict):
    open_mrs_uuid: NotRequired[Optional[str]]
    gender: GenderCategory
    birth_date: Optional[datetime.date]
    birth_date_estimated: bool
    dead: bool
    death_date: NotRequired[Optional[datetime.date]]
    death_date_estimated: NotRequired[bool]
    voided: NotRequired[bool]

class Person(Base):
    """
    Models a OpenMRS Person type
    """
    __tablename__ = 'person'
    open_mrs_uuid: Mapped[str] = mapped_column('open_mrs_uuid', String, primary_key=True)
    names: Mapped[List["PersonName"]] = relationship(back_populates="person")
    gender: Mapped[GenderCategory] = mapped_column('gender', Enum(GenderCategory), default=GenderCategory.N, nullable=False)
    birth_date: Mapped[datetime.date] = mapped_column('date_of_birth', Date, nullable=True)
    birth_date_estimated: Mapped[bool] = mapped_column('birth_date_estimated', Boolean, default=False, nullable=False)
    dead: Mapped[bool] = mapped_column('dead', Boolean, default=False, nullable=False)
    death_date: Mapped[datetime.date] = mapped_column('date_of_death', Date, nullable=True)
    death_date_estimated: Mapped[bool] = mapped_column('death_date_estimated', Boolean, default=False, nullable=False)
    addresses: Mapped[List["PersonAddress"]] = relationship(back_populates="person")
    attributes: Mapped[List["PersonAttribute"]] = relationship(back_populates="person")
    voided: Mapped[bool] = mapped_column('voided', Boolean, default=False, nullable=False)
    class_type: Mapped[str]

    __mapper_args__ = {
        "polymorphic_identity": "person",
        "polymorphic_on": "class_type",
    }

    def __init__(self, **kwargs: Unpack[PersonParams]) -> None:
        super().__init__()
        for key, value in kwargs.items():  # type: ignore[attr-defined]
            if hasattr(self, key):
                setattr(self, key, value)

    @property
    def age(self) -> Union[int, None]:
        """
        Age of the patient calculated from the patient birthdate

        :return: Current age of the patient
        :rtype: int | None
        """
        if self.birth_date is None:
            return None
        today = datetime.date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    @property
    def name(self) -> Union[PersonName, None]:
        if self.names is None or len(self.names) == 0:
            return None
        else:
            for name in self.names:
                if name.preferred:
                    return name
        return None

    @property
    def address(self) -> Union["PersonAddress", None]:
        if self.addresses is None or len(self.addresses) == 0:
            return None
        else:
            for address in self.addresses:
                if address.preferred:
                    return address
        return None

    def __str__(self) -> str:
        txt: str = "Person:\n"
        txt += "  UUID: " + (self.open_mrs_uuid if self.open_mrs_uuid is not None else "None") + "\n"
        txt += "  Gender: " + str(self.gender) + "\n"
        txt += "  Birthday: " + (self.birth_date.isoformat() if self.birth_date is not None else "None") + "\n"
        txt += "  Birthday estimated: " + str(self.birth_date_estimated) + "\n"
        txt += "  Dead: " + str(self.dead) + "\n"
        txt += "  Death date: " + (self.death_date.isoformat() if self.death_date is not None else "None") + "\n"
        txt += "  Death date estimated: " + str(self.death_date_estimated) + "\n"
        if len(self.names) == 0:
            txt += "  Names:\n"
            txt += "    None\n"
        else:
            idx: int = 1
            for name in self.names:
                name_txt: List[str] = str(name).splitlines()[1:]
                txt += "  Name #" + str(idx) + ":\n"
                for line in name_txt:
                    txt += "  " + line + "\n"
                idx += 1
        if len(self.addresses) == 0:
            txt += "  Addresses:\n"
            txt += "    None\n"
        else:
            idx: int = 1
            for address in self.addresses:
                address_txt: List[str] = str(address).splitlines()[1:]
                txt += "  Address #" + str(idx) + ":\n"
                for line in address_txt:
                    txt += "  " + line + "\n"
                idx += 1
        if len(self.attributes) == 0:
            txt += "  Attributes:\n"
            txt += "    None\n"
        else:
            idx: int = 1
            for attribute in self.attributes:
                attribute_txt: List[str] = str(attribute).splitlines()[1:]
                txt += "  Attribute #" + str(idx) + ":\n"
                for line in attribute_txt:
                    txt += "  " + line + "\n"
                idx += 1
        return txt

    def __eq__(self, other: Any) -> bool:
        """
        Tests the equality of two persons

        :param other:
        :return:
        """
        if not isinstance(other, Person):
            return False
        equals: bool = True
        equals = equals and (self.open_mrs_uuid == other.open_mrs_uuid)
        equals = equals and (self.gender == other.gender)
        equals = equals and (self.birth_date == other.birth_date)
        equals = equals and (self.birth_date_estimated == other.birth_date_estimated)
        equals = equals and (self.dead == other.dead)
        equals = equals and (self.death_date == other.death_date)
        equals = equals and (self.death_date_estimated == other.death_date_estimated)
        equals = equals and (self.voided == other.voided)
        equals = equals and (len(self.names) == len(other.names))
        equals = equals and (len(self.addresses) == len(other.addresses))
        equals = equals and (len(self.attributes) == len(other.attributes))
        if equals and len(self.names) > 0:
            all_found: bool = True
            for name in self.names:
                found: bool = False
                for other_name in other.names:
                    if name == other_name:
                        found = True
                all_found = all_found and found
            equals = equals and all_found
        if equals and len(self.addresses) > 0:
            all_found: bool = True
            for address in self.addresses:
                found: bool = False
                for other_address in other.addresses:
                    if address == other_address:
                        found = True
                all_found = all_found and found
            equals = equals and all_found
        if equals and len(self.attributes) > 0:
            all_found: bool = True
            for attribute in self.attributes:
                found: bool = False
                for other_attribute in other.attributes:
                    if attribute == other_attribute:
                        found = True
                all_found = all_found and found
            equals = equals and all_found
        return equals


    @staticmethod
    def object_hook_element_custom(dct: Dict[str, Any]) -> Union[Any, Person]:
        """
        Decodes a JSON originated dict from an API call to get the person

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: Dict[str, Any]
        :return: Union[Any, Person]
        """
        if 'person' in dct:
            return dct['person']
        if all(k in dct for k in ('uuid', 'gender', 'birthdate', 'birthdateEstimated', 'dead', 'deathDate',
                                  'deathdateEstimated', 'voided')):
            elem: Person = Person()
            elem.open_mrs_uuid = dct['uuid']
            elem.gender = GenderCategory(dct['gender'])
            elem.birth_date = datetime.datetime.fromisoformat(dct['birthdate']).date()
            elem.birth_date_estimated = dct['birthdateEstimated']
            elem.dead = dct['dead']
            elem.death_date = None if dct['deathDate'] is None else datetime.datetime.fromisoformat(dct['deathDate']).date()
            elem.death_date_estimated = dct['deathdateEstimated']
            elem.voided = dct['voided']
            return elem
        return None  # pragma: no cover
