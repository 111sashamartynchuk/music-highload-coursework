import uuid
from src.domain.models import Artist, Album, Track
from src.infrastructure.repositories import (
    PostgresAdapter,
    MongoAdapter,
    ElasticAdapter,
    RedisCacheAdapter,
)
from src.application.handlers import (
    TrackCommandHandler,
    TrackQueryHandler,
    IngestTrackCommand,
    SearchTracksQuery,
)
from src.api.controllers import SearchController, IngestController


def test_system_wiring():
    print("тестування архітектури")

    sample_artist = Artist(
        id=uuid.uuid4(),
        name="Queen",
        genre="Rock"
    )
    sample_album = Album(
        id=uuid.uuid4(),
        artist_id=sample_artist.id,
        title="A Night at the Opera",
        release_year=1975
    )
    sample_track = Track(
        id=uuid.uuid4(),
        album_id=sample_album.id,
        title="Bohemian Rhapsody",
        lyrics="Is this the real life? Is this just fantasy?",
        duration_sec=354,
        source_link="https://open.spotify.com/track/sample"
    )
    print(f"1. Domain сутності створено  {sample_track.title} ({sample_artist.name})")

    pg_adapter = PostgresAdapter()
    mongo_adapter = MongoAdapter()
    elastic_adapter = ElasticAdapter()
    redis_adapter = RedisCacheAdapter()
    print("2. Адаптери інфраструктури ")

    command_handler = TrackCommandHandler(
        pg_repo=pg_adapter,
        mongo_repo=mongo_adapter,
        elastic_repo=elastic_adapter
    )
    query_handler = TrackQueryHandler(
        cache_service=redis_adapter,
        elastic_repo=elastic_adapter,
        mongo_repo=mongo_adapter
    )
    print("3. Application-обробники CQRS ")

    ingest_api = IngestController(command_handler=command_handler)
    search_api = SearchController(query_handler=query_handler)
    print("4. Контролери API ")

    ingest_api.ingest_batch([{"raw": "data"}])
    search_api.search(q="Bohemian", year=1975)

    print("коректно")


if __name__ == "__main__":
    test_system_wiring()