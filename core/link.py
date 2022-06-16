from configparser import ConfigParser
import psycopg
from simple_salesforce import Salesforce, SalesforceLogin
import os



def config(section, filename='database.ini'):
    # Configuration file parser

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


def connect(section):
    # Connect to a database

    conn = None

    # read connection parameters
    params = config(section)

    """ Connect to the PostgreSQL database server """
    if section == "postgresql":
        try:
            print('Connecting to the PostgreSQL database...')
            conn = psycopg.connect(**params)

        except (Exception, psycopg.DatabaseError) as error:
            print(error)
        
    """ Connect with Salesforce """
    if section == "salesforce":
        print('Connecting to the Salesforce database...')
        conn = Salesforce(**params)
        #s_id, inst = SalesforceLogin(**params)
        #conn = Salesforce(instance=inst, session_id=s_id)

    return conn
