from pathlib import Path
from typing import Dict, Union

import orjson

from .path_handler import create_path


def read_json(path: Union[str, Path]) -> Dict:
    """Reads a JSON file into a dictionary.

    ```python
    from unified_io import read_json
    ```

    Args:
        path (Union[str, Path]): File path.

    Returns:
        Dict: Dictionary.
    """
    with open(str(path), "rb") as f:
        x = orjson.loads(f.read())
    return x


def write_json(x: Dict, path: Union[str, Path], kwargs: Dict = None) -> None:
    """Writes a dictionary into a JSON file.

    ```python
    from unified_io import write_json
    ```

    Args:
        x (Dict): Dictionary.

        path (Union[str, Path]): File path.

        kwargs (Dict, optional): Keyword arguments to pass to `orjson.dumps`. If `None`, `kwargs = {"option": (orjson.OPT_INDENT_2 | orjson.OPT_SERIALIZE_NUMPY)}`. Defaults to None.
    """
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if kwargs is None:
        kwargs = {"option": (orjson.OPT_INDENT_2 | orjson.OPT_SERIALIZE_NUMPY)}

    with open(str(path), "wb") as f:
        f.write(orjson.dumps(x, **kwargs))
