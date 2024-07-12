import json
import os

STORE_PATH = ".store.json"
TEMP_STORE_PATH = ".temp-store.json"


def load_store() -> any:
    """Returns all store keys and values."""
    _create_store_if_not_exists()
    with open(STORE_PATH) as f:
        json_content = json.load(f)
        return json_content


def read_store(key: str) -> any:
    """Returns the value at key in json store."""
    _create_store_if_not_exists()
    with open(STORE_PATH) as f:
        json_content = json.load(f)
        return json_content.get(key)  # if key does not exist, returns None


def write_store(key: str, value: any):
    """Writes the key, value pair in json store, overwriting any previous value."""
    _create_store_if_not_exists()
    with open(STORE_PATH, "rb") as f:
        json_content = json.load(f)
        json_content[key] = value
    with open(TEMP_STORE_PATH, "wb") as temp_f:
        json.dump(json_content, temp_f)  # write to temp file
    os.rename(TEMP_STORE_PATH, STORE_PATH)  # atomic operation


def _create_store_if_not_exists():
    try:
        with open(STORE_PATH):
            pass
    except OSError as oserror:
        if oserror.errno != 2:
            raise oserror

        with open(TEMP_STORE_PATH, "wb") as temp_f:
            json.dump({}, temp_f)
        os.rename(TEMP_STORE_PATH, STORE_PATH)
