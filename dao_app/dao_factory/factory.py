from dao_app.dao_factory.awesomedb.awesomedb_factory import AwesomeDBFACTORY
from dao_app.dao_factory.microservices.microservices_factory import MicroservicesFACTORY


class DAOFactory:
    DAO_LIST = ['awesomedb']
    DAO_OBJECTS = {
        'awesomedb': AwesomeDBFACTORY(),
        'microservices': MicroservicesFACTORY(),
    }

    def getDAOFactory(self, whichFactory: str):
        if whichFactory in self.DAO_OBJECTS:
            return self.DAO_OBJECTS[whichFactory]