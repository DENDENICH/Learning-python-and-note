

class ReversedSequence:
    def __init__(self, sequence):
        self._reversed_sequence = list(reversed(sequence))

    def __len__(self):
        return len(self._reversed_sequence)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return ReversedSequence(self._reversed_sequence[index])
        else:
            return self._reversed_sequence[index]

    def __setitem__(self, index, value):
        self._reversed_sequence[index] = value

    def __iter__(self):
        yield from self._reversed_sequence


r = ReversedSequence([1, 2, 3, 4, 5])
r.append(4)
