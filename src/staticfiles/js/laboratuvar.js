function save_istek(data) {
  var muayene_id = $("#muayene-id").val();
  var request_status = $("#lab-request-status");

  request = $.post('/muayene/' + muayene_id + '/tetkik/', {labs: Array.from(data)});

  request.done(function(response, textStatus, jqXHR) {
    request_status.html("<div class='alert alert-success'>Laboratuvar istek olusturuldu.</div>")
  });

  request.fail(function(jqXHR, textStatus, errorThrown) {
    request_status.html("<div class='alert alert-danger'>Laboratuvar istek olusturulamadi.</div>")
    console.error("save_istek", textStatus, errorThrown);
  });
}

$(document).ready(function() {
  var labs = new Set();

  $('input.form-check-input').on('change', function(e) {
    var value = $(this).val();
    if(labs.has(value)) {
      labs.delete(value);
    } else {
      labs.add(value);
    }
  });

  $('#istekForm').on('submit', function(e) {
    e.preventDefault();
    var custom_labs = new Set($('#id_custom_labs').val());
    var data = new Set([...labs, ...custom_labs])
    save_istek(data);
  });

  $('a.tetkik-sonuc')
});
