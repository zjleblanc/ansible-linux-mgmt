# Install SQL Server on RHEL Demo

Playbook to install SQL Server on RHEL

## Objectives

1. Install SQL Server
1. Configure firewall to allow remote connections

## Requirements

1. Machine needs to be registered
1. Enable the rhel-server-{{ major_version }}-optional-rpms repo

## Variables

```yaml
mssql_version: 2019
mssql_password: s3cr3t
mssql_edition: Evaluation
```