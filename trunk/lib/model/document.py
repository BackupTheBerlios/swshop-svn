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

"""Document-centric approach to resources."""

__revision__ = '$Id$'

import resource


class Document:
    
    def __init__(self):
        self.sections = []


class Section:
    pass


class Header(Section):
    pass


class Footer(Section):
    pass


class Menu(Section):
    pass


class MainMenu(Menu):
    pass