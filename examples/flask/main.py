import json

from flask import request, Flask
from uadetector.flask import UADetector

app = Flask(__name__)

# app.config['UADETECTOR_USERAGENT_CLASS'] = 'xxxx.MyUserAgent'
# app.config['UADETECTOR_REQUEST_PROPERTY_NAME'] = 'agent'

UADetector(app)


@app.route('/')
def index():
    return '<pre>{}</pre>'.format(json.dumps({
        'device_type': request.ua.device_type,
        'os': request.ua.os,
        'browser': request.ua.browser,
        'from_pc': request.ua.from_pc,
        'from_smartphone': request.ua.from_pc,
    }, indent=2))
