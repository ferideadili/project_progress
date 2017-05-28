from bson.objectid import ObjectId
from datetime import datetime

class MongoProjectsUtils(object):

    def __init__(self, mongo):
        self.mongo = mongo
        self.collection_name = "projects"

    def get(self, id):
        return self.mongo.db[self.collection_name].find_one({'_id': ObjectId(id)})

    def get_project(self, id):
        return self.get(id)['project']

    def all(self):
        results = self.mongo.db[self.collection_name].find().sort('timestamp', 1)
        return list(results)

    def all_projects(self):
        results = self.all()
        projects = []
        for doc in results:
            doc['project']['id'] = doc['_id']
            projects.append(doc['project'])

        return list(projects)

    def get_all_projects(self):
        result = self.mongo.db[self.collection_name].find()
        return result


    def upsert(self, project_id, project):
        if project_id is not None:
            return self.mongo.db[self.collection_name].update(
                {'_id': ObjectId(project_id)},
                {'$set': {"project": project}})
        else:
            # It's a new project, let's insert it!
            doc = {
                'timestamp': datetime.utcnow(),
                'project': project
            }
            return self.mongo.db[self.collection_name].insert(doc)

