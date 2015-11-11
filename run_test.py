#coding=utf8
'''
Created on 2013-10-28

'''


import unittest
from test.server_test import ServerTest

if __name__ == '__main__':
    
    suite = unittest.TestSuite()
    
    suite.addTest(ServerTest("sample_test"))

    suite.addTest(ServerTest('account_register_mdn'))
    suite.addTest(ServerTest('account_register_email'))

    suite.addTest(ServerTest('account_login_mdn'))
    suite.addTest(ServerTest('account_login_email'))
    

    suite.addTest(ServerTest("article_get_by_id"))
    suite.addTest(ServerTest("article_search_by_keyword"))

    unittest.TextTestRunner(verbosity=2).run(suite)
    
