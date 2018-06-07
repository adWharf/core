#!/usr/bin/env python
# encoding: utf-8


"""
@author: william
@contact: 1342247033@qq.com
@site: http://www.xiaolewei.com
@file: cache.py
@time: 03/03/2018 23:30
"""
from .config import config
from sponge import CacheManager
from .container import register

cache_manager = CacheManager(config.get('app.cache'))
cache = cache_manager.store()
register('cache', cache)

