# postgres

This playbook sets up postgres on a RHEL node in your environment with some initial configuration.

## suggested use case

If you are looking to setup postgres with some basic configuration, such as:
- same network access
- postgres listen on all addresses (I always forget to do this!)
- service started with firewall enabled

Additionally, the script will run a few actions on the postgres instance:
- create a database
- create a table
- create a user with access to the database and table

### vars

| name | purpose | example |
| --- | --- | --- |
| postgres_conf | path to postgres conf file | /var/lib/pgsql/data/postgresql.conf |
| postgres_hba | path to postgres hba file | /var/lib/pgsql/data/pg_hba.conf |
| postgres_user | name of user to create | ee_wizard |
| postgres_pwd | password of user to create | sUp3rS3cRet |
| postgres_db | name of database to create | pypi |
| postgres_table | name of table in database to create | packages |