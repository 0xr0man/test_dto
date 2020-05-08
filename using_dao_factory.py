# Abstract factory pattern
# from dao_factory.factory import DAOFactory
from dao_app.dao_factory.factory import DAOFactory
from dao_app.transferObjects import BranchDTO

dao_factory = DAOFactory()
awesome_db_dao_factory = dao_factory.getDAOFactory(whichFactory="awesomedb")
branchDAO = awesome_db_dao_factory.get_branch_dao()

new_branch = BranchDTO(name="firstBranch")
new_branch_bid = branchDAO.insert_branch(branch=new_branch)
print("NEW BRANCH BID", new_branch_bid)

branch = branchDAO.get_branch(new_branch_bid)
print("GETTED BRANCH", branch)