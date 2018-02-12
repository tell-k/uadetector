from flask import request, Flask
from uadetector.flask import UADetector


def make_app(ua_class=None, prop_name=None):

    app = Flask(__name__)

    if ua_class:
        app.config['UADETECTOR_USERAGENT_CLASS'] = ua_class
    if prop_name:
        app.config['UADETECTOR_REQUEST_PROPERTY_NAME'] = prop_name

    UADetector(app)
    # Skip re-assign useragent object to request object.
    UADetector(app)

    app.testing = True

    @app.route('/view')
    def view():
        return request.ua.os

    @app.route('/view2')
    def view2():
        return request.ua.__class__.__name__

    @app.route('/view3')
    def view3():
        return request.ua_obj.os

    return app
