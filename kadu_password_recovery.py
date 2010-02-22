#!/usr/bin/env python
"""Kadu Password Recovery tool

Copyright (C) 2010 Pawel Nadolski
Following source code is licensed under the GPL v2 License."""

import sys, os
from xml.dom import minidom

def_file = os.environ['HOME']+'/.kadu/kadu.conf.xml'

def usage():
	print 'Usage: ' + sys.argv[0] + ' [path_to_kadu.conf.xml]'

def main(argv):
	file=def_file
	if len(sys.argv) > 1:
		file=sys.argv[1]

	if not os.access(file, os.R_OK):
		print file + ' does not exist'
		usage()
		sys.exit(1)
		
	xmldoc = minidom.parse(file)
	enc_pass = ''
	for group in xmldoc.getElementsByTagName('Group'):
		if group.attributes['name'].value == 'General':
			for entry in group.getElementsByTagName('Entry'):
				if entry.attributes['name'].value == 'Password':
					enc_pass = entry.attributes['value'].value
			break

	password = ''
	if not enc_pass:
		print 'Could not locate enrypted password in ' + file
		sys.exit(2)
	else:
		for i in range(len(enc_pass)):
			password += chr(ord(enc_pass[i]) ^ 1 ^ i)
	print password

if __name__ == "__main__":
	main(sys.argv)
