#coding=utf-8
'''
Created on 2015-4-16

@author: liupeng
'''

class GipException(Exception):
    '''
    txboss异常基类
    '''


    def __init__(self, errorcode, errormsg=None, **kwargs):
        '''
        Constructor
        '''
        
        self.errorcode = errorcode
        self.errormsg = errormsg
        self.ext_params = kwargs
