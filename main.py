import asyncio
import aiohttp
import pandas as pd
from tqdm.asyncio import tqdm_asyncio

# Genre mapping
genre_mapping = {
    28: "Action", 12: "Adventure", 16: "Animation", 35: "Comedy",
    80: "Crime", 99: "Documentary", 18: "Drama", 10751: "Family",
    14: "Fantasy", 36: "History", 27: "Horror", 10402: "Music",
    9648: "Mystery", 10749: "Romance", 878: "Science Fiction",
    10770: "TV Movie", 53: "Thriller", 10752: "War", 37: "Western"
}

API_KEY = '8265bd1679663a7ea12ac168da84d2e8'
BASE_URL = 'https://api.themoviedb.org/3/movie/top_rated'

# Exclude these columns
exclude_columns = {'backdrop_path', 'id', 'poster_path', 'title', 'video'}

# Fetch one page
async def fetch_page(session, page):
    url = f"{BASE_URL}?api_key={API_KEY}&language=en-US&page={page}"
    async with session.get(url) as response:
        data = await response.json()
        results = []
        for movie in data.get('results', []):
            # Replace genre_ids with genre names
            genre_names = [genre_mapping.get(gid, "Unknown") for gid in movie.get("genre_ids", [])]
            movie['genre_names'] = genre_names

            # Remove unwanted columns
            for col in exclude_columns:
                movie.pop(col, None)

            results.append(movie)
        return results

# Fetch all pages concurrently
async def fetch_all_pages():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page(session, page) for page in range(1, 472)]
        results = await tqdm_asyncio.gather(*tasks)
        return [movie for page in results for movie in page]

# Main entry point
def main():
    all_movies = asyncio.run(fetch_all_pages())
    df = pd.DataFrame(all_movies)
    df.to_csv("tmdb_filtered_movies.csv", index=False)
    print("Data saved to tmdb_filtered_movies.csv")

if __name__ == "__main__":
    main()
