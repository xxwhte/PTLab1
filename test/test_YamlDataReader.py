import pytest
import yaml

from src.YamlDataReader import YamlDataReader


def test_read_yaml(tmp_path) -> None:
    path = tmp_path / "data.yaml"
    path.write_text(
        "- Иванов Иван Иванович:\n"
        "    математика: 90\n"
        "    литература: 100\n"
        "- Петров Петр Петрович:\n"
        "    химия: 89\n",
        encoding="utf-8",
    )

    assert YamlDataReader().read(str(path)) == {
        "Иванов Иван Иванович": [("математика", 90), ("литература", 100)],
        "Петров Петр Петрович": [("химия", 89)],
    }


@pytest.mark.parametrize("content", ["", "[]"])
def test_read_empty_yaml(tmp_path, content: str) -> None:
    path = tmp_path / "empty.yaml"
    path.write_text(content, encoding="utf-8")

    assert YamlDataReader().read(str(path)) == {}


@pytest.mark.parametrize("content", [
    "Student: {math: 90}",
    "- Student",
    "- {Student: {math: 90}, Other: {math: 95}}",
    "- {12: {math: 90}}",
    "- {'': {math: 90}}",
    "- {Student: {math: 90}}\n- {Student: {math: 95}}",
    "- {Student: [90]}",
    "- {Student: {}}",
    "- {Student: {1: 90}}",
    "- {Student: {math: true}}",
    "- {Student: {math: '90'}}",
])
def test_read_invalid_structure(tmp_path, content: str) -> None:
    path = tmp_path / "invalid.yaml"
    path.write_text(content, encoding="utf-8")

    with pytest.raises(ValueError):
        YamlDataReader().read(str(path))


def test_read_invalid_yaml(tmp_path) -> None:
    path = tmp_path / "invalid.yaml"
    path.write_text("- Student: [", encoding="utf-8")

    with pytest.raises(yaml.YAMLError):
        YamlDataReader().read(str(path))
