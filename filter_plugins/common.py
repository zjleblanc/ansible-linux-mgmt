#!/usr/bin/python
import random

RANDOM_SIZES = [0, .5, 1, 2, 4, 8, 64, 128, 512]

class FilterModule(object):
    def filters(self):
        return {
            'parse_usernames': self.do_parse_usernames,
            'random_sample': self.do_random_sample,
            'last_reportify': self.do_last_reportify
        }

    ## filters ##

    def do_parse_usernames(self, usernames):
        user_objects = map(self.__create_user_obj, usernames)
        return {"campers": list(user_objects)}

    def do_random_sample(self, choices, size=1):
        random.seed(a=None, version=2)
        return random.sample(choices, size)

    def do_last_reportify(self, last, homedirs):
        post_sort = sorted(last, key = lambda x: (x['user'], x['login_epoch']), reverse=True)
        post_filter = filter(lambda rec: rec['user'] != 'zach' and rec['user'] != 'reboot', post_sort)

        def __map_last_record(record):
            import datetime
            return {
                "user": record['user'],
                "hostname": record['hostname'],
                "login": datetime.datetime.fromtimestamp(record['login_epoch']).strftime('%Y-%m-%d %H:%M:%S'),
                "logout": "" if 'logout_epoch' not in record else datetime.datetime.fromtimestamp(record['logout_epoch']).strftime('%Y-%m-%d %H:%M:%S'),
                "duration": "" if 'duration' not in record else record['duration'],
                "tty": record['tty'],
                "homedir_size": homedirs[record['user']].split('\t')[0]
            }
        post_map = map(__map_last_record, post_filter)
        return list(post_map)

    ## helper functions ##

    def __create_user_obj(self, username):
        first_name, last_name = username.split(" ")
        username = first_name[0].lower() + last_name.lower()
        random.seed(a=None, version=2)
        return {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": username + "@autodotes.com",
            "home": "/home/" + username,
            "size_mb": random.choice(RANDOM_SIZES)
        }