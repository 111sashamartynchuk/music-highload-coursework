from dataclasses import dataclass
from uuid import UUID

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