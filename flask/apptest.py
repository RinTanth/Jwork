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
from routes import train

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={
    r'/*': {'origins': '*'},
    r'/restapi/fnc/*': {'origins': ['https//jm-report.jaymart.org']},
})

app.register_blueprint(train.get_blueprint(),  url_prefix="/api")

@app.route('/api/test/api', methods=['GET'])
def home():
    return "Hello, This is the Flask App in IIS Server."


@app.route('/api/invoice', methods=['POST'])
def reportDocReceive():
        content = request.get_json(silent=True)
        org_id = content['org_id']
        po_number = content['po_number']
        invoice_number = content['invoice_number']
        print(org_id, po_number, invoice_number)
        return {'po_number': po_number, "org_id" : org_id, "invoice_number" : invoice_number}

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', use_reloader=True, port=9082)