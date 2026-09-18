from typing import List, Optional
from uuid import UUID
from src.application.handlers import (
    ITrackMetadataRepository,
    ITrackLyricsRepository,
)
from src.domain.models import TrackMetadataDTO, TrackLyricsDTO


class TrackMetadataRepository(ITrackMetadataRepository):

    ## Адаптер для збереження структурованих метаданих у PostgreSQL / MongoDB.
    ### Реалізує CRUD-операції.

    def create(self, dto: TrackMetadataDTO) -> UUID:
        pass

    def get_by_id(self, track_id: UUID) -> Optional[TrackMetadataDTO]:
        pass

    def update(self, track_id: UUID, dto: TrackMetadataDTO) -> bool:
        pass

    def delete(self, track_id: UUID) -> bool:
        pass


class TrackLyricsRepository(ITrackLyricsRepository):

    ## Адаптер для роботи з текстами пісень у Elasticsearch
    ## pеалізує збереження, пошук та видалення індексу

    def index(self, dto: TrackLyricsDTO) -> None:
        pass

    def get_by_track_id(self, track_id: UUID) -> Optional[TrackLyricsDTO]:
        pass

    def search_by_text(self, text: str) -> List[UUID]:
        pass

    def delete(self, track_id: UUID) -> bool:
        pass