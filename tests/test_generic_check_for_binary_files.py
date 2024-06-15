"""Check if a binary is being committed."""
# ruff: noqa: FBT001

import tempfile
from pathlib import Path

import pytest

from pre_commit_hooks.generic_check_for_binary_files import is_binary


@pytest.mark.parametrize(
    ("file_content", "expected_result"),
    [
        (b"", False),
        (b"Hello World\n", False),
        (b"\n", False),
        (b"\x00\x01\x02\x03", True),
    ],
)
def test_is_binary(file_content: bytes, expected_result: bool) -> None:
    """Binary files should be detected."""
    with tempfile.NamedTemporaryFile(delete=False) as temporary_file:
        temporary_file.write(file_content)
        temporary_file.flush()

        file_path = Path(temporary_file.name)

        assert is_binary(file_path) == expected_result
