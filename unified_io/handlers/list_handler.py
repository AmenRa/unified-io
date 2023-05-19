from pathlib import Path
from typing import Callable, List, Union

from .common import apply_callback
from .path_handler import create_path


def read_file_to_generator(
    path: Union[str, Path],
    callback: Callable = None,
    encoding: str = "utf-8",
):
    # Internal usage
    with open(str(path), "r", encoding=encoding) as f:
        for line in f:
            line = line.strip()
            yield callback(line) if callback is not None else line


def read_file_to_list(
    path: Union[str, Path],
    callback: Callable = None,
    encoding: str = "utf-8",
):
    # Internal usage
    with open(str(path), "r", encoding=encoding) as f:
        lines = f.read().splitlines()
        lines = [apply_callback(line, callback) for line in lines]
        return lines


def read_list(
    path: Union[str, Path],
    callback: Callable = None,
    generator: bool = False,
    encoding: str = "utf-8",
) -> List[str]:
    """Reads the lines of a text file into a list of strings.

    ```python
    from unified_io import read_list
    ```

    Args:
        path (Union[str, Path]): File path.

        callback (Callable, optional): Callback to apply to each element. Defaults to None.

        generator (bool, optional): Whether to return a generator. Defaults to False.

        encoding (str, optional): File encoding. Defaults to "utf-8".

    Returns:
        List[str]: List of strings.
    """
    if generator:
        return read_file_to_generator(path, callback, encoding)
    else:
        return read_file_to_list(path, callback, encoding)


def write_list(
    x: List[str],
    path: Union[str, Path],
    callback: Callable = None,
    encoding: str = "utf-8",
) -> None:
    """Writes a list of strings into a text file.

    ```python
    from unified_io import write_list
    ```

    Args:
        x (List[str]): List of strings.

        path (Union[str, Path]): File path.

        callback (Callable, optional): Callback to apply to each element. Defaults to None.

        encoding (str, optional): File encoding. Defaults to "utf-8".
    """
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(str(path), "w", encoding=encoding) as f:
        for y in x:
            f.write(apply_callback(y, callback) + "\n")
