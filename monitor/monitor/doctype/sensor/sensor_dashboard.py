from frappe import _

def get_data():
   return {
      'fieldname': 'sensor_name',
      'transactions': [
         {
            'label': _('Data'),
            'items': ['Sensor data']
         }
      ]
   }
