# -*- coding: utf-8 -*-

import redis


class Redis:
    def __init__(self):
        self.redis = redis.StrictRedis()

    def exists(self, key):
        if self.redis.exists(key):
            return True
        return False

    def delete(self, key):
        if self.redis.delete(key):
            # delete return integer
            return True
        return False

    def set(self, key, value):
        if self.redis.set(key, value):
            return True
        return False

    def get(self, key):
        return self.redis.get(key)
