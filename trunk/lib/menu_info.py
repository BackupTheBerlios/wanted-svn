# -*- coding: iso-8859-15 -*-

import cmds_info

def create_info_menu(
		self,
		wanted,
		) :

	self.addmenu(
		menuName = 'Help',
		balloonHelp = 'Content of help menu',
		)

	self.addmenuitem(
		menuName = 'Help',
		itemType = 'command',
		statusHelp = 'Show program info',
		command = cmds_info.Info_about(wanted),
		label = 'About',
		)
