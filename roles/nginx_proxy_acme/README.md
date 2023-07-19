nginx_proxy_acme
=========

Minimum Ansible Version: 2.1

Galaxy Tags: \[ acme cert letsencrypt \]

Required Variables
------------------

| Name | Example | Description |
| -------- | ------- | ------------------- |
| acme_email | acme-sa@example.com | e-mail address to receive acme notifications |
| acme_domain_name | ansible.example.com | certificate common name |


Role Variables
--------------

| Variable | Type | Value or Expression | Description |
| -------- | ------- | ------------------- | --------- |
| acme_letsencrypt_dir | default | /etc/letsencrypt |  |
| acme_letsencrypt_keys_dir | default | {{ acme_letsencrypt_dir }}/keys |  |
| acme_letsencrypt_csrs_dir | default | {{ acme_letsencrypt_dir }}/csrs |  |
| acme_letsencrypt_certs_dir | default | {{ acme_letsencrypt_dir }}/certs |  |
| acme_letsencrypt_account_key | default | {{ acme_letsencrypt_dir }}/account/account.key |  |
| acme_required_dirs | default | _above directories_ |  |
| acme_valid_days | default | 30 | if expiring in <= acme_valid_days, generate new cert |
| acme_site_root | default | /var/www/html/{{ acme_domain_name }} | directory for site root if proxy not used |
| acme_private_ip | 192.168.0.x | private ip address for reverse proxy to direct traffic |
| acme_challenge_type | var | http-01 |  |
| acme_directory | var | https://acme-v02.api.letsencrypt.org/directory |  |
| acme_version | var | 2 |  |

Handlers
--------------

  - Restart nginx
  - Reload nginx

Example Playbook
----------------

```yaml
  - hosts: servers
    tasks:
      - name: Execute nginx_proxy_acme role
        ansible.builtin.include_role:
          name: nginx_proxy_acme
        vars:
          acme_email: acme-sa@example.com
          acme_domain_name: ansible.example.com
          acme_private_ip: 192.168.0.x
```

License
-------

license (GPL-2.0-or-later, MIT, etc)

Author Information
-------
**Zach LeBlanc**

Red Hat
