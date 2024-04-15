#!/usr/bin/python3
""" Index view
"""
from api.v1.app import app_views
from flask import jsonify


@app_views.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})
