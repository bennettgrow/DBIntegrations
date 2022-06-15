# InnoIntegrations
 Tools created for Innovasia Inc. and DESIGNBOX to integrate their CRM and external databases.

## Supports
- PostgreSQL integration via psycopg
- Salesforce integration via simple_salesforce
- Includes a terminal based console to send queries and save them as .CSVs

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
