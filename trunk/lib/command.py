# -*- coding: iso-8859-15 -*-

# Copyright 2004 Ivo Carrano and Giuseppe Maccario.

# This software is part of Wanted.

# Wanted is free software and is released under the terms of the GNU General
# Public License as published by the Free Software Foundation either version 2,
# or any later version. See the COPYING file for more details or look here:
# http://www.fsf.org/licenses/gpl.html

class Command_box :

	def __init__(
			self,
			wanted,
			) :
		self._wanted = wanted
		self._commands = {}

	def set(
			self,
			**kw
			) :
		for k, v in kw.iteritems() :
			self._commands[k] = v
		return True

	def get(
			self,
			*args
			) :
		if len(args) == 1 :
			return self._commands[args[0]]
		else :
			values = []
			for i in args :
				values.append(self._commands[i])
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
