from itertools import groupby

consecutive = [1, 1, 1, 0, 0, 1]

for num in groupby(consecutive):
    print(f"Group - {num}")
    print(f"\tMain key - {num[0]}")
    for i in num[1]:
        print(f"\t\tValue - {i}")