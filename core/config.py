#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: william wei 
@license: Apache Licence  
@contact: weixiaole@baidu.com
@file: config.py 
@time: 15/01/2018 11:27 AM 
"""

import toml
import os
from . import container

PROJECT_PATH = os.environ['PROJECT_PATH'] if 'PROJECT_PATH' in os.environ \
    else os.path.split(os.path.realpath(__file__))[0] + '/../../'
APP_PATH = os.environ['APP_PATH'] if 'APP_PATH' in os.environ \
    else os.path.split(os.path.realpath(__file__))[0] + '/../'


class Config(object):
    def __init__(self):
        self._config = {}
        for p, d, file_lists in os.walk(os.path.join(PROJECT_PATH, 'config')):
            for f in file_lists:
                try:
                    if 'example' in f:
                        continue
                    self._config[f.split('.toml')[0]] = toml.load(os.path.join(p, f))
                except Exception as e:
                    continue

    def get(self, key_str, def_val=None):
        cur = self._config
        try:
            for key in key_str.split('.'):
                cur = cur[key]
            return cur
        except Exception as e:
            container.resolve('logger').notice("config key [%s] not found" % key_str)
            return def_val

    def set(self, key_str, val):
        cur = self._config
        try:
            keys = key_str.split('.')
            for key in keys[:-1]:
                if key not in cur:
                    cur[key] = {}
                cur = cur[key]
            cur[keys[-1]] = val
        except Exception as e:
            container.resolve('logger').error(e)

    def __getattr__(self, item):
        return self.get(item)

    def __setattr__(self, key, value):
        self.set(key, value)


config = Config()


