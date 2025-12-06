from django.shortcuts import render
import requests
import random
from django.core.cache import cache
from django.conf import settings

RAWG_API_KEY = settings.RAWG_API_KEY

# View for Home Page
def home(request):
    featured_games = cache.get('featured_games')
    if not featured_games:
        try:
            # fetch the top games from RAWG
            url = f"https://api.rawg.io/api/games?key={RAWG_API_KEY}&page_size=20"
            response = requests.get(url)
            response.raise_for_status() # raise an exception if the API fails

            data = response.json().get('results', [])
            if not data:
                raise ValueError("No games returned from RAWG API")

            # shuffle and pick up to 8 games
            random.shuffle(data)
            sample_size = min(8, len(data))
            sample_data = data[:sample_size]

            # simplify each game object
            featured_games = [
                {
                    'rawg_id': g.get('id'),
                    'title': g.get('name'),
                    'cover_image': g.get('background_image') or 'https://via.placeholder.com/320x180?text=No+Image',
                }
                for g in sample_data
            ]

        except Exception as e:
            print("RAWG API error", e)
            featured_games = [] # fallback if API fails

        # cache games after fetching and processing for 15 mins
        cache.set('featured_games', featured_games, 60 * 15)

    return render(request, 'home.html', {'games': featured_games})
