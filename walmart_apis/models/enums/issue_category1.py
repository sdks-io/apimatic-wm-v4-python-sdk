from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IssueCategory1(str, Enum):
    """Issue severity category.

    - **BLOCKED**: Item cannot be advertised
    - **LIMITED**: Item has reduced visibility or performance
    - **NO_ISSUES**: Item has no SEM eligibility issues"""

    BLOCKED = "BLOCKED"
    LIMITED = "LIMITED"
    NO_ISSUES = "NO_ISSUES"

    __str__ = str.__str__


IssueCategory1OrStr: TypeAlias = Annotated[IssueCategory1 | str, open_enum_validator(IssueCategory1)]
