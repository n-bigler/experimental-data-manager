# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys
if sys.version_info >= (3, 0):
    import configparser
else:
    import ConfigParser

class Configuration():
    def __init__(self, configPath=None):
        self.config = ConfigParser.ConfigParser()
        if configPath == None:
            #try to find .expdatman.conf in home or current directory. create it if fails
            lookUnder = []
            for loc in os.path.expanduser('~'), os.curdir:
                lookUnder.append(loc + os.sep + '.expdatman.conf')

            configFound = self.config.read(lookUnder)
            if not configFound:
                # we didn't find a config file, need to create it with None as db
                homeDir = os.path.expanduser('~')
                self.configPath = os.curdir + os.sep + '.expdatman.conf'
                self.config.add_section('DATABASE')
                self.config.set('DATABASE', 'db_path', "None")
                with open(self.configPath, 'w') as configfile:
                    self.write()

            else:
                # we found one config
                self.configPath = configFound[0]
                    
        else:
            self.configPath = configPath;

    def readConfig(self):
        self.config.read(self.configPath)

    def getConfigDB(self):
        return self.config.get('DATABASE', 'db_path');

    def setConfigDB(self, new_path):
        self.config.set('DATABASE', 'db_path', new_path);
        
    def write(self):
        with open(self.configPath, 'w') as configfile:
            self.config.write(configfile)
    
    
