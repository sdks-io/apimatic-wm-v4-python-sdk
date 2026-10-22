from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IssueCategory(str, Enum):
    """Overall SEM eligibility status derived from all issues affecting this item.

    - **NO_ISSUES**: Item has no SEM issues and can be advertised on search engines with full visibility
    - **LIMITED**: Item has issues that reduce its visibility or performance in Search Engine Marketing
    - **BLOCKED**: Item has critical issues that completely prevent it from being advertised on search engines"""

    NO_ISSUES = "NO_ISSUES"
    LIMITED = "LIMITED"
    BLOCKED = "BLOCKED"

    __str__ = str.__str__


IssueCategoryOrStr: TypeAlias = Annotated[IssueCategory | str, open_enum_validator(IssueCategory)]
