from typing import Callable


def retry_on_exception(retries: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            r = retries

            while r > 0:
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    r -= 1
                    if r == 0:
                        print(f"final {e.__class__.__name__}")
                    else:
                        print(e.__class__.__name__)
                else:
                    print(f"ok")
                    return result
        return wrapper
    return decorator


error_counter_success = 0

@retry_on_exception(retries=3)
def test_success_after_one_fail():
    global error_counter_success
    if error_counter_success < 2:
        error_counter_success += 1
        raise ValueError
    return "Success after fail!"


@retry_on_exception(retries=3)
def test_fail_all_attempts():
    raise AttributeError


@retry_on_exception(retries=3)
def test_success_immediately():
    return "Success Immediately!"

result1 = test_success_after_one_fail()
result2 = test_fail_all_attempts()
result3 = test_success_immediately()