$.getScript("/static/js/helpers.js")
  .done(function() {
    console.debug("helpers.js loaded");
  })
  .fail(function() {
    console.error("helpers.js not loaded");
  })

function save_tetkik(data) {
  var muayene_id = $("#muayene-id").val();
  var istek_id = $("#istek-id").val();
  var request_status = $("#request-status");

  request = $.post('/muayene/' + muayene_id + '/tetkik/' + istek_id + '/sonuc/', {...data});

  request.done(function(response, textStatus, jqXHR) {
    request_status.html("<div class='alert alert-success'>Tetkik kaydedildi.</div>")
  });

  request.fail(function(jqXHR, textStatus, errorThrown) {
    request_status.html("<div class='alert alert-danger'>Tetkik kaydedilemedi.</div>")
    console.error("save_tetkik", textStatus, errorThrown);
  });
}

$(document).ready(function() {

  $('#submit-button').on('click', function() {
    var data = {};
    $('#sonuc-forms form').each(function() {
      var id = $('select', this).val();
      var sonuc = $('input', this).val();
      if(sonuc.length === 0) {
        return;
      }
      data[id] = sonuc;
    });
    save_tetkik(data);
  });

});
