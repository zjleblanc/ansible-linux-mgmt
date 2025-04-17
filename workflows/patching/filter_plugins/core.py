class FilterModule(object):

    def filters(self):
        return {
            "group_by_path": self.do_path_determination
        }

    def do_path_determination(self, dispatch_host_metadata):
        groups = {}

        for host_metadata in dispatch_host_metadata:
          version = host_metadata['version']
          group_key = 'rhel' + version.replace('.','_')
          host_name = host_metadata['inventory_hostname']

          groups.setdefault(group_key, {}).setdefault('patch_targets', []).append(host_name)
          groups[group_key].setdefault('patch_targets_metadata', {})[host_name] = host_metadata

        return groups
