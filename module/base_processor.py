#coding=utf-8
'''
Created on 2013-11-4

'''
from service.db import DB

from constants.constants import Constants


class Processor():
    '''
     Base class for all account process modules
             初始化数据库，缓存，短信服务
    '''


    def __init__(self,handler):
        '''
        Constructor
        '''
        self.handler = handler
        self.db = DB(handler.application)
        pass

def module(protocol):
    '''
    module装饰器, 用于装饰module中的主类
            作用是建立协议号和主类的映射
    '''
    def _module_dec(cls):
        Constants.MODULE_MAPPING[protocol] = cls
        return cls
    return _module_dec        