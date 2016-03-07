from flask import Flask
from flask import jsonify
from flask.json import dumps
from flask import flash
from flask import url_for 
from flask import request
from flask import render_template
from flask import redirect
from flask import session

from urlparse import urlparse
import logging

application = Flask(__name__)
application.debug = True

from pyicloud import PyiCloudService


@application.route("/ryan", methods=['POST'])
def ryansphone():
    try:
      api = PyiCloudService('ryan@ryguy.com')
      api.devices[1].play_sound()
      return "Success!"
    except Error as e:
      abort(500, "Error({0}): {1}".format(e.errno, e.strerror))

@application.route("/marisa", methods=['POST'])
def marisasphone():
    try:
      api = PyiCloudService('marisakaitlyn@gmail.com')
      api.devices[1].play_sound()
      return "Success!"
    except Error as e:
      abort(500, "Error({0}): {1}".format(e.errno, e.strerror))

@application.errorhandler(500)
def custom500(error):
    response = jsonify({'message': error.description})

if __name__ == "__main__":
    application.run(use_debugger=True, debug=True,
            use_reloader=True, host='0.0.0.0')
