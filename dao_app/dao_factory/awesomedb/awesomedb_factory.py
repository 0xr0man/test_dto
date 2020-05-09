import dao_app.dao_factory.factory as df
import dao_app.dao_factory.awesomedb.awesomedb_branch_dao as fd
from dao_app.awesomedb import AwesomeDB
# from dao_factory.factory import DAOFactory
# from dao_factory.awesomedb_branch_dao import AwesomeDBBranchDAO


class AwesomeDBFACTORY:
    db_url = "awesomedb_url"
    db_instance = None

    def create_connection(self, table: str):
        self.db_instance = AwesomeDB(table=table).connect(
            url=self.db_url,
            table='branches'
        )

    def get_branch_dao(self):
        self.create_connection(table="branches")
        return fd.AwesomeDBBranchDAO(awesome_db=self.db_instance)

