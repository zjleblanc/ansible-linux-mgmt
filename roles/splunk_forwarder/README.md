splunk_forwarder
=========

Adapted from [AustinCloudGuru/ansible-role-splunk-forwarder](https://github.com/AustinCloudGuru/ansible-role-splunk-forwarder)

Role Variables
--------------

| Variable | Type | Value or Expression | Description |
| -------- | ------- | ------------------- | --------- |
| splunk_forwarder_user | default | splunk |  |
| splunk_forwarder_group | default | splunk |  |
| splunk_forwarder_uid | default | 10011 |  |
| splunk_forwarder_gid | default | 10011 |  |
| splunk_release | default | 9.1.1 |  |
| splunk_url | default | https://download.splunk.com/products/universal ... |  |
| splunk_forwarder_rpm | default | splunkforwarder-9.1.1-64e843ea36b1.x86_64.rpm |  |
| splunk_rpm | default | {{ splunk_url }}/{{ splunk_forwarder_rpm }} |  |
| splunk_rpm_checksum | default | md5:48700b9eb544848e103fc4476e00e8ef |  |
| splunk_forwarder_indexer | default | splunk-indexer:9997 |  |
| splunk_forwarder_index | default | default |  |
| splunk_forwarder_sourcetype | default | nginx |  |
| splunk_forwarder_logs | default | [] |  |

Handlers
--------------

  - Enable Splunk Forwarder

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
  - hosts: servers
    tasks:
      - name: Execute splunk_forwarder role
        ansible.builtin.include_role:
          name: splunk_forwarder
        vars:
          splunk_forwarder_admin_user: zach
          splunk_forwarder_admin_pass: redhat
          splunk_forwarder_depl_server: splunk-mgt:8089
          splunk_forwarder_indexer: splunk-indexer:9997
          splunk_forwarder_index: default
          splunk_forwarder_sourcetype: nginx
          splunk_forwarder_logs:
            - /var/log/nginx/access.log
            - /var/log/nginx/error.log
```
