from __future__ import unicode_literals
from frappe import _

def get_data():
    return[
        {
            "label": _("Monitor"),
            "icon": "fa fa-chart-area",
            "items": [
                   {
                       "type": "doctype",
                       "name": "Sensor",
                       "label": _("Sensor"),
                       "description": _("Sensor list")
                   },
                   {
                       "type": "doctype",
                       "name": "Sensor data",
                       "label": _("Sensor data"),
                       "description": _("Sensor data")
                   }
            ]
        }
    ]
