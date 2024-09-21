import json
import os

STORE_PATH = ".store.json"
TEMP_EXTENSION = '.tmp'


def load_store(path: str = STORE_PATH) -> any:
    """Returns all store keys and values."""
    _create_store_if_not_exists(path)
    with open(path) as f:
        json_content = json.load(f)
        return json_content


def read_store(key: str, path: str = STORE_PATH) -> any:
    """Returns the value at key in json store."""
    _create_store_if_not_exists(path)
    with open(path) as f:
        json_content = json.load(f)
        return _get_nested_json_value(json_content, key)  # if key does not exist, returns None


def write_store(key: str, value: any, path: str = STORE_PATH):
    """Writes the key, value pair in json store, overwriting any previous value."""
    _create_store_if_not_exists(path)
    with open(path, "rb") as f:
        json_content = json.load(f)
        _set_nested_json_value(json_content, key, value)
    with open(path + TEMP_EXTENSION, "wb") as temp_f:
        json.dump(json_content, temp_f)  # write to temp file
    os.rename(path + TEMP_EXTENSION, path)  # atomic operation


def _get_nested_json_value(data: dict, key: str) -> any:
    """Gets the value from a nested dict given a dot-separated key."""
    keys = key.split(".")
    for k in keys:
        data = data.get(k, None)
        if data is None:
            return None
    return data


def _set_nested_json_value(data: dict, key: str, value: any):
    """Sets a value in a nested dict given a dot-separated key."""
    keys = key.split(".")
    d = data
    for k in keys[:-1]:
        if k not in d:
            d[k] = {}
        d = d[k]
    d[keys[-1]] = value


class AbsolutePathOnlyException(Exception):
    ...


def _create_store_if_not_exists(path: str):
    parts = path.split('/')
    if len(parts) > 1 and not path.startswith('/'):
        raise AbsolutePathOnlyException('Nested paths must start with "/".')

    # make any needed directories
    current_path = ''
    for part in parts[:-1]:  # Exclude the file name
        if part:
            current_path += '/' + part
            try:
                os.mkdir(current_path)  # Create directory
            except OSError:
                pass  # Ignore if the directory already exists
    # make file if needed
    try:
        with open(path):
            pass
    except OSError as oserror:
        if oserror.errno != 2:
            raise oserror

        print('test')
        with open(path, "wb") as f:
            json.dump({}, f)
