# -*- coding: utf-8 -*-

# This file is part of Site Workshop, a "site object model" implementation of
# content management system for small sites (eg. weblogs).
#
# Copyright: (c) 2005, Jarek Zgoda <jzgoda@o2.pl>
#
# Site Workshop is free software; you can redistribute it and/or modify it 
# under the terms of the GNU General Public License as published by the Free 
# Software Foundation; either version 2 of the License, or (at your opinion) 
# any later version.
#
# Site Workshop is distributed in the hope that it will be useful, but WITHOUT 
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more 
# details.
#
# You should have received a copy of the GNU General Public License along with
# Site Workshop; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

__revision__ = '$Id$'

import ConfigParser

class Config(ConfigParser.SafeConfigParser):
    """Generic application configuration class. Derived from SafeConfigParser,
    this class sanitizes input and performs various checks to ensure no 
    exceptions are raised for get and set operations."""
    
    def __init__(self, fileName):
        ConfigParser.SafeConfigParser.__init__(self)
        self.optionxform = str
        self.fileName = fileName
        try:
            fp = open(fileName)
            try:
                self.readfp(fp)
            finally:
                fp.close()
        except IOError:
            # config file does not exist
            pass

    def save(self):
        """Save configuration to config file."""
        fp = open(self.fileName, 'w')
        try:
            self.write(fp)
        finally:
            fp.close()

    def getOption(self, section, option, default):
        """Method returns default value if section or option does not exist
        instead of raising exceptions."""
        try:
            ret = self.get(section, option)
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
            return default
        return ret.decode('utf-8')

    def setOption(self, section, option, value):
        """Method that sanitizes option values, just to be sure they are
        always strings (Python <2.4 allows non-string values, but later
        produces weird results)."""
        if not self.has_section(section):
            self.add_section(section)
        self.set(section, option, value.encode('utf-8'))
