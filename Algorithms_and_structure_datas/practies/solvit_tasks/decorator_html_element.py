from typing import Callable

def add_tag(tag: str):
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            text = func(*args, **kwargs)
            return f"<{tag}>{text}</{tag}>"
        return wrapper
    return decorator


def add_div(func: Callable):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        return f"<div>{text}</div>"
    return wrapper


@add_tag("h2")
def greeting(name: str) -> str:
    return f"Hello, {name}!"

print(greeting("Grisha"))
