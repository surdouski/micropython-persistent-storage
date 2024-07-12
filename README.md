# mpstore

Micropython-persistent-storage (mpstore) is a lightweight persistent key-value store library for MicroPython. It provides a simple JSON-based storage API.

## Installation

You can install mpstore from the REPL with mip.
```python
# micropython REPL
import mip
mip.install("github:surdouski/micropython-persistent-storage")
```

Alternatively, you can install it by using mpremote if you don't have network connectivity on device.
```
$ mpremote mip install github:surdouski/micropython-persistent-storage
```


## Usage

### Loading the Store

To load the entire store:

```python
from mpstore.store import load_store

store = load_store()
print(store)
```

### Reading from the Store

To read a specific value from the store:

```python
from mpstore.store import read_store

value = read_store("your_key")
print(value)
```

### Writing to the Store

To write a key-value pair to the store:

```python
from mpstore.store import write_store

write_store("your_key", "your_value")
```

## API Reference

### `load_store() -> any`

Returns all keys and values from the store.

### `read_store(key: str) -> any`

Returns the value associated with the given key. Returns `None` if the key does not exist.

### `write_store(key: str, value: any)`

Writes the key-value pair to the store, overwriting any previous value.

## Testing

The project includes a test suite using the `unittest` framework. The tests are located in `test_store.py`.

### Running Tests

To run tests, do the following.
```
# install unittest, mounting the volume locally
$ docker run --rm -v $(pwd)/lib:/root/.micropython/lib micropython/unix micropython -m mip install unittest

# run the test, using the mounted volume for the unittest deps
$ docker run --rm -v $(pwd):/code -v $(pwd)/lib:/root/.micropython/lib micropython/unix micropython test_store.py
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
