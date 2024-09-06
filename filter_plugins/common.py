#!/usr/bin/python
import random

RANDOM_SIZES = [0, .5, 1, 2, 4, 8, 64, 128, 512]

class FilterModule(object):
    def filters(self):
        return {
            'parse_usernames': self.do_parse_usernames,
            'random_sample': self.do_random_sample
        }

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

    def do_parse_usernames(self, usernames):
        user_objects = map(self.__create_user_obj, usernames)
        return {"campers": list(user_objects)}

    def do_random_sample(self, choices, size=1):
        random.seed(a=None, version=2)
        return random.sample(choices, size)