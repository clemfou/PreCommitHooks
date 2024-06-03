"""Deletes empty lines at the end of a file."""

import os
import sys
from pathlib import Path


def remove_empty_trailing_lines(file_path: Path) -> None:
    """Remove trailing lines."""
    with file_path.open("r+b") as file:
        file.seek(0, os.SEEK_END)
        position = file.tell()

        while position > 0:
            file.seek(position - 1)
            char = file.read(1)

            if char not in (b"\n", b"\r"):
                break

            position -= 1

        file.truncate(position)


def main():
    """Entrypoint."""
    for file in sys.argv[1:]:
        remove_empty_trailing_lines(Path(file))


if __name__ == "__main__":
    main()
