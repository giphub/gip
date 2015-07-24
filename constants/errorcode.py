#coding:utf-8
'''
Created on 2013-10-28

'''


class Errorcode(object):
    '''
    错误代码表，通用的错误不加module下面的子目录名称，直接用下划线分割错误。
    对于特定模块的错误，需要加module下面子目录名称作为前缀。
    错误定义尽量少，不要在参数校验上花太多时间。
    
    每个错误码都不用定义对应的文字描述，文字描述只在本文件中添加注释即可
    '''
    
    ERROR_NONE = 0
    MISSING_PARAM  = 1
    MODULE_DO_NOT_EXIST = 2


