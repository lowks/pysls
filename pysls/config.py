# -*- coding: utf-8 -*-

import configparser


class Config:
    def __init__(self, path):
        self.conf = configparser.ConfigParser()
        self.conf.read(path)

    def __getattr__(self, item):
        # item looks like 'sectionName_keyName'
        s = item.index('_')
        section = item[:s]
        key = item[s + 1:]
        return self.conf.get(section, key)