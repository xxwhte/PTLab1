from Types import DataType


class CalcExcellentStudents:
    def __init__(self, data: DataType) -> None:
        self.data = data

    def calc(self) -> int:
        return sum(
            1 for grades in self.data.values()
            if grades and all(score >= 90 for _, score in grades)
        )
