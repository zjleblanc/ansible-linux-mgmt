# debug.yml

This is a basic fact gathering playbook. One of the easiest ways to get starting using Ansible is by gathering facts and transforming them with filters. Using the ansible.builtin.debug module, users can see the outcome of transformations to get familiar with common ansible operations.

## suggested use case

When you are learning Ansible for the first time or setting up a new environment, simple playbooks like this provide you a short feedback loop. I often use this method to test connectivity to hosts in my inventory and as a bonus gather some useful facts about each host.