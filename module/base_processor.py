#coding=utf-8
'''
Created on 2013-11-4

'''
import datetime

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

    def filter_db_res(self,db_res):
        '''
        判断是否是list，分解为dict，
        将dict中不能变为json的部分过滤或做处理
        '''        
        for key in db_res:
            #print type(db_res[key])
            if type(db_res[key]) == datetime.datetime:
                db_res[key] = db_res[key].strftime("%Y-%m-%d %H:%M:%S")  
           
        return db_res

def module(protocol):
    '''
    module装饰器, 用于装饰module中的主类
            作用是建立协议号和主类的映射
    '''
    def _module_dec(cls):
        Constants.MODULE_MAPPING[protocol] = cls
        return cls
    return _module_dec        
