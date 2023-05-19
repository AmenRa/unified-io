from pathlib import Path
from typing import Any, Union

import lz4.frame


def read_lz4(path: Union[str, Path]) -> Any:
    """Reads a lz4 file.

    ```python
    from unified_io import read_lz4
    ```

    Args:
        path (str): File path.

    Returns:
        Any: Output.
    """
    with lz4.frame.open(str(path), mode="rb") as f:
        x = lz4.frame.decompress(f.read())

    return x


def write_lz4(x: bytes, path: Union[str, Path]) -> None:
    """Writes bytes into a lz4 file.

    ```python
    from unified_io import write_lz4
    ```

    Args:
        x (bytes): Input bytes.

        path (Union[str, Path]): File path.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with lz4.frame.open(str(path), mode="wb") as f:
        f.write(lz4.frame.compress(x, compression_level=16))
