import gzip
from pathlib import Path
from typing import Any, Callable, Dict, List, Union

import orjson

from .common import apply_callback
from .path_handler import create_path


# String -----------------------------------------------------------------------
def read_gzip(path: Union[str, Path]) -> Any:
    """Reads a gzip file into a string.

    ```python
    from unified_io import read_gzip
    ```

    Args:
        path (Union[str, Path]): File path.

    Returns:
        Any: File contents.
    """
    with gzip.open(str(path), "rt") as f:
        x = f.read()
    return x


def write_gzip(x: str, path: Union[str, Path]) -> None:
    """Writes a string into a gzip file.

    ```python
    from unified_io import read_gzip
    ```

    Args:
        x (str): Input string.

        path (Union[str, Path]): File path.
    """
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with gzip.open(str(path), "wt") as f:
        f.write(x)


# List of Strings --------------------------------------------------------------
def read_gzip_to_generator(path: Union[str, Path], callback: Callable = None):
    # Internal usage
    with gzip.open(str(path), "rt") as f:
        for line in f:
            line = line.strip()
            yield apply_callback(line, callback)


def read_gzip_to_list(path: Union[str, Path], callback: Callable = None):
    # Internal usage
    with gzip.open(str(path), "rt") as f:
        lines = f.read().splitlines()
        return [apply_callback(line, callback) for line in lines]


def read_gzip_list(
    path: Union[str, Path],
    callback: Callable = None,
    generator: bool = False,
) -> List[str]:
    """Reads a gzip file into a list of strings.

    ```python
    from unified_io import read_gzip_list
    ```

    Args:
        path (Union[str, Path]): File path.

        callback (Callable, optional): Callback to apply to each element. Defaults to None.

        generator (bool, optional): Whether to return a generator instead of a list. Defaults to False.

    Returns:
        List: List of strings.
    """
    if generator:
        return read_gzip_to_generator(path, callback)
    else:
        return read_gzip_to_list(path, callback)


def write_gzip_list(
    x: List[str],
    path: Union[str, Path],
    callback: Callable = None,
) -> None:
    """Writes a list of strings into a gzip file.

    ```python
    from unified_io import write_gzip_list
    ```

    Args:
        x (List[str]): List of strings.

        path (Union[str, Path]): File path.

        callback (Callable, optional): Callback to apply to each element before writing. Defaults to None.
    """
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with gzip.open(str(path), "wt") as f:
        for y in x:
            f.write(apply_callback(y, callback) + "\n")


# List of Json -----------------------------------------------------------------
def read_gzip_to_json_generator(path: Union[str, Path], callback: Callable = None):
    # Internal usage
    with gzip.open(str(path), "rb") as f:
        for line in f:
            line = orjson.loads(line)
            yield apply_callback(line, callback)


def read_gzip_to_json_list(path: Union[str, Path], callback: Callable = None):
    # Internal usage
    with gzip.open(str(path), "rb") as f:
        lines = [orjson.loads(line) for line in f]
        return [apply_callback(line, callback) for line in lines]


def read_gzip_json_list(
    path: Union[str, Path],
    callback: Callable = None,
    generator: bool = False,
) -> List[Dict]:
    """Reads a gzipped JSONl file into a list of dictionaries.

    ```python
    from unified_io import read_gzip_json_list
    ```

    Args:
        path (Union[str, Path]): File path.

        callback (Callable, optional): Callback to apply to each element. Defaults to None.

        generator (bool, optional): Whether to return a generator instead of a list. Defaults to False.

    Returns:
        List[Dict]: List of dictionaries.
    """
    if generator:
        return read_gzip_to_json_generator(path, callback)
    else:
        return read_gzip_to_json_list(path, callback)


def write_gzip_json_list(
    x: List[str],
    path: Union[str, Path],
    callback: Callable = None,
) -> None:
    """Writes a list of dictionaries into a a gzipped JSONl file.

    ```python
    from unified_io import write_gzip_json_list
    ```

    Args:
        x (List[str]): List of dictionaries.

        path (Union[str, Path]): File path.

        callback (Callable, optional): Callback to apply to each element before writing. Defaults to None.
    """
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with gzip.open(str(path), "wb") as f:
        for y in x:
            f.write(orjson.dumps(apply_callback(y, callback)) + "\n".encode())
