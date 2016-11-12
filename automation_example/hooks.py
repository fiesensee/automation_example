# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "automation_example"
app_title = "Automation Example"
app_publisher = "Felix Isensee"
app_description = "An example of an automated Workflow between different documents"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "f.isensee@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/automation_example/css/automation_example.css"
# app_include_js = "/assets/automation_example/js/automation_example.js"

# include js, css files in header of web template
# web_include_css = "/assets/automation_example/css/automation_example.css"
# web_include_js = "/assets/automation_example/js/automation_example.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "automation_example.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "automation_example.install.before_install"
# after_install = "automation_example.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "automation_example.notifications.get_notification_config"

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
# 		"automation_example.tasks.all"
# 	],
# 	"daily": [
# 		"automation_example.tasks.daily"
# 	],
# 	"hourly": [
# 		"automation_example.tasks.hourly"
# 	],
# 	"weekly": [
# 		"automation_example.tasks.weekly"
# 	]
# 	"monthly": [
# 		"automation_example.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "automation_example.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "automation_example.event.get_events"
# }

