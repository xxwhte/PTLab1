import yaml

from DataReader import DataReader
from Types import DataType


class YamlDataReader(DataReader):
    def read(self, path: str) -> DataType:
        with open(path, encoding="utf-8") as file:
            records = yaml.safe_load(file)

        if records is None:
            return {}
        if not isinstance(records, list):
            raise ValueError("YAML must contain a list of students")

        students: DataType = {}
        for record in records:
            if not isinstance(record, dict) or len(record) != 1:
                raise ValueError("Each YAML entry must describe one student")

            name, grades = next(iter(record.items()))
            if not isinstance(name, str) or not name.strip():
                raise ValueError("Student name must be non-empty text")
            if name in students:
                raise ValueError(f"Duplicate student: {name}")
            if not isinstance(grades, dict) or not grades:
                raise ValueError(f"No grades for student: {name}")
            if any(not isinstance(subject, str) or type(score) is not int
                   for subject, score in grades.items()):
                raise ValueError(f"Expected subject names and scores: {name}")

            students[name] = list(grades.items())
        return students
