# -*- coding: iso-8859-15 -*-

# Copyright 2004 Ivo Carrano and Giuseppe Maccario.

# This software is part of Wanted.

# Wanted is free software and is released under the terms of the GNU General
# Public License as published by the Free Software Foundation either version 2,
# or any later version. See the COPYING file for more details or look here:
# http://www.fsf.org/licenses/gpl.html

import Pmw
import Tkinter

class Status_bar(Tkinter.Frame) :
	def __init__(
			self,
			wanted,
			) :
		self._labels = {}
		self._labels['wanted'] = wanted
		Tkinter.Frame.__init__(self,
			wanted.get('main_window'),
			)

		row_label = Tkinter.Label(
			self,
			text = 'Row: ',
			).pack(side = 'left')
		self._labels['row'] = Tkinter.Label(
			self,
			text = '',
			)
		self._labels['row'].pack(side = 'left')

		column_label = Tkinter.Label(
			self,
			text = 'Col: ',
			).pack(side = 'left')
		self._labels['column'] = Tkinter.Label(
			self,
			text = '',
			)
		self._labels['column'].pack(side = 'left')

		self._labels['message_bar'] = Pmw.MessageBar(
			self,
			labelpos = 'w',
			label_text = 'Status:',
			)
		self._labels['message_bar'].pack(
			side = 'left',
			fill = 'x',
			expand = True,
			)

	def set_labels(
			self,
			event = None,
			) :
		row, column = self._labels['wanted'].get(
			self._labels['wanted'].get('notebook').getcurselection()	# Returns the active tab
			).component('textbox').index('insert').split('.')
		self._labels['row'].config(text = row)
		self._labels['column'].config(text = int(column) + 1)

	def get(
			self,
			*a
			) :
		if len(a) == 1 :
			return self._labels[a[0]]
		else :
			values = []
			for i in a :
				values.append(self._labels[i])
			return values
