from ..classifications import NumericOperator, VariableType

class SemanticException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

    @classmethod
    def undeclared_symbol(cls: 'SemanticException', token: str) -> 'SemanticException':
        return cls(f"encountered an undeclared symbol: '{token}'")
    
    @classmethod
    def redeclaration(cls: 'SemanticException', token: str) -> 'SemanticException':
        return cls(f"redeclaration of the symbol: '{token}'")
    
    @classmethod
    def invalid_operation(cls: 'SemanticException', type_1: VariableType, operator: NumericOperator, type_2: VariableType) -> 'SemanticException':
        return cls(f"semantically invalid operation involving: '{type_1.name}' {operator.name} {type_2.name}")
    
    @classmethod
    def expected_boolean(cls: 'SemanticException', token: str) -> 'SemanticException':
        return cls(f"found non-boolean (0 or 1) where boolean was expected: '{token}'")
    
    @classmethod
    def uninitialized(cls: 'SemanticException', token: str) -> 'SemanticException':
        return cls(f"referencing uninitialized symbol: '{token}'")
    
    @classmethod
    def arity_mismatch(cls: 'SemanticException', function_id: str, provided_arity: int, expected_arity: int) -> 'SemanticException':
        return cls(f"arity mismatch, function with '{function_id}' expected {expected_arity} arguments, {provided_arity} were given")

    @classmethod
    def type_mismatch(cls: 'SemanticException', provided_type: VariableType, expected_type: VariableType) -> 'SemanticException':
        return cls(f"type mismatch, {provided_type.name} was given when {expected_type.name} was expected")
    
    @classmethod
    def stack_overflow(cls: 'SemanticException', max_num_calls: int) -> 'SemanticException':
        return cls(f"stack overflow, the maximum number of active functions calls {max_num_calls} was exceeded")

class SyntaxException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

    @classmethod
    def syntax(cls: 'SyntaxException', msg: str, location: tuple[int, int]) -> 'SyntaxException':
        return cls(f"syntax error: '{msg}' at {location}")