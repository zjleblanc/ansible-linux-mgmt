# ansible-linux-mgmt

Ansible repository for content used to manage Linux servers

## Playbooks

| Name | Playbook | Documentation |
| --- | :---: | :---: |
| debug.yml | [📕](./playbooks/debug.yml) | [📝](./playbooks/docs/debug.md) |
| postgres.yml | [📕](./playbooks/postgres.yml) | [📝](./playbooks/docs/postgres.md) |
| python_script.yml | [📕](./playbooks/python_script.yml) | [📝](./playbooks/docs/python_script.md) |

## Roles

| Name | Tasks | Documentation |
| --- | :---: | :---: |
| proxmox_guest | [📋](./roles/proxmox_guest/tasks/main.yml) | [📝](./roles/proxmox_guest/README.md) |

## Demos

| Purpose | Playbook | Documentation |
| --- | :---: | :---: |
| Register RHEL machine using subscription-manager | [📋](./demos/rhsm.yml) | [📝](./demos/docs/rhsm.md) |
| Install SQL Server on RHEL | [📋](./demos/sqlserver-rhel.yml) | [📝](./demos/docs/sqlserver-rhel.md) |
| Build Containers from template<br>Simulate building out multiple Containers with configurable options | [📋](./demos/proxmox_container_build.yml) | |