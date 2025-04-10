class FilterModule(object):

    def filters(self):
        return {
            "group_by_path": self.do_path_determination
        }

    def do_path_determination(self, hostvars):
        groups = {"rhel8_10":[],"rhel9_5":[]}

        for host in hostvars:
          if hostvars[host]['ansible_distribution_version'] == '8.10':
            groups["rhel8_10"] = groups["rhel8_10"].append(host)
          elif hostvars[host]['ansible_distribution_version'] == '9.5':
            groups["rhel9_5"] = groups["rhel9_5"].append(host)

        return groups
