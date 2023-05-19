import pickle
from pathlib import Path
from typing import Any, Dict, Union

from .path_handler import create_path


def read_pickle(path: Union[str, Path], kwargs: Dict = None) -> Any:
    """Reads a pickle file.

    ```python
    from unified_io import read_pickle
    ```

    Args:
        path (Union[str, Path]): File path.

        kwargs (Dict, optional): Keyword arguments to pass to [`pickle.load`](https://docs.python.org/3/library/pickle.html#pickle.load). Defaults to None.

    Returns:
        Any: Output.
    """
    kwargs = {} if kwargs is None else kwargs

    with open(str(path), "rb") as f:
        x = pickle.load(f, **kwargs)
    return x


def write_pickle(x: Any, path: Union[str, Path], kwargs: Dict = None) -> None:
    """Writes the input to a pickle file.

    ```python
    from unified_io import write_pickle
    ```

    Args:
        x (Any): Input.

        path (Union[str, Path]): File path.

        kwargs (Dict, optional): Keyword arguments to pass to [`pickle.dump`](https://docs.python.org/3/library/pickle.html#pickle.dump). Defaults to None.
    """
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    kwargs = {} if kwargs is None else kwargs

    with open(str(path), "wb") as f:
        pickle.dump(x, f, **kwargs)
