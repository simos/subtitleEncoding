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

		chenc=chardet.detect(fileread(filename))
		print '\nWe are detecting the encoding of', filename
		print "The encoding of "+filename+" is "+chenc['encoding']+" with confidence:",chenc['confidence']
		if chenc['encoding'] == 'utf-8':
			print "The encoding of the file is already utf-8"
		elif chenc['encoding'] != '':
			print "Trying to convert '%s' from %s to utf-8" %(filename, chenc['encoding'])
			command= "iconv -f "+ chenc['encoding']+ " -t utf-8 "+ filename+ " -o "+ filename+"-utf-8"
			print "Trying to pass the following command to the terminal... good luck!\n"+command
			if os.system(str(command))==0:
				print "Seems we have made it... Well done!"
				print "Do you want to remove the old file with "+chenc['encoding']+" encoding? (y|n)"
				ask=raw_input("")
				if ask=='y':
					print "Deleting "+filename+" and replacing with the new utf-8 one!"
					command="rm "+filename
					os.system(command)
					command="mv "+filename+"-utf-8 "+filename
					os.system(command)
				else:
					print "OK... All done! Your utf-8 file is named '"+filename+"-utf-8'... Exiting now..."
					#quiting...
			else:
				print "Error... file could not be converted to utf-8"
			
			

if __name__ == '__main__':
	a = SubtitleEncoding('sample-utf8.srt')
	b = SubtitleEncoding('sample-iso8859-7.srt')
