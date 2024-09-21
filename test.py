import unittest
import os
import json

from mpstore import load_store, read_store, write_store
from mpstore.store import STORE_PATH, TEMP_STORE_PATH


class TestStore(unittest.TestCase):
    def tearDown(self):
        self._assert_store_exists_and_temp_store_dne()

        try:
            os.remove(TEMP_STORE_PATH)
        except:
            pass
        try:
            os.remove(STORE_PATH)
        except:
            pass

    def test_empty_load_store(self):
        store = load_store()

        assert len(store) == 0
        assert store == {}  # empty dicts will both equate to False

    def test_load_store_with_values(self):
        write_store("foo", "bar")
        write_store("foo2", "bar2")

        load = load_store()

        assert load.get("foo") == "bar"
        assert load.get("foo2") == "bar2"

    def test_write_and_read(self):
        write_store("foo", "bar")

        assert read_store("foo") == "bar"

    def test_empty_store_read(self):
        assert read_store("foo") is None

    def test_store_read_not_exists(self):
        write_store("foo", "bar")

        assert read_store("DNE") is None

    def test_store_read(self):
        write_store("foo", "bar")

        assert read_store("foo") == "bar"

    def test_nested_write_and_read(self):
        write_store("item1.nested1", 2)
        write_store("item1.nested2", "value2")

        assert read_store("item1.nested1") == 2
        assert read_store("item1.nested2") == "value2"

    def test_nested_read_nonexistent_key(self):
        write_store("item1.nested1", 2)

        assert read_store("item1.nested3") is None

    def test_deeply_nested_write_and_read(self):
        write_store("level1.level2.level3", "deep_value")

        assert read_store("level1.level2.level3") == "deep_value"

    def _assert_store_exists_and_temp_store_dne(self):
        assert os.stat(STORE_PATH)  # will raise error if does not exist
        with self.assertRaises(OSError):
            os.stat(TEMP_STORE_PATH)  # should not exist b/c renamed to STORE_PATH


unittest.main()
