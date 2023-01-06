from flask import Blueprint, Flask, jsonify, request, make_response, send_from_directory, abort, send_file
import os
from io import BytesIO
import pymssql
import cx_Oracle
import numpy as np
import pandas as pd
import json
import datetime
import math
from datetime import datetime, timedelta, timezone
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.utils.dataframe import dataframe_to_rows
from dotenv import load_dotenv

load_dotenv()

app = Blueprint('kal',__name__)

def get_blueprint():
    """Return the blueprint for the main app module"""
    return app

db_Synergy_host = os.getenv("db_Synergy_host")
db_Synergy_sid = os.getenv("db_Synergy_sid")
db_Synergy_uid = os.getenv("db_Synergy_uid")
db_Synergy_pwd = os.getenv("db_Synergy_pwd")
db_Synergy_port = os.getenv("db_Synergy_port")

def getDF(sql):
        oradsn = cx_Oracle.makedsn(host=db_Synergy_host, port=db_Synergy_port, sid=db_Synergy_sid)
        conn = cx_Oracle.connect(user=db_Synergy_uid, password=db_Synergy_pwd,
                                dsn=oradsn, encoding="UTF-8", nencoding="UTF-8")
        df = pd.read_sql_query(sql, conn)
        conn.close()
        return df

def crud(sql):
        oradsn = cx_Oracle.makedsn(host=db_Synergy_host, port=db_Synergy_port, sid=db_Synergy_sid)
        conn = cx_Oracle.connect(user=db_Synergy_uid, password=db_Synergy_pwd,
                                dsn=oradsn, encoding="UTF-8", nencoding="UTF-8")
        cursor = conn.cursor()
        affect = 0
        try:
                cursor.execute(sql)
                conn.commit()
                affect = cursor.rowcount
        except:
                affect = 0
        conn.close()
        return affect

def crudArray(sql, arrayPara):
        oradsn = cx_Oracle.makedsn(host=db_Synergy_host, port=db_Synergy_port, sid=db_Synergy_sid)
        conn = cx_Oracle.connect(user=db_Synergy_uid, password=db_Synergy_pwd,
                                dsn=oradsn, encoding="UTF-8", nencoding="UTF-8")
        cursor = conn.cursor()
        affect = 0
        try:
                cursor.execute(sql, arrayPara)
                conn.commit()
                affect = cursor.rowcount
        except:
                affect = 0
        conn.close()
        return affect


# get all subinv
# @app.route("/getallsubinv", methods=['GET'])
# def company_master():

#         content = request.get_json(silent=True)
        
#         sql = f""" SELECT RM_PRS_NO ,RM_NAME ,SUBINV_CODE ,AM_PRS_NO ,AM_NAME ,
#                 BRANCH_NAME ,MON ,TUE ,WEN ,THU ,FRI ,SAT ,SUN ,HOLIDAY ,SUBINV_STATUS ,
#                 REASON  FROM SYNERGY.CHECKIN_SHOP_OPEN WHERE SUBINV_CODE = {selectedSUBINV} """
#         print(sql)
#         df = getDF(sql)
#         print(df)

#         data_list = df['RM_PRS_NO'].values.tolist() #CAPITAL LETTER
#         return jsonify(data_list)

@app.route("/getsubinv", methods=['POST'])
def company_sub():

        content = request.get_json(silent=True)
        selectedSUBINV = content['selectedSUBINV']
        print('look here', selectedSUBINV)

        if selectedSUBINV == 0:
                sql = f""" SELECT RM_PRS_NO ,RM_NAME ,SUBINV_CODE ,AM_PRS_NO ,AM_NAME ,
                BRANCH_NAME ,MON ,TUE ,WEN ,THU ,FRI ,SAT ,SUN ,HOLIDAY ,SUBINV_STATUS ,
                REASON  FROM SYNERGY.CHECKIN_SHOP_OPEN """
        else:
                sql = f""" SELECT RM_PRS_NO ,RM_NAME ,SUBINV_CODE ,AM_PRS_NO ,AM_NAME ,
                BRANCH_NAME ,MON ,TUE ,WEN ,THU ,FRI ,SAT ,SUN ,HOLIDAY ,SUBINV_STATUS ,
                REASON  FROM SYNERGY.CHECKIN_SHOP_OPEN WHERE SUBINV_CODE = {selectedSUBINV} """
        print(sql)
        df = getDF(sql)
        print(df)
        data = json.loads(df.reset_index().to_json(orient='records'))
        return jsonify({'data' : data, 'row' : len(df)})