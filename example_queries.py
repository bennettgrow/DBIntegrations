from .tests.context import core
from core.link import link

# Initialize salesforce and postgresql objects
# These usually are passed into link query functions
conn = link()
sf = conn.sf
pg = conn.pg

# Example SQL query:
print("Acivated PostgreSQL users:")
link.pg_query(pg, "SELECT username, first_name, last_name FROM db_users WHERE active = true ")

# Example SOQL query:
print("\n\nSalesforce products starting with 'SLA':")
link.sf_query(sf, "SELECT Id, Name FROM Product2 WHERE Name LIKE 'SLA%' ")

# Good practice to close any open database connections
link.close