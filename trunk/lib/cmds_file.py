# -*- coding: iso-8859-15 -*-

# Copyright 2004 Ivo Carrano and Giuseppe Maccario.

# This software is part of Wanted.

# Wanted is free software and is released under the terms of the GNU General
# Public License as published by the Free Software Foundation either version 2,
# or any later version. See the COPYING file for more details or look here:
# http://www.fsf.org/licenses/gpl.html

import Pmw

class File_new :
	def __init__(
			self,
			wanted,
			) :
		self._wanted = wanted
		wanted.get('command_box').set(file_new = self)
	def __call__(self) :
		"""Create a new, blank editing window"""
		name = 'Untitled ' + str(self._wanted.get('tab_count'))
		tab = self._wanted.get('notebook').add(name)
		self._wanted.increment_tab_count()
		text_box = Pmw.ScrolledText(
				tab,
				labelpos = 'n',
				label_text = name,
				borderframe = 1,
				)
		self._wanted.set(**{
			name : text_box,
			})
		self._wanted.get('notebook').selectpage(name)
		Pmw.Color.changecolor(
			text_box.component('textbox'),
			background = self._wanted.get('config_box').get('text_bgcolor'),
			)
		text_box.component('textbox').bind(
			'<KeyRelease>',
			self._wanted.get('status_bar').set_labels,
			)
		text_box.component('textbox').bind(
			'<ButtonRelease>',
			self._wanted.get('status_bar').set_labels,
			)
		text_box.component('textbox').after_idle(self._wanted.get('status_bar').set_labels)
		text_box.pack(
			fill = 'both',
			expand = True
			)
