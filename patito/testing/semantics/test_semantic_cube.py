import pytest
from ...src.semantics.semantic_cube import SemanticCube
from ...src.classifications import VariableType
from ...src.classifications import NumericOperator

@pytest.fixture
def cube() -> SemanticCube:
    return SemanticCube()

@pytest.mark.parametrize('type_1, oper, type_2, result_type', [
    (VariableType.ENTERO, NumericOperator.SUMA, VariableType.FLOTANTE, VariableType.FLOTANTE),
    (VariableType.ENTERO, NumericOperator.SUMA, VariableType.ENTERO, VariableType.ENTERO),
    (VariableType.FLOTANTE, NumericOperator.SUMA, VariableType.ENTERO, VariableType.FLOTANTE),
    (VariableType.ENTERO, NumericOperator.DIVISION, VariableType.ENTERO, VariableType.FLOTANTE),
    (VariableType.FLOTANTE, NumericOperator.MAYOR_A, VariableType.FLOTANTE, VariableType.ENTERO),
    (VariableType.ENTERO, NumericOperator.IGUALDAD, VariableType.FLOTANTE, VariableType.ENTERO),
    (VariableType.ENTERO, NumericOperator.ASIGNACION, VariableType.FLOTANTE, None),
    (VariableType.ENTERO, NumericOperator.ASIGNACION, VariableType.ENTERO, VariableType.ENTERO),
])
def test_get_result_type(cube: SemanticCube, type_1: VariableType, oper: NumericOperator, type_2: VariableType, result_type: VariableType | None) -> None:
    assert cube.get_result_type(oper, type_1, type_2) == result_type
