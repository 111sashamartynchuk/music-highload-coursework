class PostgresAdapter:
    def save_relations(self, artist_data: dict, album_data: dict, track_data: dict):
        pass

class MongoAdapter:
    def save_track_card(self, card_document: dict):
        pass

    def get_track_card(self, track_id: str) -> dict:
        pass

class ElasticAdapter:
    def index_lyrics(self, track_id: str, title: str, artist: str, lyrics: str):
        pass

    def search_by_text(self, text: str) -> list[str]:
        pass

class RedisCacheAdapter:
    def get_cached_search(self, query_key: str) -> list[dict] | None:
        pass

    def set_cached_search(self, query_key: str, results: list[dict], ttl: int = 3600):
        pass