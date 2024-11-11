from ..classifications import VariableType

is_numeric = lambda t: t == VariableType.ENTERO or t == VariableType.FLOTANTE
all_numeric = lambda t1, t2: is_numeric(t1) and is_numeric(t2) 
has_float = lambda t1, t2: VariableType.FLOTANTE in (t1, t2)
same_type = lambda t1, t2: t1 == t2

def numeric_strategy(type_1: VariableType, type_2: VariableType) -> VariableType | None:
    if all_numeric(type_1, type_2) and has_float(type_1, type_2):
        return VariableType.FLOTANTE
    elif all_numeric(type_1, type_2):
        return VariableType.ENTERO
    else:
        return None
    
def division_strategy(type_1: VariableType, type_2: VariableType) -> VariableType | None:
    if all_numeric(type_1, type_2):
        return VariableType.FLOTANTE
    else:
        return None
    
def relational_strategy(type_1: VariableType, type_2: VariableType) -> VariableType | None:
    if all_numeric(type_1, type_2):
        return VariableType.ENTERO
    else:
        return None
    
def assignment_strategy(type_1: VariableType, type_2: VariableType) -> VariableType | None:
    if same_type(type_1, type_2):
        return type_1
    else:
        return None
    
def none_strategy(type_1: VariableType, type_2: VariableType) -> VariableType | None:
    return None
    