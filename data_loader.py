import csv
import random
import uuid
from pathlib import Path

# Списки для генерації атрибутів
GENRES = [
    "Rock", "Pop", "Hip-Hop", "Jazz-Hop",
    "Indie", "Electronic", "Metal", "R&B"
]

ALBUM_SUFFIXES = [
    "Greatest Hits", "Live Sessions", "Remastered",
    "Chronicles", "Volume 1", "Anthology", "Echoes"
]


class MockDataGenerator:
    def __init__(self, csv_filepath: str):
        self.csv_filepath = Path(csv_filepath)
        # Кеші для збереження зв'язків однаковий виконавець - однаковий ID
        self.artist_cache = {}  # artist_name -> {"id": UUID, "genre": str}
        self.album_cache = {}   # (artist_name, album_title) -> UUID

    def _get_or_create_artist(self, artist_name: str) -> dict:
        if artist_name not in self.artist_cache:
            self.artist_cache[artist_name] = {
                "id": uuid.uuid4(),
                "name": artist_name,
                "genre": random.choice(GENRES)
            }
        return self.artist_cache[artist_name]

    def _get_or_create_album(self, artist_name: str, artist_id: uuid.UUID) -> dict:
        suffix = random.choice(ALBUM_SUFFIXES)
        album_title = f"{artist_name} - {suffix}"

        cache_key = (artist_name, album_title)
        if cache_key not in self.album_cache:
            self.album_cache[cache_key] = {
                "id": uuid.uuid4(),
                "artist_id": artist_id,
                "title": album_title,
                "release_year": random.randint(1975, 2024)
            }
        return self.album_cache[cache_key]

    def process_and_preview(self, limit: int = 3):
        if not self.csv_filepath.exists():
            print(f"Помилка: Файл {self.csv_filepath} не знайдено.")
            print("Переконайтеся, що файл розміщено у папці 'data/' з назвою 'spotify_millsongdata.csv'.")
            return

        print(f"--- Тестування генерації на базі {self.csv_filepath.name} ---")

        with open(self.csv_filepath, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for idx, row in enumerate(reader):
                if idx >= limit:
                    break

                artist_name = row.get("artist", "Unknown Artist").strip()
                song_title = row.get("song", "Untitled").strip()
                lyrics_snippet = row.get("text", "")[:60].replace("\n", " ") + "..."
                source_link = row.get("link", "")

                artist = self._get_or_create_artist(artist_name)
                album = self._get_or_create_album(artist_name, artist["id"])

                track = {
                    "id": uuid.uuid4(),
                    "album_id": album["id"],
                    "title": song_title,
                    "lyrics_preview": lyrics_snippet,
                    "duration_sec": random.randint(120, 360),
                    "source_link": source_link
                }

                print(f"\n[Запис #{idx + 1}]")
                print(f"  • Виконавець: {artist['name']} (ID: {artist['id']}, Жанр: {artist['genre']})")
                print(f"  • Альбом:     {album['title']} (Рік: {album['release_year']})")
                print(f"  • Трек:       {track['title']} (Тривалість: {track['duration_sec']} с)")
                print(f"  • Текст:      \"{track['lyrics_preview']}\"")


if __name__ == "__main__":
    csv_path = "data/spotify_millsongdata.csv"
    generator = MockDataGenerator(csv_filepath=csv_path)
    generator.process_and_preview(limit=3)