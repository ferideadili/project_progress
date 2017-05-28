from bson.objectid import ObjectId


class UserMongoUtils(object):

    def __init__(self, mongo):
        self.mongo = mongo
        self.users_collection = 'user'

    def find_all_producers(self):
        result=self.mongo.db[self.users_collection].find()
        return result