#!/usr/bin/env python
# encoding: utf-8


"""
@author: william
@contact: 1342247033@qq.com
@site: http://www.xiaolewei.com
@file: ad_status.py
@time: 12/04/2018 17:10
"""
from enum import Enum

ADSTATUS_UNKNOW  = -1    # 未知
ADSTATUS_NORMAL  = 0     # 正常 
ADSTATUS_PENDING = 1     # 待审核 
ADSTATUS_DENIED  = 2     # 审核不通过 
ADSTATUS_FROZEN  = 3     # 冻结 
ADSTATUS_SUSPEND = 4     # 挂起 
ADSTATUS_PREPARE = 5     # 准备状态 
ADSTATUS_DELETED = 6     # 删除

AD_BID_TYPE = Enum('AD_BID_TYPE', ('CPM', 'OCPM'))
AD_BID_TYPE_OCPM_OPT_MORE_CLICK = 2
AD_BID_TYPE_OCPM_OPT_MORE_ORDER = 7
