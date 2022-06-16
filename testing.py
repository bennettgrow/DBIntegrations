from core.dbtools import dbtools as db
from core import link

# Initialize salesforce and postgresql objects
# These usually are passed into link query functions



#db.pg_query("SELECT username, first_name, last_name FROM db_users WHERE active = true ")

# Request contact info from SF
sf_contacts = db.sf_query("SELECT Name, AccountId, Email, Phone, MobilePhone, Title FROM Contact ")
# Drop "attributes" column
sf_contacts = sf_contacts.drop(['attributes'], axis=1)
# Print first 10 rows
print(sf_contacts.head(10))

for i in sf_contacts.index:

#    pg_contacts = (
#        """INSERT INTO contact_dev (name, accountid, email, phone, mobilephone, title)
#        VALUES (%s,%s,%s,%s,%s,%s)""" 
#        % (sf_contacts['Name'], sf_contacts['AccountId'], sf_contacts['Email'], sf_contacts['Phone'], sf_contacts['MobilePhone'], sf_contacts['Title'])
#        % "ON CONFLICT contact_dev DO UPDATE SET"
#        )

    pg_contacts = """INSERT INTO contact_dev (name, accountid) VALUES ("%s","%s")""" % (sf_contacts['Name'], sf_contacts['AccountId']) + "ON CONFLICT DO UPDATE;"
    
    ret = db.pg_single_insert(pg_contacts)
    if ret == 1: # Break loop on error
        break

