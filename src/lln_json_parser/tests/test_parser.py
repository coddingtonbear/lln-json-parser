import os
from unittest import TestCase

from lln_json_parser.parser import get_entries


class TestParser(TestCase):
    def test_basic(self):
        with open(os.path.join(os.path.dirname(__file__), "example.json"), "r") as inf:
            items = list(get_entries(inf))

            assert len(items) == 2
