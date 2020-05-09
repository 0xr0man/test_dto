# Abstract factory pattern
# from dao_factory.factory import DAOFactory
from dao_app.dao_factory.factory import DAOFactory
from dao_app.transferObjects import BranchDTO, UserDTO

dao_factory = DAOFactory()
awesome_db_dao_factory = dao_factory.getDAOFactory(whichFactory="awesomedb")
branchDAO = awesome_db_dao_factory.get_branch_dao()

microservices_factory = dao_factory.getDAOFactory(whichFactory="microservices")
userDAO = microservices_factory.get_users_mc_dao()

# it is branch module realization with


class Branch:
    def create(self, branch: BranchDTO):
        new_branch_bid = branchDAO.insert_branch(branch=branch)
        # updating user
        updated_user = userDAO.update_user(data=UserDTO(
            uid=1,
            branches=[new_branch_bid])
        )
        return new_branch_bid

    def get(self, branch: BranchDTO):
        return branchDAO.get_branch(branch=branch)

    def delete(self, branch: BranchDTO):
        branchDAO.delete_branch(branch)


branch_obj = Branch()
# creating branch
created_branch_bid = branch_obj.create(branch=BranchDTO(
    name="first branch"
))
print("CREATED BRANCH BID", created_branch_bid)
# getting branch
getted_branch = branch_obj.get(branch=BranchDTO(bid=created_branch_bid))
print("GETTED BRANCH", getted_branch)
# deleting branch
print("DELETING BRANCH")
branch_obj.delete(branch=getted_branch)
# is deleted?
print(branch_obj.get(branch=BranchDTO(bid=created_branch_bid)))

