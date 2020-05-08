from dao_app.dao_factory.awesomedb_factory import AwesomeDBFACTORY


class DAOFactory:
    DAO_LIST = ['awesomedb']
    import dao_app.dao_factory.awesomedb_factory
    DAO_OBJECTS = {
        'awesomedb': AwesomeDBFACTORY()
    }

    def getDAOFactory(self, whichFactory: str):
        if whichFactory in self.DAO_OBJECTS:
            return self.DAO_OBJECTS[whichFactory]