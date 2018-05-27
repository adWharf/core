#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: william wei 
@license: Apache Licence  
@contact: weixiaole@baidu.com
@file: __init__.py.py 
@time: 15/01/2018 10:51 AM 
"""
import os
from .container import register, resolve
from .cache import cache
from .config import Config

PROJECT_PATH = os.environ['PROJECT_PATH'] if 'PROJECT_PATH' in os.environ \
    else os.path.split(os.path.realpath(__file__))[0] + '/../../'
APP_PATH = os.environ['APP_PATH'] if 'APP_PATH' in os.environ \
    else os.path.split(os.path.realpath(__file__))[0] + '/../'

config = Config()


__all__ = ['cache', 'config', 'logger', 'register', 'resolve']

# if os.path.exists(os.path.join(config.PROJECT_PATH, '.env')):
#     dotenv.read_dotenv(os.path.join(config.PROJECT_PATH, '.env'))
