$(document).ready(function() {
    var date = $("input[name='date']");
    var target = $("#randevu-list");

    date.change(function() {
        var value = $(this).val();

        $.ajax({
            method: 'GET',
            url: '/randevu/list/?date=' + encodeURIComponent(value),
            dataType: 'json',
            success: function(data) {
                var value_to_date = new Date(value);
                var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
                html = '<h2>' + value_to_date.toLocaleDateString('tr', options) + '</h2><h3>Randevu Listesi</h3>';
                keys = Object.keys(data);
                keys.sort();
                for(var i = 0; i < keys.length; i++) {
                    var time = keys[i];
                    var hasta = data[keys[i]];
                    html = html + '<p><b>' + time + '</b> - ' + hasta['name'] + ' (' + hasta['person_number'] + ' kişi)</p>';
                }
                target.html(html);
            }
        });
    });
});
