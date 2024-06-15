"""Deletes empty lines at the end of a file."""

import os
import sys
from pathlib import Path


def remove_empty_trailing_lines(file_path: Path) -> None:
    """Remove trailing lines."""
    with file_path.open("r+b") as file:
        try:
            file.seek(-1, os.SEEK_END)

        except IOError:
            return

        position = file.tell()

        while position > 0:
            file.seek(position - 1)
            char = file.read(1)

            if char not in (b"\n", b"\r"):
                break

            position -= 1

        if position == 0 and file.read(1) in (b"\n", b"\r"):
            file.seek(0)
            file.truncate(0)
            file.write(b"\n")

        else:
            file.seek(position + 1)
            file.truncate()


def main():
    """Entrypoint."""
    for file in sys.argv[1:]:
        remove_empty_trailing_lines(Path(file))


if __name__ == "__main__":
    main()
