# -*- coding: utf-8 -*-

# This file is part of Site Workshop, a "site object model" implementation of
# content management system for small sites (eg. weblogs)
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

import unittest
import ConfigParser
import os
import os.path as op

import testprep

import config

class ConfigTests(unittest.TestCase):
    
    def setUp(self):
        self.fileName = op.expanduser('~/.test.cfg')
        self.cfg = config.Config(self.fileName)
    
    def test_setOption(self):
        self.cfg.setOption('test', 'test option', 'testValue')
        val = self.cfg.get('test', 'test option')
        self.failUnless(val == 'testValue')

    def test_getExistingOption(self):
        self.cfg.add_section('test')
        self.cfg.set('test', 'option', 'value')
        val = self.cfg.getOption('test', 'option', 'default')
        self.failUnless(val == 'value')

    def test_getNonExistingOption(self):
        self.cfg.add_section('test')
        val = self.cfg.getOption('test', 'option', 'default')
        self.failUnless(val == 'default')

    def test_saveConfig(self):
        self.cfg.setOption('test', 'option', 'value')
        self.cfg.save()
        cp = ConfigParser.SafeConfigParser()
        fp = open(self.fileName)
        try:
            cp.readfp(fp)
        finally:
            fp.close()
        val = cp.get('test', 'option')
        self.failUnless(val == 'value')

    def tearDown(self):
        if os.access(self.fileName, os.F_OK):
            os.unlink(self.fileName)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
