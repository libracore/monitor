# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "monitor"
app_title = "Monitor"
app_publisher = "Libracore AG"
app_description = "Environmental monitor app"
app_icon = "octicon octicon-eye"
app_color = "grey"
app_email = "lars.mueller@hseag.com"
app_license = "GPL"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/monitor/css/monitor.css"
# app_include_js = "/assets/monitor/js/monitor.js"

# include js, css files in header of web template
# web_include_css = "/assets/monitor/css/monitor.css"
# web_include_js = "/assets/monitor/js/monitor.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "monitor.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "monitor.install.before_install"
# after_install = "monitor.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "monitor.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"monitor.tasks.all"
# 	],
# 	"daily": [
# 		"monitor.tasks.daily"
# 	],
# 	"hourly": [
# 		"monitor.tasks.hourly"
# 	],
# 	"weekly": [
# 		"monitor.tasks.weekly"
# 	]
# 	"monthly": [
# 		"monitor.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "monitor.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "monitor.event.get_events"
# }

