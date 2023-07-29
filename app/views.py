import json
from django.shortcuts import render

def movie_details(request):
    # fetching json file from movies folder
    with open('movies/index.json') as file:
        json_data = json.load(file)

    # Flatten the JSON data to a list of movies
    all_movies = []
    for date_data in json_data:
        all_movies.extend(date_data.get('movies', []))

    # Extract all unique genres from movies data
    all_genres = set()
    for movie in all_movies:
        all_genres.update(movie.get('genre', []))

    # Pass this context to our web page template
    context = {
        'movies': all_movies,
        'all_genres': all_genres,
    }
    print(context)
    return render(request, 'movie_template.html', context)
