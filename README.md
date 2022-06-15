# InnoIntegrations
 Tools created for Innovasia Inc. and DESIGNBOX to integrate their CRM and external databases.

## Supports
- PostgreSQL integration using psycopg
- Salesforce integration using their REST API

 ## Setup
Connections to the supported databases require login information in *database.ini* that must be formatted similarly to:
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
