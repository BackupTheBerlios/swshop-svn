# -*- coding: utf-8 -*-

# This file is part of SiteWorkshop project, site object model implementation.
#
#       Copyright: (c) 2005, Jarek Zgoda <jzgoda@o2.pl>
#
# SiteWorkshop is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License or, at your opinion,
# any later version.
#
# SiteWorkshop is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SiteWorkshop; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import unittest

import testprep

import textile
from model import resource

class HTMLHyperlinkTests(unittest.TestCase):

    def setUp(self):
        atts = {}
        atts['title'] = u'Strona domowa języka Python'
        atts['accesskey'] = u'p'
        self.link = resource.HTMLHyperlink(u'Python', \
            u'http://www.python.org/', **atts)

    def test_asString(self):
        link = self.link.asString()
        href = 'href="http://www.python.org/"'
        title = 'title="Strona domowa języka Python"'
        accesskey = 'accesskey="p"'
        self.failUnless(link.find(href) > -1)
        self.failUnless(link.find(title) > -1)
        self.failUnless(link.find(accesskey) > -1)


class HTMLImageTests(unittest.TestCase):
    
    def setUp(self):
        atts = {}
        atts['title'] = u'Naprawdę duży python!'
        self.img = resource.HTMLImage('Python', \
            'http://www.python.org/snake.jpg', \
            u'Zdjęcie prawdziwego Pythona', **atts)
    
    def test_asString(self):
        img = self.img.asString()
        src = 'src="http://www.python.org/snake.jpg"'
        alt = 'alt="Zdjęcie prawdziwego Pythona"'
        title = 'title="Naprawdę duży python!"'
        self.failUnless(img.find(src) > -1)
        self.failUnless(img.find(alt) > -1)
        self.failUnless(img.find(title) > -1)


class HTMLFragmentTests(unittest.TestCase):
    
    def setUp(self):
        self.text = u'''<h1>Oto jest test</h1>
            <p>A ten test będziemy za jakiś czas 
            eksploatować.</p>'''
        self.fragment = resource.HTMLFragment('Rant', self.text)
    
    def test_asString(self):
        fragment = self.fragment.asString()
        self.failUnless(self.text.encode('utf-8') == fragment)


class TextileFragmentTests(unittest.TestCase):
    
    def setUp(self):
        self.text = u'''p. Sprawdzamy, jak się to całe Textile zachowa,
            czy rzeczywiście _jest się czym_ ekscytować?'''
        self.fragment = resource.TextileFragment('Test', self.text)
    
    def test_asString(self):
        fragment = self.fragment.asString()
        self.failUnless(self.text.encode('utf-8') == fragment)
    
    def test_asHTMLFragment(self):
        textile.INPUT_ENCODING = 'utf-8'
        textile.OUTPUT_ENCODING = 'utf-8'
        tf = textile.textile(self.text.encode('utf-8'))
        frag = resource.HTMLFragment('Test', tf)
        self.failUnless(False)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
