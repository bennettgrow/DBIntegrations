# DBIntegrations
 Tools created for a corportation to integrate their CRM and external databases.
 
 In current state, running *console.py* provides an interactive terminal-based system to query a PostgreSQL database or Salesforce.

## Features
- PostgreSQL integration via psycopg
- Salesforce integration via simple_salesforce
- Includes a terminal based console to send queries preview the results, and save them as .CSVs

## Requirements
- Python 3.5+
- simple_salesforce
- pyscopg
- pandas
- *database.ini* file in root dir. that must be formatted similarly to:
```
[salesforce]
username=user@email.com
password=pa55w0rd
security_token=abc123def456

[postgresql]
host=localhost
dbname=postgresql
user=myname
password=pa55w0rd
```
To generate a Salesforce security token, log in to Salesforce then click your avatar at the top right of the screen. Select *Settings*, then navigate to *Reset Security Token* on the left side. 
