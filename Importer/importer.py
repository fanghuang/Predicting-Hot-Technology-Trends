import couchdb
import schemas

from enum import Enum
class DB_Schema(Enum):
	corey = 1
	fang = 2

class Importer:

	def __init__(self):
		self.db_schemas = {
			"stackoverflow_daily": DB_Schema.corey,
			"stackoverflow_monthly": DB_Schema.fang,
			"stackoverflow_monthly_2000": DB_Schema.fang
		}
		

	def getDataFromDB(self, dbName):
		server = couchdb.Server()

		if dbName not in self.db_schemas:
			return {}

		schema = self.db_schemas[dbName]
		db = server[dbName]

		if schema == DB_Schema.corey:
			return schemas.importerCoreySchema(db)
		elif schema == DB_Schema.fang:
			return schemas.importerFangSchema(db)

