#coding=utf-8 
''' 
Created on 2013-10-27 
 

'''
 
import time
import unittest
import httplib

from tornado.escape import json_encode

from constants.constants import Constants
from constants.errorcode import Errorcode
from constants.protocol import Protocol

class ServerTest(unittest.TestCase):
    '''
    单元测试，提供所有的测试方法
    
    '''
    def setUp(self):
        '''
        单元测试初始化，设定ip地址端口等信息
        '''
        self.server_host = '127.0.0.1'
        self.server_port = 8341
        self.server_url = '%s:%d'% (self.server_host, self.server_port)         

        pass
    
    def tearDown(self):
        '''
        单元测试完成后的清理操作
        '''
        
        pass
      
          
    def sample_test(self):
        '''
        示例代码
        '''
        body = {"protocol":Protocol.SAMPLE_MODULE_SAMPLE}
        headers = {} 
        self.__http_request(body, headers)


    def account_register_mdn(self):
        '''
        用户用手机注册
        '''
        body = {"protocol":Protocol.ACCOUNT_REG,
                "params":{"account":"13711112222",
                          "type":"mdn",
                          "password":"test"
                         }
               } 
        headers = {} 
        self.__http_request(body, headers)

    def account_register_email(self):
        '''
        用户用手机注册
        '''
        body = {"protocol":Protocol.ACCOUNT_REG,
                "params":{"account":"abc@abc.com",
                          "type":"email",
                          "password":"test"
                         }
               } 
        headers = {} 
        self.__http_request(body, headers)

    def account_login_mdn(self):
        '''
        用户用手机注册
        '''
        body = {"protocol":Protocol.ACCOUNT_LOGIN,
                "params":{"account":"13711112222",
                          "type":"mdn",
                          "password":"test"
                         }
               } 
        headers = {} 
        self.__http_request(body, headers)

    def account_login_email(self):
        '''
        用户用手机注册
        '''
        body = {"protocol":Protocol.ACCOUNT_LOGIN,
                "params":{"account":"abc@abc.com",
                          "type":"email",
                          "password":"test"
                         }
               } 
        headers = {} 
        self.__http_request(body, headers)


    def article_get_by_id(self):
        '''
        示例代码
        '''
        body = {"protocol":Protocol.ARTICLE_GET_BY_ID,"params":{"id":'6a81b294-2677-4b9f-aa1f-10b21099c08b'}}
        headers = {} 
        self.__http_request(body, headers)
                
    def article_search_by_keyword(self):
        '''
        示例代码
        '''
        body = {"protocol":Protocol.ARTICLE_SEARCH_BY_KEYWORD,"params":{"keyword":"幼儿园 感冒","start":0,"limit":10}}
        headers = {} 
        self.__http_request(body, headers)
   
    

 
    def __http_request(self,body,headers):
        
        try:
            httpClient = httplib.HTTPConnection(self.server_url)
            httpClient.request("POST", "/s", json_encode(body), headers)
            
            response = httpClient.getresponse()
            
            print response.status
            print response.reason
            

            print response.read().decode("unicode_escape") 
            print time.time()
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()         


        
if __name__ == "__main__":
    unittest.main()
    pass
