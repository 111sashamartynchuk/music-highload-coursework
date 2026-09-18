from dataclasses import dataclass
from uuid import UUID


# Доменні сутності (Entities)

@dataclass
class Artist:
    id: UUID
    name: str
    genre: str


@dataclass
class Album:
    id: UUID
    artist_id: UUID
    title: str
    release_year: int


@dataclass
class Track:
    id: UUID
    album_id: UUID
    title: str
    lyrics: str
    duration_sec: int
    source_link: str


# Об'єкти передачі даних (DTO)

@dataclass
class CreateTrackDTO:
    ### DTO для створення/імпорту нового треку з контролера
    title: str
    artist_name: str
    album_title: str
    lyrics: str
    genre: str
    release_year: int
    duration_sec: int
    source_link: str


@dataclass
class TrackMetadataDTO:
    ## DTO тільки метаінформації про трек
    id: UUID
    title: str
    artist_name: str
    album_title: str
    genre: str
    release_year: int
    duration_sec: int
    source_link: str


@dataclass
class TrackLyricsDTO:
    # DTO для збереження та пошуку слів
    track_id: UUID
    title: str
    artist_name: str
    lyrics: str


@dataclass
class TrackFullViewDTO:
    # Агрегований DTO для повернення клієнту через Фасад
    id: UUID
    title: str
    artist_name: str
    album_title: str
    lyrics: str
    genre: str
    release_year: int
    duration_sec: int
    source_link: str