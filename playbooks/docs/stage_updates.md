# stage updates

This [playbook](../stage_updates.yml) shows how to stage updates for a RHEL host with limited connectivity

## plays

The playbook is broken up into two plays, which in reality would likely be two separate job templates. 

### download

The first play runs dnf to download updates for installed packages. There are options to specify security or bugfix updates for downloading. For environments with low connectivity, this task could take awhile and experience interruptions. I would recommend doing this asynchronously and implementing a process to check for completion which can trigger the next install job.

### install 

The second play will gather package facts, install the previously downloaded updates from cache, and report on the changes applied to the system. This play only requires the SSH connection for ansible to execute.

## using the ansible.utils collection

Most of the tasks in this playbook come from ansible.builtin, but the fact diff module lives in the [ansible.utils](https://docs.ansible.com/ansible/latest/collections/ansible/utils/index.html) collection. I recommend including this task for audit and reporting purposes - plus it's nice just to know what changes.