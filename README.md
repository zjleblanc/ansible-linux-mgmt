# ansible-linux-mgmt

Ansible repository for content used to manage Linux servers

## Playbooks

| Name | Playbook | Documentation |
| --- | :---: | :---: |
| debug.yml | [📕](./playbooks/debug.yml) | [📝](./playbooks/docs/debug.md) |
| postgres.yml | [📕](./playbooks/postgres.yml) | [📝](./playbooks/docs/postgres.md) |
| python_script.yml | [📕](./playbooks/python_script.yml) | [📝](./playbooks/docs/python_script.md) |
| configure_nginx_site_ssl.yml | [📕](./playbooks/configure_nginx_site_ssl.yml) | [📝](./playbooks/docs/configure_nginx_site_ssl.md) |
| sql_query.yml | [📕](./playbooks/sql_query.yml) | [📝](./playbooks/docs/sql_query.md) |

## Roles

| Name | Tasks | Documentation |
| --- | :---: | :---: |
| proxmox_guest | [📋](./roles/proxmox_guest/tasks/main.yml) | [📝](./roles/proxmox_guest/README.md) |

## Demos

| Purpose | Playbook | Documentation |
| --- | :---: | :---: |
| Register RHEL machine using subscription-manager | [📋](./demos/rhsm.yml) | [📝](./demos/docs/rhsm.md) |
| Install SQL Server on RHEL | [📋](./demos/sqlserver-rhel.yml) | [📝](./demos/docs/sqlserver-rhel.md) |
| Join RHEL machine to Active Directory Domain | [📋](./demos/join_ad_domain.yml) | [📝](./demos/docs/join-ad-domain.md) |
| Update login (or other) setting with lineinfile | _None_ | [📝](./demos/docs/min-pass-change.md) |
| Build Containers from template<br>Simulate building out multiple Containers with configurable options | [📋](./demos/proxmox_container_build.yml) | |