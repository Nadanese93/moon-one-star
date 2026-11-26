"""One-star review of the Moon, for Make.fun entry #199.

Writes the entry text to entry.txt inside the output directory the
harness specifies via MAKEFUN_OUTPUT_DIR (mounted at /output in the
grader sandbox). Deterministic: the same bytes on every run.
"""

import os

ENTRY = "One star. Advertised as cheese. I brought crackers. It was rock. False advertising since 1969."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    encoded = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(encoded)
    # Round-trip verification: read the bytes back from disk and
    # refuse to report success if what landed differs from the entry.
    with open(path, "rb") as f:
        on_disk = f.read()
    if on_disk != encoded:
        raise SystemExit(
            f"entry.txt verification failed: {len(on_disk)} bytes on disk, "
            f"expected {len(encoded)}"
        )


if __name__ == "__main__":
    main()
