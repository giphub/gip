#coding=utf-8
'''
Created on 2015-4-14

'''

class Protocol(object):
    '''
    定义所有的协议编号,协议的常量名称形如 ACCOUNT_REGISTER=101
    用短横线分割，短横线前是所述的功能分组和module下的目录相对应，如module/account
    短横线之后是具体的功能名称和module/account/register.py相对应
    
    SAMPLE_MODULE_SAMPLE 为示例
    ''' 
    SAMPLE_MODULE_SAMPLE = 0
  

    '''
    跟用户相关
    '''
    ACCOUNT_REG = 1
    ACCOUNT_LOGIN = 2
    
    '''
    跟数据库中的article表相关的内容
    '''

    ARTICLE_GET_BY_ID = 1001
    ARTICLE_SEARCH_BY_KEYWORD = 1002



