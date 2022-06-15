from configparser import ConfigParser
from importlib.resources import path
import psycopg
from simple_salesforce import Salesforce
import json
import os

class link:

    def __init__(self):
        self.pg = link.connect(self, "postgresql")
        self.sf = link.connect(self, "salesforce")


    def config(section, filename='database.ini'):

        # Find parent directory
        path = os.path.realpath(__file__)
        dir = os.path.dirname(path)
        dir = dir.replace('core','')

        # create a parser
        parser = ConfigParser()

        # Read ini file
        parser.read(dir + filename)

        # get section
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db


    def connect(self, section):
        conn = None

        # read connection parameters
        params = link.config(section)

        """ Connect to the PostgreSQL database server """
        if section == "postgresql":
            try:
                print('Connecting to the PostgreSQL database...')
                conn = psycopg.connect(**params)

            except (Exception, psycopg.DatabaseError) as error:
                print(error)
            
        """ Connect with the Salesforce REST API """
        if section == "salesforce":
            print('Connecting to the Salesforce database...')
            conn = Salesforce(**params)

        return conn

    def close(self):
        self.pg.close()
        print('Connections closed. \n')


    def pg_query(pg, SQL):
        try:
            cur = pg.cursor()
            cur.execute(SQL)
            row = cur.fetchone()
            while row is not None:
                print(row)
                row = cur.fetchone()
            cur.close()
        except (Exception, psycopg.DatabaseError) as error:
            print(error)


    def sf_query(sf, SOQL):
        try:
            obj = sf.query_all(SOQL)
            obj_json = json.dumps(obj, indent=4)
            print(obj_json)
        except (Exception) as error:
            print(error)
