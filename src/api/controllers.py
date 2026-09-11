class SearchController:
    """Вхідний адаптер (Driving Adapter) для HTTP запитів користувачів"""
    def __init__(self, query_handler):
        self.query_handler = query_handler

    def search(self, q: str, year: int = None):
        pass

class IngestController:
    """Вхідний адаптер для прийому батчів від генератора даних"""
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def ingest_batch(self, batch_data: list[dict]):
        pass