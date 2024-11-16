from ..classifications import NumericOperator, VariableType

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
    def invalid_operation(cls: 'SemanticError', type_1: VariableType, operator: NumericOperator, type_2: VariableType) -> 'SemanticError':
        return cls(f"semantically invalid operation involving: '{type_1.name}' {operator.name} {type_2.name}")
    
    @classmethod
    def expected_boolean(cls: 'SemanticError', token: str) -> 'SemanticError':
        return cls(f"found non-boolean (0 or 1) where boolean was expected: '{token}'")
    
    @classmethod
    def uninitialized(cls: 'SemanticError', token: str) -> 'SemanticError':
        return cls(f"referencing uninitialized symbol: '{token}'")
    
    @classmethod
    def arity_mismatch(cls: 'SemanticError', function_id: str, provided_arity: int, expected_arity: int) -> 'SemanticError':
        return cls(f"arity mismatch, function with '{function_id}' expected {expected_arity} arguments, {provided_arity} were given")

    @classmethod
    def type_mismatch(cls: 'SemanticError', provided_type: VariableType, expected_type: VariableType) -> 'SemanticError':
        return cls(f"type mismatch, {provided_type.name} was given when {expected_type.name} was expected")

class SyntaxError(Exception):
    def __init__(self, message: str):
        super().__init__(message)