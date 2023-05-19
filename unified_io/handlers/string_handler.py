from pathlib import Path
from typing import Union

from .path_handler import create_path


def read(path: Union[str, Path], encoding: str = "utf-8") -> str:
    """Reads a text file into a single string.

    ```python
    from unified_io import read
    ```

    Args:
        path (Union[str, Path]): File path.

        encoding (str, optional): File encoding. Defaults to "utf-8".

    Returns:
        str: String.
    """
    with open(str(path), "r", encoding=encoding) as f:
        x = f.read()
    return x


def write(x: str, path: Union[str, Path], encoding: str = "utf-8") -> None:
    """Writes a string into a text file.

    ```python
    from unified_io import write
    ```

    Args:
        x (str): String.

        path (Union[str, Path]): File path.

        encoding (str, optional): File encoding. Defaults to "utf-8".
    """
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(str(path), "w", encoding=encoding) as f:
        f.write(x)
