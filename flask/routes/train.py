from flask import Blueprint, Flask, jsonify, request, make_response, send_from_directory, abort
import os
import io
import cx_Oracle
import pymssql
import numpy as np
import pandas as pd
import json
import jwt
import time
import requests
import random
import string
import calendar
# from pandas.io.json import json_normalize
from pandas import json_normalize
from datetime import datetime, timedelta, timezone
from functools import wraps
from dotenv import load_dotenv

load_dotenv()

app = Blueprint('train',__name__)

oracle_client = r"C:\instantclient_19_5"
os.environ["ORACLE_HOME"] = oracle_client
os.environ["PATH"] = oracle_client+os.pathsep+os.environ["PATH"]
os.environ["NLS_LANG"] = "AMERICAN_AMERICA.TH8TISASCII"

APP_SECRET_KEY = os.getenv("APP_SECRET_KEY")

db_Synergy_host = os.getenv("db_Synergy_host")
db_Synergy_sid = os.getenv("db_Synergy_sid")
db_Synergy_uid = os.getenv("db_Synergy_uid")
db_Synergy_pwd = os.getenv("db_Synergy_pwd")
db_Synergy_port = os.getenv("db_Synergy_port")

def get_blueprint():
    """Return the blueprint for the main app module"""
    return app

def getDF(sql):
        oradsn = cx_Oracle.makedsn(host=db_Synergy_host, port=db_Synergy_port, sid=db_Synergy_sid)
        conn = cx_Oracle.connect(user=db_Synergy_uid, password=db_Synergy_pwd,
                                dsn=oradsn, encoding="UTF-8", nencoding="UTF-8")
        df = pd.read_sql_query(sql, conn)
        conn.close()
        return df

@app.route('/getYear', methods=['GET'])
def getYear():
    return {"Year" : 2023}

@app.route("/company", methods=['POST'])
def get_years():

        content = request.get_json(silent=True)
        datasource = content['datasource']
        
        sql = f""" select comcode, company
                from mas_company
  where datasource = {datasource} """
        print(sql)
        df = getDF(sql)
        print(df)
        data = json.loads(df.reset_index().to_json(orient='records'))
        return jsonify({'data' : data, 'row' : len(df)})



@app.route("/company_master", methods=['GET'])
def company_master():

        content = request.get_json(silent=True)
        # datasource = content['datasource']
        
        sql = f""" select distinct datasource
                from SYNERGY.mas_company"""
        print(sql)
        df = getDF(sql)
        print(df)

        data_list = df['DATASOURCE'].values.tolist() #CAPITAL LETTER
        return jsonify(data_list)

        # data = json.loads(df.reset_index().to_json(orient='records'))
        # return jsonify(data)


@app.route("/company_sub", methods=['POST'])
def company_sub():

        content = request.get_json(silent=True)
        datasource = content['datasource']
        print('look here', datasource)
        
        sql = f""" select comcode, company
                from mas_company
  where datasource = '{datasource}' """
        print(sql)
        df = getDF(sql)
        print(df)
        data = json.loads(df.reset_index().to_json(orient='records'))
        return jsonify({'data' : data, 'row' : len(df)})