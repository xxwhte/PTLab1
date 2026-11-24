import sys

import pytest

from src.main import get_path_from_arguments, main


@pytest.fixture()
def correct_arguments_string() -> tuple[list[str], str]:
    return ["-p", "/home/user/file.txt"], "/home/user/file.txt"


@pytest.fixture()
def noncorrect_arguments_string() -> list[str]:
    return ["/home/user/file.txt"]


def test_get_path_from_correct_arguments(
        correct_arguments_string: tuple[list[str], str]) -> None:
    path = get_path_from_arguments(correct_arguments_string[0])
    assert path == correct_arguments_string[1]


def test_get_path_from_noncorrect_arguments(
        noncorrect_arguments_string: list[str]) -> None:
    with pytest.raises(SystemExit) as e:
        get_path_from_arguments(noncorrect_arguments_string[0])
        assert e.type == SystemExit


@pytest.mark.parametrize(("extension", "content"), [
    (".yaml", "- A: {math: 90}\n- B: {math: 100, chemistry: 89}\n"),
    (".YML", "- A: {math: 90}\n- B: {math: 100, chemistry: 89}\n"),
    (".txt", "A\n math:90\nB\n math:100\n chemistry:89\n"),
])
def test_main_prints_results(tmp_path, monkeypatch, capsys,
                             extension: str, content: str) -> None:
    path = tmp_path / f"grades{extension}"
    path.write_text(content, encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["main.py", "-p", str(path)])

    main()

    output = capsys.readouterr().out
    assert "Rating:  {'A': 90.0, 'B': 94.5}" in output
    assert "Количество студентов-отличников: 1" in output
