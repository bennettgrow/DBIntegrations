from core.dbtools import dbtools as db

# Initialize salesforce and postgresql objects
# These usually are passed into link query functions


# Example SQL query:
#db.pg_query("SELECT username, first_name, last_name FROM db_users WHERE active = true ")

# Example SOQL query:
# print("\nSalesforce products starting with 'SLA':")
db.sf_query("SELECT Id, Name FROM Product2 WHERE Name LIKE 'SLA%' ")


