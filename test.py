import inspect
from functools import partial

isinstance(1, partial)

def foo(): pass
isinstance(foo, partial)

inspect.signature(foo)