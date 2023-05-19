import csv
import sys
from pathlib import Path
from typing import Callable, Dict, List, Union

from .common import apply_callback
from .path_handler import create_path


def read_csv_to_generator(
    path: Union[str, Path],
    callback: Callable = None,
    encoding: str = "utf-8",
    kwargs: Dict = None,
):
    # Internal usage
    with open(path, "r", encoding=encoding) as f:
        lines = csv.DictReader(f, **kwargs)
        for line in lines:
            yield apply_callback(line, callback)


def read_csv_to_list(
    path: Union[str, Path],
    callback: Callable = None,
    encoding: str = "utf-8",
    kwargs: Dict = None,
):
    # Internal usage
    with open(path, "r", encoding=encoding) as f:
        x = list(csv.DictReader(f, **kwargs))
    return [apply_callback(y, callback) for y in x]


def read_csv(
    path: Union[str, Path],
    callback: Callable = None,
    generator: bool = False,
    encoding: str = "utf-8",
    kwargs: Dict = None,
) -> List[Dict]:
    """Reads a CSV file into a list of dictionaries.

    ```python
    from unified_io import read_csv
    ```

    Args:
        path (Union[str, Path]): File path.

        callback (Callable, optional): Callback to apply to each element. Defaults to None.

        generator (bool, optional): Whether to return a generator instead of a list. Defaults to False.

        encoding (str, optional): File encoding. Defaults to "utf-8".

        kwargs (Dict, optional): Keyword arguments to pass to [`csv.DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader). Defaults to None.

    Returns:
        List[Dict]: List of dictionaries.
    """
    csv.field_size_limit(sys.maxsize)

    kwargs = {} if kwargs is None else kwargs

    if generator:
        return read_csv_to_generator(path, callback, encoding, kwargs)
    else:
        return read_csv_to_list(path, callback, encoding, kwargs)


def write_csv(
    x: List[Dict],
    path: Union[str, Path],
    callback: Callable = None,
    encoding: str = "utf-8",
    kwargs: Dict = None,
) -> None:
    """Writes a list of dictionaries to a CSV file.

    ```python
    from unified_io import write_csv
    ```

    Args:
        x (List[Dict]): List of dictionaries.

        path (Union[str, Path]): File path.

        callback (Callable, optional): Callback to apply to each element before writing. Defaults to None.

        encoding (str, optional): File encoding. Defaults to "utf-8".

        kwargs (Dict, optional): Keyword arguments to pass to [`csv.DictWriter`](https://docs.python.org/3/library/csv.html#csv.DictWriter). Defaults to None.
    """
    kwargs = {} if kwargs is None else kwargs

    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(str(path), "w", encoding=encoding, newline="") as f:
        keys = list(x[0])
        dict_writer = csv.DictWriter(f, keys, **kwargs)
        dict_writer.writeheader()
        dict_writer.writerows([apply_callback(y, callback) for y in x])
