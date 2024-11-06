from dataclasses import dataclass
from ..classifications import PatitoType
from typing import Optional

@dataclass
class FunctionAttrs:
    signature: Optional[list[PatitoType]] = None
    referent: Optional[str] = None
    