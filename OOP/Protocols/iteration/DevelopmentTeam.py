from dataclasses import dataclass, field
from itertools import chain


@dataclass
class DevelopmentTeam:
    junior_developers: list = field(default_factory=list)
    senior_developers: list = field(default_factory=list)

    def add_junior(self, *args):
        # self.junior_developers.extend(args)
        self.junior_developers.extend((name, "junior") for name in args)

    def add_senior(self, *args):
        self.senior_developers.extend((name, "senior") for name in args)

    def __iter__(self):
        yield from chain(self.junior_developers, self.senior_developers)

    def __len__(self):
        return len(self.junior_developers) + len(self.senior_developers)



dt = DevelopmentTeam()

dt.add_junior("John", "Jack")
dt.add_senior("Mike", "Mary")

for i in dt:
    print(i)