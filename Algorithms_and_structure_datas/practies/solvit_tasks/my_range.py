# def _is_valid_step(step: int):
#     if step != 0:
#         return step
#     else: 
#         raise ValueError("value 'step' must be positive number")

# def my_range(*args):
#     if len(args) == 1:
#         start, stop, step = 0, args[0], 1
#     elif len(args) == 2:
#         start, stop, step = args[0], args[1], 1
#     elif len(args) == 3:
#         start, stop, step = args[0], args[1], _is_valid_step(args[2])
#     else:
#         raise ValueError("Invalid arguments")

#     if step > 0:
#         while start < stop:
#             yield start
#             start += step
#     else:
#         while start > stop:
#             yield start
#             start += step


### Можно ещё проще :)
def my_range(*args):
    for i in range(*args):
        yield i