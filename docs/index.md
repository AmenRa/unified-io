<p align="center">
  <!-- Python -->
  <a href="https://www.python.org" alt="Python">
      <img src="https://badges.aleen42.com/src/python.svg" />
  </a>
  <!-- Version -->
  <a href="https://badge.fury.io/py/unified-io"><img src="https://badge.fury.io/py/unified-io.svg" alt="PyPI version" height="18"></a>
  <!-- Black -->
  <a href="https://github.com/psf/black" alt="Code style: black">
      <img src="https://img.shields.io/badge/code%20style-black-000000.svg" />
  </a>
  <!-- License -->
  <a href="https://lbesson.mit-license.org/"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  </a>
</p>

## ⚡️ Introduction

[unified-io](https://github.com/AmenRa/unified-io) is a Python utility that attempts to unify several I/O operations (i.e., read/write data in different formats) under a similar interface while making them more concise and user-friendly.

The library provides a unified interface for reading/writing files, which is based on the following principles:  

- Read/write interfaces consist of concise functions with similar signatures.  
- Read/write interfaces allows passing keyword arguments to the underlying I/O functions to preserve flexibility.  
- Read operations can be performed lazily using generators.  
- Before reading/writing, the user can specify a callback function that will be applied to each element of the data stream.  
- _read_ functions have _load_ aliases (e.g., `read_csv` has a `load_csv` alias) and _write_ functions have _save_ aliases (e.g., `write_csv` has a `save_csv` alias.  
- Use very efficient stuff for each format (e.g., [`orjson`](https://github.com/ijl/orjson) for `json` files). Suggestions are welcome!

## ✨ Supported formats

- [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) and similar formats (e.g., TSV, PSV, etc.)
- [GZIP](https://en.wikipedia.org/wiki/Gzip)
- [JSON](https://en.wikipedia.org/wiki/JSON)
- [JSONl](https://jsonlines.org)
- [LZ4](https://en.wikipedia.org/wiki/LZ4_(compression_algorithm))
- [Numpy](https://numpy.org) (`.npy`)
- [Pickle](https://docs.python.org/3/library/pickle.html)
- [Text](https://en.wikipedia.org/wiki/Text_file)

## 🔌 Requirements
```
python>=3.7
```

## 💾 Installation
```bash
pip install unified-io
```

## 💡 Examples

The API is designed to be as simple as possible. For example, the following code snippet reads a CSV file, applies a callback function to each element of the data stream, and writes the result to a JSONl file:
```python
from unified_io import read_csv, write_jsonl

def callback(x):
    return {"id": x["id"], "title": x["title"].lower()}

# Using a generator we avoid loading the entire file into memory
data = read_csv('input.csv', callback=callback, generator=True)

write_jsonl('output.jsonl', data)
```

## 🎁 Feature Requests
Would you like to see other features implemented? Please, open a [feature request](https://github.com/AmenRa/unified-io/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=%5BFeature+Request%5D+title).


## 🤘 Want to contribute?
Would you like to contribute? Please, drop me an [e-mail](mailto:elias.bssn@gmail.com?subject=[GitHub]%20unified-io).


## 📄 License
[unified-io](https://github.com/AmenRa/unified-io) is an open-sourced software licensed under the [MIT license](LICENSE).