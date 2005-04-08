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

import textile


class AbstractError(Exception): pass

class Resource:
    """Abstract class for any site resource representation."""

    def __init__(self, name, **atts):
        self.name = name
        self.atts = atts

    def attributesAsString(self):
        attlist = []
        for k, v in self.atts.items():
            attlist.append(u'%s="%s"' % (k, v))
        return u' '.join(attlist)
    
    def asUnicode(self):
        """Quasi-abstract method, that must be implemented in descendant
        classes to provide resource representation as Python unicode object."""
        raise AbstractError, 'Method asUnicode() not implemented'

    def asString(self, encoding='utf-8'):
        return self.asUnicode().encode(encoding)


class HTMLHyperlink(Resource):
    """HTML hyperlink ("a" tag) representation."""

    def __init__(self, name, href, **atts):
        Resource.__init__(self, name, **atts)
        self.href = href
   
    def asUnicode(self):
        atts = self.attributesAsString()
        return u'<a href="%s" %s>%s</a>' % (self.href, atts, self.name)        


class HTMLImage(Resource):
    """HTML image ("img" tag) representation."""
    
    def __init__(self, name, source, altText, **atts):
        Resource.__init__(self, name, **atts)
        self.src = source
        self.alt = altText
    
    def asUnicode(self):
        atts = self.attributesAsString()
        return u'<img src="%s" alt="%s" %s />' % (self.src, self.alt, atts)


class HTMLFragment(Resource):
    """HTML document fragment, returned exactly as is."""
    
    def __init__(self, name, text):
        Resource.__init__(self, name)
        self.text = text
    
    def asUnicode(self):
        return self.text


class TextileFragment(Resource):
    """Document fragment, written using Textile simplified markup; asString
    returns exact "raw" fragment, asHTMLFragment returns HTMLFragment 
    instance."""
    
    def __init__(self, name, text):
        Resource.__init__(self, name)
        self.text = text
        textile.INPUT_ENCODING = 'utf-8'
        textile.OUTPUT_ENCODING = 'utf-8'
    
    def asUnicode(self):
        return self.text
    
    def asHTMLFragment(self):
        text = self.text.encode('utf-8')
        return HTMLFragment(self.name, textile.textile(text))
