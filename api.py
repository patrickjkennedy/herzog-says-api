#!/usr/bin/python
from flask import Flask
from flask_restful import Resource, Api
from flask.ext.mysql import MySQL
from random import randint
import json

mysql = MySQL()

#Initialize Flask app
app = Flask(__name__)

#MySQL Config
app.config['MYSQL_DATABASE_USER'] = ''
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = ''
app.config['MYSQL_DATABASE_HOST'] = ''

mysql.init_app(app)

api = Api(app)

class Quote(Resource):
    def post(self):
        try:

        #Connect to database
            conn = mysql.connect()
            cursor = conn.cursor()

        #Count rows
            query = "SELECT COUNT(*) FROM quotes"
            cursor.execute(query)
            numRows = cursor.fetchall()

        #Pick random row
            i = randint(0,numRows[0][0]-1)

        #Query db for quote
            query = "SELECT * FROM quotes WHERE id=" + str(i)
            cursor.execute(query)
            response = cursor.fetchall()

            return {'data': response}

        except Exception as e:
            return {'error': str(e)}


api.add_resource(Quote,'/quote')


if __name__ == '__main__':
	app.run(debug=True)
