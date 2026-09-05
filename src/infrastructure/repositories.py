class MongoRepository:
    def save_document(self, document: dict):
        pass

class ElasticRepository:
    def index_text(self, text: str):
        pass

class RedisCache:
    def get_cache(self, key: str):
        pass
    def set_cache(self, key: str, value: dict):
        pass