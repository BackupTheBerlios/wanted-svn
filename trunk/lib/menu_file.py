# -*- coding: iso-8859-15 -*-

# Copyright 2004 Ivo Carrano and Giuseppe Maccario.

# This software is part of Wanted.

# Wanted is free software and is released under the terms of the GNU General
# Public License as published by the Free Software Foundation either version 2,
# or any later version. See the COPYING file for more details or look here:
# http://www.fsf.org/licenses/gpl.html

import cmds_file

def create_file_menu(
		self,
		wanted,
		) :

	self.addmenu(
		menuName = 'File',
		balloonHelp = 'Content of file menu',
		)

	self.addmenuitem(
		menuName = 'File',
		itemType = 'command',
		statusHelp = 'Create a new edit tab',
		command = cmds_file.File_new(wanted),
		label = 'New',
		)
