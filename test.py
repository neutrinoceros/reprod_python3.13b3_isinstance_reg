import inspect
import functools

isinstance(1, functools.partial)

def foo(): pass
isinstance(foo, functools.partial)

inspect.signature(foo)