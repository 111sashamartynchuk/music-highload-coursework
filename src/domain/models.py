from dataclasses import dataclass
from uuid import UUID

@dataclass
class Artist:
    id: UUID
    name: str
    genre: str

@dataclass
class Track:
    id: UUID
    title: str
    lyrics: str
    release_year: int
    artist_id: UUID