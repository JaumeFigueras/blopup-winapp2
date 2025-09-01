#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations  # Needed to allow returning type of enclosing class PEP 563

from src.data_model import Base
from src.data_model.person import Person
from src.data_model.person_attribute_type import PersonAttributeType

from sqlalchemy import ForeignKey
from sqlalchemy import String
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


class PersonAttributeParams(TypedDict):
    open_mrs_uuid: NotRequired[Optional[str]]
    value: Optional[str]
    attribute_type: NotRequired[Union[PersonAttributeType, str]]
    person: NotRequired[Union[Person, str]]

class PersonAttribute(Base):
    """
    Models the person attribute subresource in the OpenMRS data model
    """
    __tablename__ = 'person_attribute'
    open_mrs_uuid: Mapped[str] = mapped_column('open_mrs_uuid', String, primary_key=True)
    value: Mapped[str] = mapped_column('value', String, nullable=False)
    attribute_type_open_mrs_id: Mapped[str] = mapped_column(ForeignKey("person_attribute_type.open_mrs_uuid"))
    attribute_type: Mapped[PersonAttributeType] = relationship(back_populates='values')
    person_open_mrs_uuid: Mapped[str] = mapped_column(ForeignKey("person.open_mrs_uuid"))
    person: Mapped[Person] = relationship(back_populates="attributes")

    def __init__(self, **kwargs: Unpack[PersonAttributeParams]) -> None:
        super().__init__()
        for key, value in kwargs.items():  # type: ignore[attr-defined]
            if hasattr(self, key):
                if key == "person" and isinstance(value, str):
                    self.person_open_mrs_uuid = value
                elif key == "attribute_type" and isinstance(value, str):
                    self.attribute_type_open_mrs_id = value
                else:
                    setattr(self, key, value)


    def __str__(self) -> str:
        txt: str = "Attribute:\n"
        txt += "  UUID: " + (self.open_mrs_uuid if self.open_mrs_uuid is not None else "None") + "\n"
        txt += "  Attribute type name: " + (self.attribute_type.name if self.attribute_type is not None else "None") + "\n"
        txt += "  Value: " + (self.value if self.value is not None else "None") + "\n"
        return txt

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, PersonAttribute):
            return False
        equal = True
        equal = equal and self.open_mrs_uuid == other.open_mrs_uuid
        equal = equal and self.value == other.value
        return equal

    @staticmethod
    def object_hook_list_custom(dct: Dict[str, Any]) -> Union[Any, List[PersonAttribute]]:
        """
        Decodes a JSON originated dict from an API call to get the address of a person

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: Dict[str, Any]
        :return: Union[Any, PatientAddress]
        """
        if 'results' in dct:
            return dct['results']
        if all(k in dct for k in ('uuid', 'name')):
            return dct
        if (all(k in dct for k in ('uuid', 'value', 'attributeType')) and
                all(k in dct['attributeType'] for k in ('uuid', 'name'))):
            elem: PersonAttribute = PersonAttribute(
                open_mrs_uuid=dct['uuid'],
                value=dct['value'],
                attribute_type=dct['attributeType']['uuid']
            )
            return elem
        return None  # pragma: no cover
