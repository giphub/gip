#coding=utf-8
'''
Created on 2015-04-14

'''

import logging
import os
import sys
import time
import traceback

from ConfigParser import ConfigParser
from tornado import httpserver, process
import tornado.ioloop
import tornado.web
import torndb


from handler.main_handler import MainHandler


class App(tornado.web.Application):
    '''
    继承tornado.web.Application
    
    '''
    
    def __init__(self,config):
        start=time.time()
        handlers = [
            (r"/", MainHandler),  
        ]
    
        settings = dict(gzip=True,
                    debug=False,)
        super(App, self).__init__(handlers, **settings)

        

        # 创建数据库链接
        self.mysql_conn_read,self.mysql_conn_write = self.build_db_connection(config)
        
        end = time.time()
        logging.info("......启动总耗时："+str((end-start)*1000)+"毫秒")
        print("......启动总耗时："+str((end-start)*1000)+"毫秒")
        
    def build_db_connection(self,config):
        
        mysql_host=config.get("mysql_read", "host")
        mysql_database=config.get("mysql_read", "database")
        mysql_user=config.get("mysql_read", "user")
        mysql_password=config.get("mysql_read", "password")

        mysql_conn_read = torndb.Connection(host=mysql_host, database=mysql_database,
             user=mysql_user, password=mysql_password,time_zone="+8:00")
        
        # 写
        mysql_host=config.get("mysql_write", "host")
        mysql_database=config.get("mysql_write", "database")
        mysql_user=config.get("mysql_write", "user")
        mysql_password=config.get("mysql_write", "password")

        mysql_conn_write = torndb.Connection(host=mysql_host, database=mysql_database,
             user=mysql_user, password=mysql_password,time_zone="+8:00")
        
        return mysql_conn_read,mysql_conn_write    
        

       
def main():
    
    '''
    读取配置，启动服务
    '''
    config = ConfigParser()
    config.read('config.cfg')
    log_path = config.get("default", "logpath")
    num_processes = int(config.get("default", "num_processes"))
    port = int(config.get("default", "port"))
    
    # 初始化日志服务
    initLog(log_path)
    
    # 服务最大线程不超过cpu核数
    cpu_count=process.cpu_count()
    if num_processes>cpu_count:
        print("This server is only "+str(cpu_count)+" cores, input value is too large.")
        num_processes = 0
    
    # 启动服务    
    app = App(config)
    http_server = httpserver.HTTPServer(app)
    http_server.bind(port)
    http_server.start(num_processes)
    tornado.ioloop.IOLoop.instance().start()


def initLog(log_path):
    '''
    初始化日志系统，定义日格式等
    '''
    try:
        if os.path.exists(log_path)==False:
            os.makedirs(log_path)
    except:
        etype, evalue, tracebackObj = sys.exc_info()[:3]
        print("Type: " , etype)
        print("Value: " , evalue)
        traceback.print_tb(tracebackObj)
        
    track_log = log_path+'/track.log'    
    
    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=track_log,
                filemode='w')
    
    #logging.debug('This is debug message')
    #logging.info('This is info message')
    #logging.warning('This is warning message')
    
 
if __name__ == "__main__":
    main()    

