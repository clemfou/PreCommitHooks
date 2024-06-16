"""Wrapper around packer fmt command."""

import subprocess
import sys
from pathlib import Path


def run_packer_fmt(file_path: Path) -> None:
    """Run the packer fmt command."""
    try:
        subprocess.run(["/usr/bin/packer", "fmt", file_path], stderr=subprocess.PIPE, check=True)

    except subprocess.CalledProcessError as err:
        sys.exit(1)
        print(err.stderr.decode())


def main() -> None:
    """Entrypoint."""
    for file in sys.argv[1:]:
        run_packer_fmt(Path(file))


if __name__ == "__main__":
    main()
