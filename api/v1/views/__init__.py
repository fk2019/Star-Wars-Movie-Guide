#!/usr/bin/python3
"""Initialize api blueprint
"""
from flask import Blueprint
#create a blueprint called app_views
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

#import all views
from api.v1.views.index import *
from api.v1.views.movies import *
