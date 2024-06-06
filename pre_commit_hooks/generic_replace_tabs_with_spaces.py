"""Replace tabs with spaces."""

import argparse
from pathlib import Path


def replace_tabs_with_spaces(file_path: Path, shiftwidth: int):
    """Replace tabs with spaces."""
    try:
        with file_path.open("r+") as file:
            content = file.readlines()
            file.seek(0)

            for line in content:
                file.write(line.replace("\t", " " * shiftwidth))
            file.truncate()

    except Exception as e:
        print(f"Error while processing {file_path}: {e}")


def main():
    """Entrypoint."""
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", type=Path, nargs="*")
    parser.add_argument("--shiftwidth", default=4)

    args = parser.parse_args()

    for filename in args.filenames:
        replace_tabs_with_spaces(filename, args.shiftwidth)


if __name__ == "__main__":
    main()
