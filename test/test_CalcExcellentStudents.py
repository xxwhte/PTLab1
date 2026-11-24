import pytest

from src.CalcExcellentStudents import CalcExcellentStudents
from src.Types import DataType


@pytest.mark.parametrize(("students", "expected"), [
    ({
        "A": [("math", 90), ("chemistry", 90)],
        "B": [("math", 100)],
        "C": [("math", 100), ("chemistry", 89)],
    }, 2),
    ({"A": [("math", 89)]}, 0),
    ({"A": []}, 0),
    ({}, 0),
])
def test_calc(students: DataType, expected: int) -> None:
    assert CalcExcellentStudents(students).calc() == expected
