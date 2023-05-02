#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Crieated on Tue May   2 23:49:33 2023
@authors: Nathaniel Emenike
          Ayomide Akanji
"""
from flask import jsonify, Blueprint
from models import storage
from api.v1.views import app_views
from models.state import State


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """ check the status of route """
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def object_status():
    """Create an endpoint that retrieves the number of each objects by type
    """
    objects = {"amenities": 'Amenity', "cities": 'City', "places": 'Place',
               "reviews": 'Review', "states": 'State', "users": 'User'}
    for key, value in objects.items():
        objects[key] = storage.count(value)
    return jsonify(objects)