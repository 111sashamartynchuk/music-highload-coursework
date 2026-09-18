from src.application.handlers import MusicCatalogFacade


class TrackController:
    ### аналог MovieController
    # Приймає HTTP-запити та передає виклики у MusicCatalogFacade.
    def __init__(self, catalog_facade: MusicCatalogFacade):
        self.catalog_facade = catalog_facade

    def create_track(self, payload: dict):
        pass

    def get_track(self, track_id: str):
        pass

    def search_tracks(self, query: str):
        pass