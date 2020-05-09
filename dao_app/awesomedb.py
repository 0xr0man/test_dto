import attr


# it is simple "database"
@attr.s(slots=False)
class AwesomeDB:
    url: str = attr.ib(default=None)
    table: str = attr.ib(default=None)
    db_data: dict = attr.ib(default={})

    def count_documents(self):
        return len(self.table)

    def connect(self, url: str, table: str):
        db_data = {
            table: []
        }
        return AwesomeDB(url=url, table=table, db_data=db_data)

    def get(self, query: dict):
        for item in self.db_data[self.table]:
            for key in query:
                # не загонялся что может быть несколько условий в query,
                # только одно
                # не загонялся над поиском нужного элемента
                if item[key] == query[key]:
                    return item
        return None

    def insert(self, data: dict):
        self.db_data[self.table].append(data)

    def delete(self, data: dict):
        self.db_data[self.table].remove(data)
