from dataclasses import dataclass
from ..classifications import PatitoType
from typing import Optional

@dataclass
class VariableAttrs:
    variable_type: Optional[PatitoType] = None
    referent: Optional[str] = None
    