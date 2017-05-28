
class MongoSettingsUtils(object):

    def __init__(self, mongo):
        self.mongo = mongo
        self.collection_name = "settings"

    def get_settings(self):
        return self.mongo.db[self.collection_name].find_one()


    def add_supported_language(self, lang):
        '''
            Add a supported language
        '''

        # Get current settings document in order to update it.
        settings = self.mongo.db[self.collection_name].find_one()

        # if the document exists, then just update the langs property.
        if settings is not None:
            self.mongo.db[self.collection_name].update(
                {'_id': settings['_id']},
                {'$addToSet': {'langs': lang}}
            )

        # If the document doesn't exist, then we have to create it.
        else:
            settings = {}
            settings['langs'] = [lang]
            self.mongo.db[self.collection_name].insert(settings)

    def update_supported_languages(self, langs):
        # Get old settings document in order to update it.
        settings = self.mongo.db[self.collection_name].find_one()

        # if the document exists, then just update the langs property.
        if settings is not None:
            self.mongo.db[self.collection_name].update(
                {'_id': settings['_id']},
                {'$set': {'langs': langs}})

        # If the document doesn't exist, then we have to create it.
        else:
            settings = {}
            settings['langs'] = langs
            self.mongo.db[self.collection_name].insert(settings)

    def get_supported_languages(self):
        settings = self.mongo.db[self.collection_name].find_one()
        if settings is not None:
            return list(settings['langs'])
        else:
            return []
