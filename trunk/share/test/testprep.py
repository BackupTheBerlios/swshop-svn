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

"""
Test preparation module
"""

import os, sys
import os.path as op

libPath = \
    op.join(op.dirname(op.dirname(op.dirname(op.abspath(sys.argv[0])))), 'lib')
sys.path.insert(0, libPath)
