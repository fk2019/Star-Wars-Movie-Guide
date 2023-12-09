#!/usr/bin/env python3
"""Different views for star wars api"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from os import getenv
import redis
import requests
import uuid


api_key = getenv('MOVIES_API_KEY')
host = getenv('REDIS_HOST')
db = getenv('REDIS_DB')
port = getenv('REDIS_PORT')
pool = redis.ConnectionPool(host=host, port=port, db=db)


@app_views.route('/', strict_slashes=False)
def index():
    """Load necessary landing data"""
    response = requests.get('https://api.themoviedb.org/3/search/movie?&api_key={}&query=star%20wars'.format(api_key))
    movies = response.json().get('results')
    films = []
    genres = [12, 28, 878]
    # obtain only films, not tvs etc
    if movies:
        for movie in movies:
            if genres == sorted(movie['genre_ids']):
                films.append(movie)
        return jsonify(films=films[1])
    return jsonify({'status': 'api error'})


@app_views.route('/movies/', strict_slashes=False)
def movie_list():
    """Cache results in redis and return the list"""
    redis_client = redis.Redis(connection_pool=pool)
    if redis_client.exists('films'):
        films = redis_client.get('films').decode('utf-8')
        return jsonify(films=eval(films))
    response = requests.get('https://api.themoviedb.org/3/search/movie?&api_key={}&query=star%20wars'.format(api_key))
    empire_r = requests.get('https://api.themoviedb.org/3/search/movie?&api_key={}&query=empire%20strikes%20back'.format(api_key))
    jedi_r = requests.get('https://api.themoviedb.org/3/search/movie?&api_key={}&query=return%20of%20the %20jedi'.format(api_key))
    empire = empire_r.json().get('results')[0]
    jedi = jedi_r.json().get('results')[0]
    movies = response.json().get('results')
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
