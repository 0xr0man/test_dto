import attr


@attr.s()
class BranchDTO:
    bid: int = attr.ib(default=-1)
    name: str = attr.ib(default=None)
