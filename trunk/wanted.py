#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

# Copyright 2004 Ivo Carrano and Giuseppe Maccario.

# This software is part of Wanted.

# Wanted is free software and is released under the terms of the GNU General
# Public License as published by the Free Software Foundation either version 2,
# or any later version. See the COPYING file for more details or look here:
# http://www.fsf.org/licenses/gpl.html

import sys
import os

# Finds modules in subdirs of the courrent package directory.
sys.path.insert(
	1,
	sys.path[0] + os.sep + 'lib'
	)

import Pmw
import config
import command
import menu_bar
import status_bar

class Wanted :

	def __init__(self) :
		self._components = {}
		self._components['tab_count'] = 1
		self._components['config_box'] = config.Config_box(self)
		self._components['command_box'] = command.Command_box(self)
		self._components['main_window'] = Pmw.initialise()
		self._components['main_window'].title(
			self._components['config_box'].get('main_title'),
			)
		self._components['config_box'].set(
			balloon = Pmw.Balloon(self._components['main_window']),
			)
		self._components['menu_bar'] = menu_bar.Menu_bar(self)
		self._components['main_window'].configure(menu = self._components['menu_bar'])
		self._components['notebook'] = Pmw.NoteBook(
			self._components['main_window'],
			borderwidth = self._components['config_box'].get('border_width'),
			pagemargin = self._components['config_box'].get('page_margin'),
			tabpos = self._components['config_box'].get('tab_position'),
			hull_width = 640,
			hull_height = 480,
			)
		self._components['notebook'].component('hull')['borderwidth'] = self._components['config_box'].get('border_width')
		self._components['status_bar'] = status_bar.Status_bar(self)
		self._components['config_box'].get('balloon').configure(
			statuscommand = self._components['status_bar'].get('message_bar').helpmessage,
			)
		self._components['command_box'].get('file_new').__call__()
		self._components['notebook'].configure(
			raisecommand = self._components['status_bar'].set_labels,
			)
		self._components['notebook'].pack(
			fill = 'both',
			expand = True
			)
		self._components['status_bar'].pack(
			fill = 'x',
			expand = True,
			)
		self._components['main_window'].mainloop()

	def set(
			self,
			**kw
			) :
		self._components.update(kw)

	def get(
			self,
			*a
			) :
		if len(a) == 1 :
			return self._components[a[0]]
		else :
			values = []
			for i in a :
				values.append(self._components[i])
			return values

	def increment_tab_count(self) :
		self._components['tab_count'] += 1

	def set_foo(
			self,
			**kw
			) :
		return True

	def get_foo(
			self,
			*a
			) :
		if len(a) == 1 :
			return True
		else :
			values = []
			for i in a :
				values.append(True)
			return values


Wanted()
