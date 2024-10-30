import pytest
from ...src.semantics.semantic_cube import SemanticCube
from ...src.classifications import PatitoType
from ...src.classifications import PatitoOperator

@pytest.fixture
def cube() -> SemanticCube:
    return SemanticCube()

@pytest.mark.parametrize('type_1, oper, type_2, result_type', [
    (PatitoType.ENTERO, PatitoOperator.SUMA, PatitoType.FLOTANTE, PatitoType.FLOTANTE),
    (PatitoType.ENTERO, PatitoOperator.SUMA, PatitoType.ENTERO, PatitoType.ENTERO),
    (PatitoType.FLOTANTE, PatitoOperator.SUMA, PatitoType.ENTERO, PatitoType.FLOTANTE),
    (PatitoType.ENTERO, PatitoOperator.DIVISION, PatitoType.ENTERO, PatitoType.FLOTANTE),
    (PatitoType.FLOTANTE, PatitoOperator.MAYOR_A, PatitoType.FLOTANTE, PatitoType.ENTERO),
    (PatitoType.ENTERO, PatitoOperator.IGUALDAD, PatitoType.FLOTANTE, PatitoType.ENTERO),
])
def test_get_result_type(cube: SemanticCube, type_1: PatitoType, oper: PatitoOperator, type_2: PatitoType, result_type: PatitoType) -> None:
    assert cube.get_result_type(type_1, type_2, oper) == result_type

