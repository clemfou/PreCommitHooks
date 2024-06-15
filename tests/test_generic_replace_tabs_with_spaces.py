"""Replace tabs with spaces."""

import tempfile
from pathlib import Path

import pytest

from pre_commit_hooks.generic_replace_tabs_with_spaces import replace_tabs_with_spaces


@pytest.mark.parametrize(
    ("initial_content", "expected_content", "shiftwidth"),
    [
        (b"", b"", 4),
        (b"Hello\tWorld", b"Hello  World", 2),
        (b"Hello\tWorld", b"Hello    World", 4),
        (b"\tHello World", b"  Hello World", 2),
        (b"\tHello World", b"    Hello World", 4),
        (b"\t\tHello World", b"    Hello World", 2),
        (b"\tHello\tWorld", b"  Hello  World", 2),
    ],
)
def test_replace_tabs_with_spaces(
    initial_content: bytes, expected_content: bytes, shiftwidth: int,
) -> None:
    """Tabs should be replaced with spaces."""
    with tempfile.NamedTemporaryFile(delete=False) as temporary_file:
        temporary_file.write(initial_content)
        temporary_file.flush()

        file_path = Path(temporary_file.name)

        try:
            replace_tabs_with_spaces(file_path, shiftwidth)

            with file_path.open("rb") as file:
                content = file.read()

            assert content == expected_content

        finally:
            Path.unlink(file_path)
