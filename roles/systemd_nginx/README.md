systemd_nginx
=========

Automation Solution Architect

Minimum Ansible Version: 2.1

Galaxy Tags: \[ systemd nginx eda remediation \]

Required Variables
------------------

| Name | Example | Description |
| -------- | ------- | ------------------- |
| systemd_nginx_eda_webhook | 10.0.1.15 | url for an active eda webhook source |


Role Variables
--------------

| Variable | Type | Value or Expression | Description |
| -------- | ------- | ------------------- | --------- |
| systemd_nginx_path_unit_name | default | demosite | name of the systemd path unit |
| systemd_nginx_service_name | default | deploydemosite | name of the systemd service unit |
| systemd_nginx_path_modified | default | /usr/share/nginx/demo | path to monitor |

Example Playbook
----------------

  ```yaml
    - hosts: servers
      tasks:
        - name: Execute systemd_nginx role
          ansible.builtin.include_role:
            name: systemd_nginx
          vars:
            systemd_nginx_eda_webhook: "10.0.1.15:5001/endpoint"
  ```

License
-------

GPL-2.0-or-later

Author Information
-------
**Zachary LeBlanc**

Red Hat
