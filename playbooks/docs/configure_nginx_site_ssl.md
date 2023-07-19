# python_script

This playbook takes a domain name and configures a site on an nginx reverse proxy with a valid acme certificate.

## suggested use case

If you have a reverse proxy with multiple sites **OR** want to automate acme certificate management.
<br>
<br>
If you are using a different web hosting service, the patterns in this playbook/role should still apply and can be modified to best suit your needs.

### prereqs

- You must own the domain name you pass to the role and have a DNS record pointing to your reverse proxy. If you do not have this configured, then the acme challenge will fail.

### vars

| name | purpose | example |
| --- | --- | --- |
| acme_domain_name | common name for the acme cert | example.autodotes.com |
| acme_email | e-mail address for acme notifications (e.g. expiration) | zach@autodotes.com |
| acme_private_ip | internal ip address for proxy to forward traffic (optional) | 192.168.0.X | 

### notes

- If you don't provide a private ip address, then a static site will be served on the proxy server with content from `acme_site_root`.
- By default, a cert will not be generated if a cert exists that doesn't expire within 30 days. You can increase/decrease this window via `acme_valid_days`.