# -*- coding: iso-8859-15 -*-

# Copyright 2004 Ivo Carrano and Giuseppe Maccario.

# This software is part of Wanted.

# Wanted is free software and is released under the terms of the GNU General
# Public License as published by the Free Software Foundation either version 2,
# or any later version. See the COPYING file for more details or look here:
# http://www.fsf.org/licenses/gpl.html

import Pmw
import menu_file
import menu_info

class Menu_bar(Pmw.MainMenuBar) :

	def __init__(
			self,
			wanted,
			) :
		Pmw.MainMenuBar.__init__(
			self,
			parent = wanted.get('main_window'),
			balloon = wanted.get('config_box').get('balloon'),
			hotkeys = True,
			)

		self.component('hull')['borderwidth'] = wanted.get('config_box').get('menu_bar_border_width')

		menu_file.create_file_menu(
			self,
			wanted,
			)
		menu_info.create_info_menu(
			self,
			wanted,
			)
