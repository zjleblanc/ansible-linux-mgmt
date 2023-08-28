# sql query

This playbook shows how to query a SQL Server instance and process the data

## make it your own

The query is simple, the json manipulation a bit more complex, but intended to output a list of objects with column_name -> value key-pairs. Once comfortable, manipulate the query used to return a targeted set of data or modify the `json_query` to process the results according to your specifications.

## using the reporting collection

The [zjleblanc.reporting](https://galaxy.ansible.com/zjleblanc/reporting) collection contains roles which output user-friendly html reports based on provided data. The [table](https://github.com/zjleblanc/zjleblanc.reporting/blob/master/zjleblanc/reporting/roles/table/README.md) role is developed for tabular datasets and works well with the output of the `mssql_script` module.