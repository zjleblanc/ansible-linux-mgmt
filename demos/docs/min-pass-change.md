# RHEL Minimum Password Lifetime Setting

Red Hat Enterprise Linux ships with a setting which enforces a number of days as the minimum password lifetime for new user accounts. If you need to configure this setting for frequent password rotations, the following ansible snippet will do the trick.

## Ansible Task

```yaml
- name: Allow multiple password changes in single day
  ansible.builtin.lineinfile:
    path: /etc/login.defs
    regexp: '^PASS_MIN_DAYS'
    line: PASS_MIN_DAYS 0
```