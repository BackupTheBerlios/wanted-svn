# -*- coding: iso-8859-15 -*-

# Copyright 2004 Ivo Carrano and Giuseppe Maccario.

# This software is part of Wanted.

# Wanted is free software and is released under the terms of the GNU General
# Public License as published by the Free Software Foundation either version 2,
# or any later version. See the COPYING file for more details or look here:
# http://www.fsf.org/licenses/gpl.html

import Pmw

class Info_about :
	def __init__(
			self,
			wanted,
			) :
		self._wanted = wanted
		wanted.get('command_box').set(info_about = self)
	def __call__(self) :
		Pmw.aboutversion('0.1')
		Pmw.aboutcopyright(
			'Copyright 2004\n' +
			'Ivo Carrano and Giuseppe Maccario\n' +
			'All Right Reserved'
			)
		Pmw.aboutcontact(
			'http://www.wanted.org/\n' +
			'License: GNU GPL2'
			)
		about = Pmw.AboutDialog(applicationname = 'WANTED - WANton Text EDitor')
		about.withdraw()
		about.show()
