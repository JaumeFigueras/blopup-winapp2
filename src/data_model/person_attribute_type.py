#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations  # Needed to allow returning type of enclosing class PEP 563

from src.data_model import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:  # pragma: no cover
    from src.data_model.person_attribute import PersonAttribute

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from typing import List
from typing import Optional
from typing import Dict
from typing import Union
from typing import Any
from typing import TypedDict
from typing import NotRequired
from typing import Unpack


class PersonAttributeTypeParams(TypedDict):
    open_mrs_uuid: NotRequired[Optional[str]]
    name: Optional[str]


class PersonAttributeType(Base):
    __tablename__ = 'person_attribute_type'
    open_mrs_uuid: Mapped[str] = mapped_column('open_mrs_uuid', String, primary_key=True)
    name: Mapped[str] = mapped_column('name', String, default=None, nullable=True)
    values: Mapped[List[PersonAttribute]] = relationship(back_populates="attribute_type", lazy='dynamic')

    def __init__(self, **kwargs: Unpack[PersonAttributeTypeParams]) -> None:
        super().__init__()
        for key, value in kwargs.items():  # type: ignore[attr-defined]
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self) -> str:
        txt: str = "Attribute Type:\n"
        txt += "  UUID: " + (self.open_mrs_uuid if self.open_mrs_uuid is not None else "None") + "\n"
        txt += "  Name: " + (self.name if self.name is not None else "None") + "\n"
        return txt

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, PersonAttributeType):
            return False
        equal = True
        equal = equal and self.open_mrs_uuid == other.open_mrs_uuid
        equal = equal and self.name == other.name
        return equal

    @staticmethod
    def object_hook_list_custom(dct: Dict[str, Any]) -> Union[Any, List[PersonAttributeType]]:
        if 'results' in dct:
            return dct['results']
        if all(k in dct for k in ('uuid', 'name')):
            elem: PersonAttributeType = PersonAttributeType(
                open_mrs_uuid=dct['uuid'],
                name=dct['name'],
            )
            return elem
        return None  # pragma: no cover

