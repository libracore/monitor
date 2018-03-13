// Copyright (c) 2017-2018, libracore and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sensor', {
	refresh: function(frm) {
        fetch_data(frm);
	}
});

function fetch_data(frm) {
    frappe.call({
        method: 'get_last_datapoints',
        doc: frm.doc,
        callback: function(response) {
            if (response != null) {
                create_line_chart(response.message.time, response.message.temperature);
                
                // write values to doc as well
                cur_frm.set_value('chart_time', response.message.time.toString());
                cur_frm.set_value('chart_temperature', response.message.temperature.toString());  
                // refresh form 
                refresh_field(['chart_time', 'chart_temperature']);
            }
        }
    }); 
}

function create_line_chart(time, temperature) {
    var parent = document.querySelectorAll('[data-fieldname="chart"]')[0];
    let chart = new Chart( parent, { 
        data: {
          labels: time,
          datasets: [
            {
              label: "Temperature", type: 'line',
              values: temperature
            }
          ],
          yMarkers: [{ label: "Threshold", value: 30 }]
        },
        lineOptions: { hideDots: 1, regionFill: 1 },
        title: "Temperature",
        type: 'line', 
        height: 250,
        colors: ['green']
    });

}
