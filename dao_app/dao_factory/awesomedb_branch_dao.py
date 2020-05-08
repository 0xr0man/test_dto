from dao_app.awesomedb import AwesomeDB
from dao_app.transferObjects import BranchDTO
from datetime import datetime
import attr


@attr.s()
class AwesomeDBBranchDAO:
    awesome_db: AwesomeDB = attr.ib(default=None)

    def get_branch(self, bid):
        return self.awesome_db.get(query={'bid': bid})
        # return Transfer obj

    # Transfer object
    def insert_branch(self, branch: BranchDTO):
        # для простоты, не загонялся
        now = datetime.now()
        timestamp = int(datetime.timestamp(now))
        branch.bid = timestamp
        branch_dict = attr.asdict(branch)
        self.awesome_db.insert(branch_dict)
        return branch.bid

    def delete_branch(self, branch: BranchDTO):
        branch_dict = attr.asdict(branch)
        self.awesome_db.delete(branch_dict)
