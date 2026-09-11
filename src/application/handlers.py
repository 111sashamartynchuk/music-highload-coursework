from uuid import UUID

class IngestTrackCommand:
    """DTO для передачі вхідних даних від завантажувача/генератора"""
    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

class SearchTracksQuery:
    """DTO для пошукового запиту"""
    def __init__(self, query_text: str, year_filter: int = None):
        self.query_text = query_text
        self.year_filter = year_filter

class TrackCommandHandler:
    """Application Service: обробляє запис у різні сховища (Hexagonal Output Ports)"""
    def __init__(self, pg_repo, mongo_repo, elastic_repo):
        self.pg_repo = pg_repo
        self.mongo_repo = mongo_repo
        self.elastic_repo = elastic_repo

    def handle_ingest(self, command: IngestTrackCommand) -> UUID:
        pass

class TrackQueryHandler:
    """Application Service: обробляє пошук із кешуванням"""
    def __init__(self, cache_service, elastic_repo, mongo_repo):
        self.cache_service = cache_service
        self.elastic_repo = elastic_repo
        self.mongo_repo = mongo_repo

    def handle_search(self, query: SearchTracksQuery) -> list[dict]:
        pass