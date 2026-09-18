from src.api.controllers import TrackController
from src.application.handlers import (
    TrackMetadataService,
    TrackLyricsService,
    MusicCatalogFacade,
)
from src.domain.models import CreateTrackDTO
from src.infrastructure.repositories import (
    TrackMetadataRepository,
    TrackLyricsRepository,
)


def verify_architecture_flow():
    print("Перевірка ланцюжка архітектури")

    metadata_repo = TrackMetadataRepository()
    lyrics_repo = TrackLyricsRepository()
    print("1. Repositories створено: TrackMetadataRepository & TrackLyricsRepository")

    metadata_service = TrackMetadataService(metadata_repo=metadata_repo)
    lyrics_service = TrackLyricsService(lyrics_repo=lyrics_repo)
    print("2. Services підключено: TrackMetadataService & TrackLyricsService")

    catalog_facade = MusicCatalogFacade(
        metadata_service=metadata_service,
        lyrics_service=lyrics_service
    )
    print("3. Facade зібрано: MusicCatalogFacade")

    controller = TrackController(catalog_facade=catalog_facade)
    print("4. Controller готовий: TrackController")

    test_track_dto = CreateTrackDTO(
        title="Bohemian Rhapsody",
        artist_name="Queen",
        album_title="A Night at the Opera",
        lyrics="Is this the real life?",
        genre="Rock",
        release_year=1975,
        duration_sec=354,
        source_link="https://open.spotify.com/..."
    )
    controller.create_track(test_track_dto)
    controller.search_tracks(query="Bohemian")

    print("\nЛанцюжок успішно перевірено:")
    print("TrackController -> MusicCatalogFacade -> [TrackMetadataService + TrackLyricsService] -> [TrackMetadataRepository + TrackLyricsRepository]")


if __name__ == "__main__":
    verify_architecture_flow()