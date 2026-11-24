import argparse
import sys
from pathlib import Path

from CalcExcellentStudents import CalcExcellentStudents
from CalcRating import CalcRating
from DataReader import DataReader
from TextDataReader import TextDataReader
from YamlDataReader import YamlDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str,
                        required=True, help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader: DataReader
    if Path(path).suffix.lower() in {".yaml", ".yml"}:
        reader = YamlDataReader()
    else:
        reader = TextDataReader()
    students = reader.read(path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    print("Rating: ", rating)
    excellent_count = CalcExcellentStudents(students).calc()
    print(f"Количество студентов-отличников: {excellent_count}")


if __name__ == "__main__":
    main()
