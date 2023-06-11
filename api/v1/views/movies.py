#!?usr/bin/env python3
"""Different views for star wars api"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
import redis
import requests
import uuid


api_key = '01d62744c62c7c8890fb5d5a3c788c53'
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)


@app_views.route('/', strict_slashes=False)
def index():
    """Load necessary landing data"""
    response = requests.get('https://api.themoviedb.org/3/search/movie?&api_key={}&query=star%20wars'.format(api_key))
    movies = response.json()['results']
    films = []
    genres = [12, 28, 878]
    for movie in movies:
        if genres == sorted(movie['genre_ids']):
            films.append(movie)
    return jsonify(films=films[1])


@app_views.route('/movies/', strict_slashes=False)
def movie_list():
    """Chache results in redis and return the list"""
    redis_client = redis.Redis(connection_pool=pool)
    if redis_client.exists('films'):
        films = redis_client.get('films').decode('utf-8')
        return jsonify(films=eval(films))
    response = requests.get('https://api.themoviedb.org/3/search/movie?&api_key={}&query=star%20wars'.format(api_key))
    empire_r = requests.get('https://api.themoviedb.org/3/search/movie?&api_key={}&query=empire%20strikes%20back'.format(api_key))
    jedi_r = requests.get('https://api.themoviedb.org/3/search/movie?&api_key={}&query=return%20of%20the %20jedi'.format(api_key))
    empire = empire_r.json()['results'][0]
    jedi = jedi_r.json()['results'][0]
    movies = response.json()['results']
    movies.append(empire)
    movies.append(jedi)
    films = []
    genres = [12, 28, 878]
    image_path="https://image.tmdb.org/t/p/w1280"
    for movie in movies:
        if genres == sorted(movie['genre_ids']):
            films.append(movie)
    redis_client.set('films', str(films))
    return jsonify(films=films)
