"""Deletes empty lines at the end of a file."""

import tempfile
from pathlib import Path

import pytest

from pre_commit_hooks.generic_fix_end_of_files import remove_empty_trailing_lines


@pytest.mark.parametrize(
    ("initial_content", "expected_content"),
    [
        (b"", b""),
        (b"\n", b"\n"),
        (b"\n\n", b"\n"),
        (b"Hello world\n", b"Hello world\n"),
        (b"Hello world\n\n", b"Hello world\n"),
        (b"Hello world\n\n\n", b"Hello world\n"),
    ],
)
def test_remove_empty_trailing_lines(
    initial_content: bytes,
    expected_content: bytes,
) -> None:
    """Empty lines should be removed."""
    with tempfile.NamedTemporaryFile(delete=False) as temporary_file:
        temporary_file.write(initial_content)
        temporary_file.flush()

        file_path = Path(temporary_file.name)

        try:
            # Ensure that content is as expected before processing
            with file_path.open("rb") as file:
                pre_content = file.read()

                assert pre_content == initial_content

            remove_empty_trailing_lines(file_path)

            with file_path.open("rb") as file:
                content = file.read()

            assert content == expected_content

        finally:
            Path.unlink(file_path)
