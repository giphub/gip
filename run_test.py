#coding=utf8
'''
Created on 2013-10-28

'''
import torndb

from test.server_test import ServerTest
if __name__ == '__main__':
    import unittest
    #from test.server_test import ServerTest

    suite = unittest.TestSuite()
    

    suite.addTest(ServerTest("sample_test"))
    suite.addTest(ServerTest("article_get_by_id_test"))

    unittest.TextTestRunner(verbosity=2).run(suite)
    
