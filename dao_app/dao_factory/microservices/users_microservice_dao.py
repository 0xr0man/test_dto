import attr
from dao_app.transferObjects import UserDTO


@attr.s(slots=False)
class UsersMicroservice:
    url: str = attr.ib(default=None)

    def get_user(self, user: UserDTO):
        # send get rest query to mc
        # pseudocode: send_query(url=self.url, data=user_json)
        resp_dict = {
            'uid': user.uid,
            'branches': [1, 2, 4],
        }
        return UserDTO(**resp_dict)

    def update_user(self, data: UserDTO):
        user_old_data: UserDTO = self.get_user(data)
        # data_dict = attr.asdict(data)
        # # send update rest query to mc
        resp = user_old_data
        resp.branches += data.branches
        resp_dict = attr.asdict(resp)
        return UserDTO(**resp_dict)

