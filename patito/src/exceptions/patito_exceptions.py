from ..classifications import PatitoOperator, PatitoType

class SemanticError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

    @classmethod
    def undeclared_symbol(cls: 'SemanticError', token: str) -> 'SemanticError':
        return cls(f"encountered an undeclared symbol: '{token}'")
    
    @classmethod
    def redeclaration(cls: 'SemanticError', token: str) -> 'SemanticError':
        return cls(f"redeclaration of the symbol: '{token}'")
    
    @classmethod
    def invalid_operation(cls: 'SemanticError', type_1: PatitoType, operator: PatitoOperator, type_2: PatitoType) -> 'SemanticError':
        return cls(f"semantically invalid operation involving: '{type_1.name}' {operator.name} {type_2.name}")
    
    @classmethod
    def expected_boolean(cls: 'SemanticError', token: str) -> 'SemanticError':
        return cls(f"found non-boolean (0 or 1) where boolean was expected: '{token}'")

class SyntaxError(Exception):
    def __init__(self, message: str):
        super().__init__(message)