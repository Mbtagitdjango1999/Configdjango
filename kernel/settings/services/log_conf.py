import toml
#import logging
import os 
#from logging import config
import logging.config

dict12={'version': 1,

'disable_existing_loggers': False,
 

'handlers': {'coreHandler': {'level': 'INFO', 'class': 'logging.handlers.RotatingFileHandler', 'filename': 'logs/core/core.log', 'maxBytes': 104857600, 'backupCount': 5, 'formatter': 'coreFormatter'}, 'consoleHandler': {'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'consoleFormatter'}, 'authHandler': {'level': 'INFO', 'class': 'logging.handlers.RotatingFileHandler', 'filename': 'logs/auth/auth.log', 'maxBytes': 104857600, 'backupCount': 10, 'formatter': 'authFormatter'}},


'formatters': {'consoleFormatter': {'format': '%(levelname)s %(asctime)s %(module)s %(message)s', 'datefmt': '%Y-%m-%d %H-%M-%S'}, 'coreFormatter': {'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s', 'datefmt': '%Y-%m-%d %H-%M-%S'}, 'authFormatter': {'format': '%(levelname)s %(asctime)s %(module)s %(message)s', 'datefmt': '%Y-%m-%d %H-%M-%S'}}, 
 

'loggers': {'core': {'handlers': ['coreHandler', 'consoleHandler'], 'level': 'INFO', 'propagate': False}, 'auth': {'handlers': ['authHandler'], 'level': 'INFO', 'propagate': False}}}

from kernel.settings.base import BASE_DIR
#print(11111)

if not os.path.exists(os.path.join(BASE_DIR,'logs')):
    os.makedirs(os.path.join(BASE_DIR,'logs'))
    
if not os.path.exists(os.path.join(BASE_DIR,'logs','auth')):
    os.makedirs(os.path.join(BASE_DIR,'logs','auth'))
    
if not os.path.exists(os.path.join(BASE_DIR,'logs','core')):
    os.makedirs(os.path.join(BASE_DIR,'logs','core'))        
#print(44444444)

with open('logging.toml') as config_file:
    
    dict1 = toml.load(config_file)
   # print(55555555)
  #  print(log_config)
    # logging.config.dictConfig(log_config)
  #  print(6666666666)

if dict1 == dict12:
    print('1111111111111111111111111111111111111111111111111')
    logging.config.dictConfig(dict1)
    
    
if dict12 != dict1:
    print("weqweqweqweqwe")    
    print()
    print(dict1)
    dict123 =  {'version': 1, 'disable_existing_loggers': False, 'handlers': {'coreHandler': {'level': 'INFO', 'class': 'logging.handlers.RotatingFileHandler', 'filename': 'logs/core/core.log', 'maxBytes': 104857600, 'backupCount': 5, 'formatter': ['coreFormatter']}, 'consoleHandler': {'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': ['consoleFormatter']}, 'authHandler': {'level': 'INFO', 'class': 'logging.handlers.RotatingFileHandler', 'filename': 'logs/auth/auth.log', 'maxBytes': 104857600, 'backupCount': 10, 'formatter': ['authFormatter']}}, 'formatters': {'consoleFormatter': {'format': '%(levelname)s %(asctime)s %(module)s %(message)s', 'datefmt': '%Y-%m-%d %H-%M-%S'}, 'coreFormatter': {'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s', 'datefmt': '%Y-%m-%d %H-%M-%S'}, 'authFormatter': {'format': '%(levelname)s %(asctime)s %(module)s %(message)s', 'datefmt': '%Y-%m-%d %H-%M-%S'}}, 'loggers': {'core': {'handlers': ['coreHandler', 'consoleHandler'], 'level': 'INFO', 'propagate': False}, 'auth': {'handlers': ['authHandler'], 'level': 'INFO', 'propagate': False}}}  
    # logging.config.dictConfig(dict123)
    if dict123 != dict12:
        print('asdasdasdasd') 

# logging.config.dictConfig(dict1)



# LOGGING = {
#     'version' :1,
#     'disable_existing_loggers':False,
    
#     'loggers':{
#         'core':{
#             'handlers':[
                
#             ]
#         }
#     } 
    
# }





