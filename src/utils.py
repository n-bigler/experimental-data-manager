# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys
if sys.version_info >= (3, 0):
    import configparser
else:
    import ConfigParser

def readConfig(db_path):
    if sys.version_info >= (3, 0):
        config = configparser.ConfigParser()
        if db_path != None:
            # need to save a new db_path
            config['DATABASE'] = {'db_path': os.path.abspath(db_path)}
            with open(os.curdir + os.sep + '.readme2db.conf', 'w') as configfile:
                config.write(configfile)

        look_under = []
        for loc in os.path.expanduser('~'), os.curdir:
            look_under.append(loc + os.sep + '.readme2db.conf')

        config_found = config.read(look_under)
        if not config_found:
            # we didn't find a config file

            return None
        else:
            return config['DATABASE']['db_path']
    else:
        #python 2
        config = ConfigParser.ConfigParser()
        if db_path != None:
            # need to save a new db_path
            if not config.has_section('DATABASE'):
                config.add_section('DATABASE')
            config.set('DATABASE', 'db_path', os.path.abspath(db_path))
            with open(os.curdir + os.sep + '.readme2db.conf', 'w') as configfile:
                config.write(configfile)

        look_under = []
        for loc in os.path.expanduser('~'), os.curdir:
            look_under.append(loc + os.sep + '.readme2db.conf')

        config_found = config.read(look_under)
        if not config_found:
            # we didn't find a config file

            return None
        else:
            return config.get('DATABASE', 'db_path')
