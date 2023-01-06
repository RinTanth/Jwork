"""
Deploy Flask App in IIS Server
"""
from flask import Flask, jsonify, request, make_response, send_from_directory, abort
from flask import send_file
from flask_cors import CORS, cross_origin
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address
from datetime import datetime, timedelta
import argparse
import os
import io
import jwt
import base64
import xlsxwriter
from pprint import pprint
from xlsxwriter import Workbook
import json
from dotenv import load_dotenv
from werkzeug.wrappers import response

from flask_swagger_ui import get_swaggerui_blueprint
load_dotenv()

APP_SECRET_KEY = os.getenv("APP_SECRET_KEY")

from routes import jern
from routes import junior
from routes import kal




app = Flask(__name__)
app.config.from_object(__name__)


# limiter = Limiter(app, key_func=get_remote_address)

api_jmreport_only = {
    "origins": ["https://jm-report.jaymart.org"]
}

api_v1_cors_config = {
  "origins": ["https://jm-report.jaymart.org","http://localhost:8090","http://localhost:8888"]
}

# CORS(app, resources={
        
#         "/api/*": api_v1_cors_config,
#         "/master/*": api_v1_cors_config,
#         "/api/synergy/*": api_v1_cors_config,
#         "/restapi/fnc/hr/*": api_v1_cors_config,
#         "/restapi/fnc/token": api_jmreport_only
                
#     })

#     r'/test/*': api_vi_cors_config
CORS(app, resources={
    r'/*': {'origins': '*'},
    r'/restapi/fnc/*': {'origins': ['https://jm-report.jaymart.org']},
})

# CORS(app)
# cors = CORS(app, resources={r"/test/*": {"origins": "*"}})

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###


# ถ้า endpoint duplicate จะชี้ไปที่บรรทัดที่เจอก่อน
app.register_blueprint(jern.get_blueprint(), url_prefix="/api")
app.register_blueprint(junior.get_blueprint(), url_prefix="/api")
app.register_blueprint(kal.get_blueprint(), url_prefix="/api")



# if __name__ == "__main__":
#     app.run()
# @limiter.limit('1000 per day')


@app.route('/api/test', methods=['GET'])
def home():
    return "Hello, This is the Flask App in IIS Server."


# @app.route('/token/chktimeout', methods=['POST'])
# def token_chktimeout():
#     auth_header = request.headers.get('Authorization')
#     if auth_header:
#         auth_token = auth_header.split(" ")[1]
#     else:
#         auth_token = ''
    
#     if not auth_token:
#         return jsonify({'message' : 'Token Missing' , 'signin' : True}), 200
#     try:
#         data = jwt.decode(auth_token, APP_SECRET_KEY, algorithms=["HS256"])
#         return jsonify({'message' : 'Token Success' , 'signin' : False}), 200
#     except:
#         return jsonify({'message' : 'Token Expire' , 'signin' : True}), 200



# @app.route('/curdate', methods=['POST', 'GET'])
# @cross_origin(**api_v1_cors_config)
# def curdate():
#     now = datetime.now()
#     date_time = now.strftime("%d/%m/%Y")
#     res = {"dte": date_time}
#     response = make_response(res, 200)
#     return response


if __name__ == '__main__':
    app.debug = False
# app.run(host='0.0.0.0', port=9080)
# app.run(host='0.0.0.0', port=9001)
    app.run(host='0.0.0.0', use_reloader=True, port=9999)