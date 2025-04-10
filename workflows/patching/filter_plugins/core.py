class FilterModule(object):

    def filters(self):
        return {
            "group_by_path": self.do_path_determination
        }

    def do_path_determination(self, hostvars):
        groups = {
          "rhel8_10": [],
          "rhel9_5": []
        }

        for host in hostvars:
          version = hostvars[host]['ansible_facts']['distribution_version']
          if version == '8.10':
            groups["rhel8_10"].append(host)
          elif version == '9.5':
            groups["rhel9_5"].append(host)

        return groups
