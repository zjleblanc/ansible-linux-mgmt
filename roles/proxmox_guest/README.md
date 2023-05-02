proxmox_guest
=========

Create a proxmox kvm guest based on provided configuration.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

  ```yaml
    - name: Build KVMs via defined configs
      when: proxmox_vm_configs is defined
      loop: "{{ proxmox_vm_configs }}"
      loop_control:
        loop_var: pve_config
      register: r_proxmox_kvm
      ansible.builtin.include_role: 
        name: proxmox_guest
  ```

Example Config
--------------

```yaml
proxmox_vm_configs:
  - cores: 2
    cpu: host
    description: KVM guest created from template
    ide:
      ide2: none,media=cdrom
    kvm: rhel-8.7-x86_64-kvm.qcow2
    memory: 8192
    name: rhel-guest-1
    net: 
      net0: virtio,bridge=vmbr0,firewall=1
    node: pve
    onboot: true
    ostype: l26
    virtio:
      virtio0: local:32,format=qcow2
    scsihw: virtio-scsi-single
    sockets: 2
    tags:
      - demo
      - rhel
      - linux
    timeout: 120
```