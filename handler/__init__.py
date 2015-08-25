#coding=utf-8


import os
import importlib

module_set = set()
module_path = "module"

# 自动加载module中的类
def load_modules(path):
    for py_file in os.listdir(path):
    
        if '__init__' in py_file or 'base_processor' in py_file or '.pyc' in py_file:
            continue
        if os.path.isdir(path + '/' + py_file):
            load_modules(path + '/' + py_file)
            
        if '.py' in py_file:
            module_set.add( (path + "/" + py_file).strip('.py') )

load_modules(module_path)

for module_name in module_set:
    importlib.import_module(module_name.replace('/' , '.'))
