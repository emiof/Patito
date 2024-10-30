from ..classifications import PatitoType
from ..classifications import PatitoOperator

is_numeric = lambda t: t == PatitoType.ENTERO or t == PatitoType.FLOTANTE
all_numeric = lambda t1, t2: is_numeric(t1) and is_numeric(t2) 
has_float = lambda t1, t2: PatitoType.FLOTANTE in (t1, t2)

def numeric_strategy(type_1: PatitoType, type_2: PatitoType) -> PatitoType | None:
    if all_numeric(type_1, type_2) and has_float(type_1, type_2):
        return PatitoType.FLOTANTE
    elif all_numeric(type_1, type_2):
        return PatitoType.ENTERO
    else:
        return None
    
def division_strategy(type_1: PatitoType, type_2: PatitoType) -> PatitoType | None:
    if all_numeric(type_1, type_2):
        return PatitoType.FLOTANTE
    else:
        return None
    
def relational_strategy(type_1: PatitoType, type_2: PatitoType) -> PatitoType | None:
    if all_numeric(type_1, type_2):
        return PatitoType.ENTERO
    else:
        return None
    
def none_strategy(type_1: PatitoType, type_2: PatitoType) -> PatitoType | None:
    return None
    