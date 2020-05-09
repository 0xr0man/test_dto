import attr
from dao_app.dao_factory.microservices.users_microservice_dao import UsersMicroservice


@attr.s()
class MicroservicesFACTORY:
    mc_url: str = attr.ib(default=None)
    mc_urls = {
        'users': "http://users_url",
    }

    def get_url(self, mc_name):
        self.mc_url = self.mc_urls[mc_name]

    def get_users_mc_dao(self):
        self.get_url(mc_name="users")
        return UsersMicroservice(url=self.mc_url)

