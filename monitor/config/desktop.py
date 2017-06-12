# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Monitor",
			"color": "grey",
			"icon": "octicon octicon-eye",
			"type": "module",
			"label": _("Monitor")
		}
	]
