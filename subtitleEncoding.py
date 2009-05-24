#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

# Author  : Simos Xenitellis <simos@gnome.org>, 2009
# Version : 0.1

import dircache         # dircache.listdir()
import os               # os.system(), os.remove(), os.path.gmtime(), os.getenv()
import getopt           # getopt.getopt()
import sys              # sys.argv, sys.exit()
import urllib           # urllib.urlretrieve()

try:
        import chardet  # chardet.detect()
except ImportError, err:
        print 'Import error:', err
        print 'This script requires to have the python-chardet package installed'
        print 'Please install the package python-chardet and try again.\nExiting...'
        sys.exit(1)

class SubtitleEncoding:
	def __init__(self, filename):
		urlread = lambda url: urllib.urlopen(url).read()
		fileread = lambda file: open(file).read()

		print 'We are detecting the encoding of', filename
		print chardet.detect(fileread(filename))


if __name__ == '__main__':
	a = SubtitleEncoding('sample-utf8.srt')
	b = SubtitleEncoding('sample-iso8859-7.srt')
