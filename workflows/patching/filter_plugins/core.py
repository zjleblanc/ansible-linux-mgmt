class FilterModule(object):

    def filters(self):
        return {
            "group_by_path": self.do_path_determination
        }

    def do_path_determination(self, dispatch_host_metadata):
        groups = {
          "rhel8_10": {},
          "rhel9_5": {}
        }

        for host in dispatch_host_metadata:
          version = host['version']
          name = host['inventory_hostname']
          if version == '8.10':
            groups["rhel8_10"].setdefault('patch_targets', []).append(name)
            groups["rhel8_10"].setdefault('patch_targets_metadata', {})[name] = host
          elif version == '9.5':
            groups["rhel9_5"].setdefault('patch_targets', []).append(name)
            groups["rhel9_5"].setdefault('patch_targets_metadata', {})[name] = host

        return groups
