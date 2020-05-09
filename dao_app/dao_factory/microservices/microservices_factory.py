import attr
from dao_app.dao_factory.users_microservice_dao import UsersMicroservice

# наследоваться от DBFACtory


@attr.s()
class MicroservicesFACTORY:
    mc_name: str = attr.ib(default=None)
    mc_url: str = attr.ib(default=None)
    mc_urls = {
        'users': "users_url",
    }

    # def create_connection(self, table: str):
    #     self.db_instance = AwesomeDB(table=table).connect(
    #         url=self.db_url,
    #         table='branches'
    #     )
    def get_url(self):
        self.mc_url = self.mc_urls[self.mc_name]

    def get_users_mc_dao(self):
        self.get_url()
        return UsersMicroservice(url=self.mc_url)

