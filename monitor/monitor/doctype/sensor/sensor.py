# -*- coding: utf-8 -*-
# Copyright (c) 2017-2018, libracore and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Sensor(Document):
    # load last 100 data points
    def get_last_datapoints(self):
        sql_query = "SELECT `date`, `time`, `value` FROM `tabSensor data` WHERE `sensor_name`= '{0}'".format(self.name)
        records = frappe.db.sql(sql_query, as_dict = True)
        #split into time and temperature vectors
        time = []
        temperature = []
        for record in records:
            time_parts = str(record.time).split(":")
            time.append("{0} {1}:{2}".format(record.date, time_parts[0], time_parts[1]))
            temperature.append(record.value)
        
        return { 'time': time, 'temperature': temperature }
	
