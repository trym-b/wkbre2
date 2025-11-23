from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from pathlib import Path
from subprocess import run
from sys import exit
from typing import Callable


@dataclass
class _Formatter:
    format: Callable[[None], None]
    check_format: Callable[[None], None]


def _formatters() -> list[_Formatter]:
    return [
        _Formatter(
            format=format_cmake,
            check_format=check_format_cmake,
        )
    ]


def _repo_root() -> Path:
    return Path(__file__).parent.parent.parent


def _files_to_format(file_extensions: list[str], exact_file_names: list[str]) -> None:
    files_to_format = []
    for file_extension in file_extensions:
        files_to_format.extend(_repo_root().rglob(f"*{file_extension}"))

    for exact_file_name in exact_file_names:
        files_to_format.extend(_repo_root().rglob(exact_file_name))

    files_to_format = list(set(files_to_format))

    return [
        file
        for file in files_to_format
        if not file.is_relative_to(_repo_root() / "build")
    ]


def format_cmake() -> None:
    name = "CMake"
    file_extensions = [".cmake"]
    exact_file_names = ["CMakeLists.txt"]
    files_to_format = " ".join(
        map(
            str,
            _files_to_format(
                file_extensions=file_extensions,
                exact_file_names=exact_file_names,
            ),
        )
    )
    command = f"uv run gersemi --indent 4 --in-place {files_to_format}"
    print(f"Formatting '{name}' files")
    run(
        args=command,
        check=True,
        shell=True,
        text=True,
        capture_output=False,
    )


def check_format_cmake() -> None:
    name = "CMake"
    file_extensions = [".cmake"]
    exact_file_names = ["CMakeLists.txt"]
    files_to_format = " ".join(
        map(
            str,
            _files_to_format(
                file_extensions=file_extensions,
                exact_file_names=exact_file_names,
            ),
        )
    )
    command = f"uv run gersemi --indent 4 --check {files_to_format}"
    print(f"Checking formatting for '{name}' files")
    completed_process = run(args=command, shell=True, text=True, capture_output=True)
    print(f"stdout:\n{completed_process.stdout}")
    print(f"stderr:\n{completed_process.stderr}")
    if "would be reformatted" in completed_process.stderr:
        print(
            f"Formatting check failed, please reformat by calling 'uv run python {Path(__file__).relative_to(_repo_root())}'"
        )
        exit(1)


def _args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--check", required=False, action="store_true")
    return parser.parse_args()


def _format() -> None:
    for formatter in _formatters():
        formatter.format()


def _verify_format() -> None:
    for formatter in _formatters():
        formatter.check_format()


def _main() -> None:
    args = _args()
    if args.check:
        _verify_format()
    else:
        _format()


if __name__ == "__main__":
    _main()
