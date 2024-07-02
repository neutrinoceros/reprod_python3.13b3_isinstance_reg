import inspect
import functools
from unittest import TestCase
import unittest.mock as mk


class TestIsinstance(TestCase):
    def test_int(self):
        isinstance(1, functools.partial)

    def test_func(self):
        def foo(): pass
        isinstance(foo, functools.partial)

    def test_signature(self):
        def foo(): pass
        inspect.signature(foo)
