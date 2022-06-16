from core import link
import psycopg
from simple_salesforce import Salesforce
import json
import pandas as pd

class dbtools:

    def __init__(self):
        self.recentdf = None

    def pg_query(SQL):
        try:
            pg = link.connect('postgresql')
            cur = pg.cursor()
            cur.execute(SQL)

            # Add each row (tuple) to a list
            tuplelist = []
            row = cur.fetchone()
            while row is not None:
                tuplelist.append(row)
                row = cur.fetchone()
                
            # Convert data to a DataFrame
            df = pd.DataFrame(list(tuplelist))

            cur.close()
            pg.close()
            return df

        except (Exception, psycopg.DatabaseError) as error:
            print(error)

    def pg_single_insert(insert_req):
        """ Single line INSERT request """
        try:
            pg = link.connect('postgresql')
            cur = pg.cursor()
            cur.execute(insert_req)
            pg.commit()
        except (Exception, psycopg.DatabaseError) as error:
            print(error)
            pg.rollback()
            cur.close()
            return 1
        cur.close()
        pg.close()
        


    def sf_query(SOQL):
        try:
            sf = link.connect('salesforce')
            obj = sf.query_all(SOQL)
            obj = obj['records']
            obj_json = json.dumps(obj, indent=4)
            df = pd.read_json(obj_json)
            return df

        except (Exception) as error:
            print(error)


    def df_to_csv(df, name):
    # Saves a dataframe to a CSV file
    # name should not include suffix '.csv'
        name = name + '.csv'
        df.to_csv(name)




