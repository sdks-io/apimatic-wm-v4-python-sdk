from __future__ import annotations

from typing import TypeAlias

from ..enum_filter2 import EnumFilter2, EnumFilter2Dict
from ..multi_value_filter1 import MultiValueFilter1, MultiValueFilter1Dict
from ..range_filter import RangeFilter, RangeFilterDict

RowFilter1: TypeAlias = EnumFilter2 | RangeFilter | MultiValueFilter1
"""Supertype of all row filters."""

RowFilter1Dict: TypeAlias = EnumFilter2Dict | RangeFilterDict | MultiValueFilter1Dict
