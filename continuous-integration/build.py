from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from subprocess import run
from os import environ


@dataclass
class _Compiler:
    name: str
    tool_path: Path


@dataclass
class _Platform:
    name: str


_SUPPORTED_COMPILERS = (
    _Compiler(name="gcc", tool_path="g++"),
    _Compiler(name="msvc", tool_path="msvc"),
)
_SUPPORTED_PLATFORMS = (_Platform(name="ubuntu-24.04"), _Platform(name="windows"))


def _repo_root() -> Path:
    return Path(__file__).parent.parent


def _select_compiler_from_string(string: str) -> _Compiler:
    for compiler in _SUPPORTED_COMPILERS:
        if compiler.name == string:
            return compiler
    raise ValueError(f"No compiler name matches: '{string}'")


def _select_platform_from_string(string: str) -> _Platform:
    for platform in _SUPPORTED_PLATFORMS:
        if platform.name == string:
            return platform
    raise ValueError(f"No platform name matches: '{string}'")


def _args() -> tuple[_Compiler, _Platform]:
    parser = ArgumentParser()
    parser.add_argument(
        "--compiler",
        choices=[compiler.name for compiler in _SUPPORTED_COMPILERS],
        required=True,
    )
    parser.add_argument(
        "--platform",
        choices=[platform.name for platform in _SUPPORTED_PLATFORMS],
        required=True,
    )
    arguments = parser.parse_args()
    compiler = _select_compiler_from_string(arguments.compiler)
    platform = _select_platform_from_string(arguments.platform)
    return (compiler, platform)


def _main() -> None:
    selected_compiler, selected_platform = _args()

    build_directory = (
        _repo_root() / "build" / selected_platform.name / selected_compiler.name
    )

    environment = environ.copy()
    vcpkg_root = _repo_root() / "build/3rdParty/vcpkg/"
    environment["PATH"] = f"{environment['PATH']}:{vcpkg_root}"

    cmake_configure_command = (
        "cmake"
        f" --preset={selected_platform.name}"
        f' -B "{build_directory}"'
        f" -DCMAKE_CXX_COMPILER={selected_compiler.tool_path}"
    )
    run(
        cmake_configure_command,
        capture_output=False,
        check=True,
        shell=True,
        env=environment,
    )

    cmake_build_command = f"cmake --build {build_directory}"
    print(f"Building with {selected_compiler.name}")
    run(
        cmake_build_command,
        capture_output=False,
        check=True,
        shell=True,
        env=environment,
    )


if __name__ == "__main__":
    _main()
