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

    def test_mk(self):
        def foo(): pass
        with mk.patch.object(functools, "partial", autospec=True):
            inspect.signature(foo)

            inspect.signature(self.test_mk)
            def bar(x: int) -> None: pass
            inspect.get_annotations(bar, eval_str=True)