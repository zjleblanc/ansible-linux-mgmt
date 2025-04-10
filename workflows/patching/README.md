# setup

- Create RHEL8 boxes<br>
  `ansible-playbook workflows/patching/setup/main.yml -e target_platform=rhel8`
- Create RHEL9 boxes<br>
  `ansible-playbook workflows/patching/setup/main.yml -e target_platform=rhel9`