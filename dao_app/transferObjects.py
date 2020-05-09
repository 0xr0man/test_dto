import attr


@attr.s()
class BranchDTO:
    bid: int = attr.ib(default=-1)
    name: str = attr.ib(default=None)


@attr.s()
class UserDTO:
    # def __init__(self, **kwargs):
    #     self.__dict__.update(kwargs)
    uid: int = attr.ib(default=-1)
    branches: list = attr.ib(default=[])
    rate: int = attr.ib(default=-1)
