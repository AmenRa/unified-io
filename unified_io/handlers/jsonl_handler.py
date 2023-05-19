from pathlib import Path
from typing import Callable, Dict, List, Union

import orjson

from .common import apply_callback
from .path_handler import create_path


def read_jsonl_to_generator(path: Union[str, Path], callback: Callable = None):
    # Internal usage
    with open(str(path), "rb") as f:
        for line in f:
            line = orjson.loads(line)
            yield apply_callback(line, callback)


def read_jsonl_to_list(path: Union[str, Path], callback: Callable = None):
    # Internal usage
    with open(str(path), "rb") as f:
        lines = [orjson.loads(line) for line in f]
        return [apply_callback(line, callback) for line in lines]


def read_jsonl(
    path: Union[str, Path],
    callback: Callable = None,
    generator: bool = False,
) -> List[Dict]:
    """Reads a JSONl file into a list of dictionaries.

    ```python
    from unified_io import read_jsonl
    ```

    Args:
        path (Union[str, Path]): File path.

        callback (Callable, optional): Callback to apply to each element. Defaults to None.

        generator (bool, optional): Whether to return a generator. Defaults to False.

    Returns:
        List[Dict]: List of dictionaries.
    """
    if generator:
        return read_jsonl_to_generator(path, callback)
    else:
        return read_jsonl_to_list(path, callback)


def write_jsonl(
    x: List[Dict],
    path: Union[str, Path],
    callback: Callable = None,
    kwargs: Dict = None,
) -> None:
    """Writes a list of dictionaries into a JSONL file.

    ```python
    from unified_io import write_jsonl
    ```

    Args:
        x (List[Dict]): List of dictionaries.

        path (Union[str, Path]): File path.

        callback (Callable, optional): Callback to apply to each element.
        Defaults to None.

        kwargs (Dict, optional): Keyword arguments to pass to `orjson.dumps`. If `None`, `kwargs = {"option": (orjson.OPT_SERIALIZE_NUMPY)}`. Defaults to None.
    """
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if kwargs is None:
        kwargs = {"option": orjson.OPT_SERIALIZE_NUMPY}

    with open(str(path), "wb") as f:
        for y in x:
            f.write(orjson.dumps(apply_callback(y, callback), **kwargs) + "\n".encode())
