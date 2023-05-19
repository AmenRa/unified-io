from pathlib import Path
from typing import Union

import numpy as np

from .path_handler import create_path


def read_numpy(path: Union[str, Path], kwargs: dict = None) -> np.ndarray:
    """Reads a npy file into a Numpy array.

    ```python
    from unified_io import read_numpy
    ```

    Args:
        path (Union[str, Path]): File path.

        kwargs (Dict, optional): Keyword arguments to pass to [`np.load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html). Defaults to None.

    Returns:
        np.ndarray: Numpy Array
    """
    kwargs = {} if kwargs is None else kwargs

    with open(str(path), "rb") as f:
        x = np.load(file=f, **kwargs)
    return x


def write_numpy(x: np.ndarray, path: Union[str, Path], kwargs: dict = None) -> None:
    """Writes a Numpy Array into a npy file.

    ```python
    from unified_io import write_numpy
    ```

    Args:
        x (np.ndarray): Numpy Array.

        path (Union[str, Path]): File path.

        kwargs (Dict, optional): Keyword arguments to pass to [`np.save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html). Defaults to None.
    """
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    kwargs = {} if kwargs is None else kwargs

    with open(str(path), "wb") as f:
        np.save(file=f, arr=x, **kwargs)
