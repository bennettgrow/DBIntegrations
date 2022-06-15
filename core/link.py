from configparser import ConfigParser
import psycopg
from simple_salesforce import Salesforce
import json

class link:

    def __init__(self):
        self.pg = link.connect(self, "postgresql")
        self.sf = link.connect(self, "salesforce")


    def config(section, filename='database.ini'):
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        # get section, default to postgresql
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
