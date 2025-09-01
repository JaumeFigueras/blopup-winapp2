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

class PersonAddressParams(TypedDict):
    open_mrs_uuid: NotRequired[str]
    address: Optional[str]
    city_village: Optional[str]
    state_province: NotRequired[Optional[str]]
    country_code: NotRequired[Optional[str]]
    postal_code: NotRequired[Optional[str]]
    preferred: bool
    person: NotRequired[Union[Person, str]]

class PersonAddress(Base):
    """
    Models the person address subresource in the OpenMRS data model
    """
    __tablename__ = 'person_address'
    open_mrs_uuid: Mapped[str] = mapped_column('open_mrs_uuid', String, primary_key=True)
    address: Mapped[Optional[str]] = mapped_column('address_1', String, default=None, nullable=True)
    city_village: Mapped[Optional[str]] = mapped_column('city_village', String, default=None, nullable=True)
    state_province: Mapped[Optional[str]] = mapped_column('state_province', String, default=None, nullable=True)
    country_code: Mapped[Optional[str]] = mapped_column('country_code', String, default=None, nullable=True)
    postal_code: Mapped[Optional[str]] = mapped_column('postal_code', String, default=None, nullable=True)
    preferred: Mapped[bool] = mapped_column('preferred', Boolean, default=False, nullable=False)
    person_open_mrs_uuid: Mapped[Optional[str]] = mapped_column(ForeignKey("person.open_mrs_uuid"))
    person: Mapped[Person] = relationship(back_populates="addresses")

    def __init__(self, **kwargs: Unpack[PersonAddressParams]) -> None:
        super().__init__()
        for key, value in kwargs.items():  # type: ignore[attr-defined]
            if hasattr(self, key):
                if key == "person" and isinstance(value, str):
                    self.person_open_mrs_uuid = value
                else:
                    setattr(self, key, value)

    @property
    def display(self) -> str:
        txt: str = ""
        txt += self.address + " " if self.address is not None else "- "
        txt += "; " + self.city_village + " " if self.city_village is not None else ";- "
        txt += "; " + self.postal_code if self.postal_code is not None else ";-"
        return txt

    def __str__(self) -> str:
        txt: str = "Address:\n"
        txt += "  UUID: " + (self.open_mrs_uuid if self.open_mrs_uuid is not None else "None") + "\n"
        txt += "  Address: " + (self.address if self.address is not None else "None") + "\n"
        txt += "  City / Village: " + (self.city_village if self.city_village is not None else "None") + "\n"
        txt += "  State / Province: " + (self.state_province if self.state_province is not None else "None") + "\n"
        txt += "  Country code: " + (self.country_code if self.country_code is not None else "None") + "\n"
        txt += "  Postal code: " + (self.postal_code if self.postal_code is not None else "None") + "\n"
        txt += "  Preferred: " + str(self.preferred) + "\n"
        return txt

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, PersonAddress):
            return False
        equal = True
        equal = equal and self.open_mrs_uuid == other.open_mrs_uuid
        equal = equal and self.address == other.address
        equal = equal and self.city_village == other.city_village
        equal = equal and self.state_province == other.state_province
        equal = equal and self.country_code == other.country_code
        equal = equal and self.postal_code == other.postal_code
        equal = equal and self.preferred == other.preferred
        return equal

    @staticmethod
    def object_hook_list_custom(dct: Dict[str, Any]) -> Union[Any, List[PersonAddress]]:
        """
        Decodes a JSON originated dict from an API call to get the address of a person

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: Dict[str, Any]
        :return: Union[Any, PatientAddress]
        """
        if 'results' in dct:
            return dct['results']
        if all(k in dct for k in ('uuid', 'address1', 'cityVillage', 'stateProvince', 'country', 'postalCode',
                                  'preferred')):
            if not dct['voided']:
                elem: PersonAddress = PersonAddress(
                    open_mrs_uuid=dct['uuid'],
                    address=dct['address1'],
                    city_village=dct['cityVillage'],
                    state_province=dct['stateProvince'],
                    country_code=dct['country'],
                    postal_code=dct['postalCode'],
                    preferred=dct['preferred']
                )
                return elem
        return None  # pragma: no cover

    @staticmethod
    def object_hook_element_custom(dct: Dict[str, Any]) -> Union[Any, List[PersonAddress]]:
        """
        Decodes a JSON originated dict from an API call to get the address of a person

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: Dict[str, Any]
        :return: Union[Any, PatientAddress]
        """
        if all(k in dct for k in ('uuid', 'address1', 'cityVillage', 'stateProvince', 'country', 'postalCode',
                                  'preferred', 'voided')):
            if not dct['voided']:
                elem: PersonAddress = PersonAddress(
                    open_mrs_uuid=dct['uuid'],
                    address=dct['address1'],
                    city_village=dct['cityVillage'],
                    state_province=dct['stateProvince'],
                    country_code=dct['country'],
                    postal_code=dct['postalCode'],
                    preferred=dct['preferred']
                )
                return elem
        return None  # pragma: no cover