# -*- coding: iso-8859-15 -*-


# Copyright 2004 Ivo Carrano and Giuseppe Maccario.

# This software is part of Wanted.

# Wanted is free software and is released under the terms of the GNU General
# Public License as published by the Free Software Foundation either version 2,
# or any later version. See the COPYING file for more details or look here:
# http://www.fsf.org/licenses/gpl.html

class Config_box :

	def __init__(self, wanted,) :
		self._options = {}
		self._options['wanted'] = wanted
		self.set(	# Defaults values
			main_title = 'Wanted',
			show_menu_bar = True,
			tab_position = None,	# must be: 'n', or 'None'
			page_margin = 0,
			border_width = 0,
			text_wrap = 'none',	# must be: 'none', 'char', or 'word'
			text_bgcolor = 'white',
			rowheader_width = 0,
			menu_bar_border_width = 0,
			)
		self.set(	# Test values
			main_title = 'Wanted',
			show_menu_bar = False,
			tab_position = 'n',
			page_margin = 0,
			border_width = 1,
			text_wrap = 'none',
			text_bgcolor = 'white',
			rowheader_width = 2,
			menu_bar_border_width = 0,
			)

	def set(
			self,
			**kw
			) :
		for k, v in kw.iteritems() :
			self._options[k] = v
		return True

	def get(
			self,
			*args
			) :
		if len(args) == 1 :
			return self._options[args[0]]
		else :
			values = []
			for i in args :
				values.append(self._options[i])
			return values

	def set_foo(
			self,
			**kw
			) :
		return True

	def get_foo(
			self,
			*args
			) :
		if len(args) == 1 :
			return True
		else :
			values = []
			for i in args :
				values.append(True)
			return values
