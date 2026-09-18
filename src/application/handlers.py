from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from src.domain.models import (
    CreateTrackDTO,
    TrackMetadataDTO,
    TrackLyricsDTO,
    TrackFullViewDTO,
)

# Output Ports (Інтерфейси CRUD-репозиторіїв)

class ITrackMetadataRepository(ABC):  # CRUD-порт для реляційних та карточних метаданих треку
    @abstractmethod
    def create(self, dto: TrackMetadataDTO) -> UUID:
        pass

    @abstractmethod
    def get_by_id(self, track_id: UUID) -> Optional[TrackMetadataDTO]:
        pass

    @abstractmethod
    def update(self, track_id: UUID, dto: TrackMetadataDTO) -> bool:
        pass

    @abstractmethod
    def delete(self, track_id: UUID) -> bool:
        pass


class ITrackLyricsRepository(ABC):  #CRUD-порт для повнотекстових індексів текстів пісень"""
    @abstractmethod
    def index(self, dto: TrackLyricsDTO) -> None:
        pass

    @abstractmethod
    def get_by_track_id(self, track_id: UUID) -> Optional[TrackLyricsDTO]:
        pass

    @abstractmethod
    def search_by_text(self, text: str) -> List[UUID]:
        pass

    @abstractmethod
    def delete(self, track_id: UUID) -> bool:
        pass

# Доменні сервіси (Business Services)

class TrackMetadataService:
    ## Сервіс, відповідальний суто за метадані (артисти, альбоми, дати)
    def __init__(self, metadata_repo: ITrackMetadataRepository):
        self.metadata_repo = metadata_repo

    def save_metadata(self, dto: TrackMetadataDTO) -> UUID:
        return self.metadata_repo.create(dto)

    def get_metadata(self, track_id: UUID) -> Optional[TrackMetadataDTO]:
        return self.metadata_repo.get_by_id(track_id)


class TrackLyricsService:
    ### за роботу з лірикою та текстовим пошуком
    def __init__(self, lyrics_repo: ITrackLyricsRepository):
        self.lyrics_repo = lyrics_repo

    def save_lyrics(self, dto: TrackLyricsDTO) -> None:
        self.lyrics_repo.index(dto)

    def get_lyrics(self, track_id: UUID) -> Optional[TrackLyricsDTO]:
        return self.lyrics_repo.get_by_track_id(track_id)

    def search_lyrics(self, text: str) -> List[UUID]:
        return self.lyrics_repo.search_by_text(text)

# Фасад (Facade) - координує роботу двох сервісів
class MusicCatalogFacade:

    # Фасад , кординує TrackMetadataService та TrackLyricsService.

    def __init__(self, metadata_service: TrackMetadataService, lyrics_service: TrackLyricsService):
        self.metadata_service = metadata_service
        self.lyrics_service = lyrics_service

    def register_new_track(self, create_dto: CreateTrackDTO) -> UUID:
        ## пр узгодженого збереження в обидва сервіси
        pass

    def get_full_track_details(self, track_id: UUID) -> Optional[TrackFullViewDTO]:
        # Отримує метадані з одного сервісу, а текст з іншого
        pass

    def search_tracks(self, query: str) -> List[TrackFullViewDTO]: #Шукає збіги за словами через LyricsService, а деталі бере з MetadataService
        pass