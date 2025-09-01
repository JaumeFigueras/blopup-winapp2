#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations  # Needed to allow returning type of enclosing class PEP 563

import enum

from PyQt5.QtCore import QT_TR_NOOP, QCoreApplication


class GenderCategory(enum.StrEnum):
    """
    Enum to model the different gender types OpenMRS has in the system
    """
    M = 'M'  # Male
    F = 'F'  # Female
    N = 'N'  # Undefined

    def __str__(self) -> str:
        if self.value == 'M':
            return QCoreApplication.translate('PersonAttributes', 'Male')
        elif self.value == 'F':
            return QCoreApplication.translate('PersonAttributes', 'Female')
        else:
            return QCoreApplication.translate('PersonAttributes', 'Undefined gender')


class HomelessnessCategory(enum.StrEnum):
    UNDEFINED = 'Undefined'
    STREET_OR_PUBLIC_SPACE = 'Street or public space'
    NIGHT_SHELTER = 'Night shelter'
    TEMPORAL_SHELTER = 'Temporal shelter'
    WOMEN_SHELTER = 'Women shelter'
    IMMIGRANTS_SHElTER = 'Immigrants Shelter'
    ASSISTED_HOUSING = 'Assisted housing'
    FAMILY_FRIENDS_NO_LEGAL_RENT = 'Family, friends or no legal rent'
    EVICTION_PENDING = 'Eviction pending'
    VIOLENCE_MENACE = 'Violence menace'
    TEMPORAL_STRUCTURE_OR_HUT = 'Temporal structure or hut'
    NOT_SUITABLE_HOUSING = 'Not suitable housing'
    OVERCROWDED_HOUSING = 'Overcrowded housing'

    def __str__(self):
        return QCoreApplication.translate('PersonAttributes', self.value.name)


class SkinColourCategory(enum.StrEnum):
    """
    Enum to model the different skin colour types
    """
    UNDEFINED = 'Undefined colour'
    I_II_III = 'I, II, III'
    IV = 'IV'
    V_VI = 'V, VI'

    def __str__(self) -> str:
        return QCoreApplication.translate('PersonAttributes', self.value.name)


