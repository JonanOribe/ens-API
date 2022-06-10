import json
import os
from configparser import ConfigParser
from bson import json_util

import urllib
import urllib.request as urllib2
import json
import time
import hmac,hashlib
import codecs

def get_config_file_data():
    configFilePath:str =  '\\'.join(os.path.abspath(__file__).split('\\')[:3])
    config_file = configFilePath + '\\config.cfg'
    config = ConfigParser()
    return config,config_file

def json_auto_formatter(collection_as_list):
    return json.loads(json_util.dumps(collection_as_list))