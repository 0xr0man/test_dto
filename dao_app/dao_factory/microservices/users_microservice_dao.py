import attr
from dao_app.transferObjects import UserDTO


@attr.s(slots=False)
class UsersMicroservice:
    url: str = attr.ib(default=None)

    def get_user(self, user: UserDTO):
        # send get rest query to mc
        resp = {
            'uid': 3,
            'branches': [1, 2, 4],
            'rate': 999,
        }
        return UserDTO(**resp)

    # def update_user(self, data: UserDTO):
    #     data_dict = attr.asdict(data)
    #     # send update rest query to mc
    #     pass

