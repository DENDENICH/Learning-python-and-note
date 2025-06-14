from typing import Any
from functools import singledispatch

@singledispatch
def fun(arg: Any, verbose: bool = False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)

@fun.register(int) # срабатывает, если передается int в аргумент arg
def _(arg: Any, verbose: bool = False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)

@fun.register(list) # срабатывает, если передается list в аргумент arg
def _(arg: Any, verbose: bool = False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)


fun([3, 4, 5, 6], verbose=True)