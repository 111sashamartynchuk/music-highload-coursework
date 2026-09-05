import pandas as pd
import random

df = pd.read_csv('data/ваз_файл.csv')
df = df.dropna()

genres = ['Rock', 'Jazz-hop', 'Pop', 'Indie', 'Metal', 'Electronic', 'Hip-Hop']
album_suffixes = ['Greatest Hits', 'Live Session', 'The Early Years', 'Unplugged', 'Vol. 1']

print("Генеруємо бракуючі дані...")

df['release_year'] = [random.randint(1980, 2024) for _ in range(len(df))]

df['genre'] = [random.choice(genres) for _ in range(len(df))]

df['album'] = df['artist'] + " - " + [random.choice(album_suffixes) for _ in range(len(df))]

print(df[['artist', 'song', 'album', 'genre', 'release_year']].head())