"""Check if a binary is being committed."""

import sys
from pathlib import Path


def is_binary(file_path: Path) -> bool:
    """Check if the file is a binary."""
    try:
        with file_path.open("rb") as file:
            chunk = file.read(512)

            if b"\0" in chunk:
                return True
        return False

    except IOError:
        return False


def main():
    """Entrypoint."""
    binary_files = [file for file in sys.argv[1:] if is_binary(Path(file))]

    if binary_files:
        for binary_file in binary_files:
            print(f"{binary_file} - is a binary")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
