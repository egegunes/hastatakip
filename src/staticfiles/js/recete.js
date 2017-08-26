$.getScript("/static/js/helpers.js")
  .done(function() {
    console.debug("helpers.js loaded");
  })
  .fail(function() {
    console.error("helpers.js not loaded");
  })

function prepare_data(data) {
  var ilac = {
    "ilac": data[0].value,
    "kullanim": data[1].value,
    "kutu": data[2].value
  };
  return ilac;
}

function add_to_storage(ilac) {
  var ilaclar = JSON.parse(sessionStorage.getItem('ilaclar'));
  if(ilaclar === null) {
    ilaclar = new Array();
  }
  ilaclar.push(ilac);
  sessionStorage.setItem('ilaclar', JSON.stringify(ilaclar));
}

function clear_form() {
  $("#id_ilac").val([]).trigger("change");
  $("#id_kullanim").val("");
  $("#id_kutu").val("");
}

function add_to_list(ilac_list, ilac) {
  ilac_list.html(ilac_list.html() + "<li>" + ilac.ilac + " - " + ilac.kullanim + " -  " + ilac.kutu + " kutu</li>");
}

function save_recete() {
  var ilaclar = sessionStorage.getItem('ilaclar');
  var muayene_id = $("#muayene-id").val();
  var request_status = $("#request-status");

  request = $.post('/muayene/' + muayene_id + '/recete/', {"ilaclar": ilaclar});

  request.done(function(response, textStatus, jqXHR) {
    request_status.html("<div class='alert alert-success'>Recete olusturuldu.</div>")
  });

  request.fail(function(jqXHR, textStatus, errorThrown) {
    request_status.html("<div class='alert alert-danger'>Recete olusturulamadi.</div>")
    console.error("save_recete", textStatus, errorThrown);
  });

  request.always(function() {
    $("#recete-ilac ul").html("");
    sessionStorage.clear();
  });
}

$(document).ready(function() {
  var recete_form = $("#ilac-form");
  var ilac_list = $("#recete-ilac ul");
  var recete_modal = $("#receteForm");

  recete_form.on("submit", function(e) {
    e.preventDefault();
    var data = $("#ilac-form :input").serializeArray();
    // Get rid of csrfmiddlewaretoken
    data.splice(0, 1)
    ilac = prepare_data(data);
    add_to_storage(ilac);
    add_to_list(ilac_list, ilac);
    clear_form();
  });

  recete_modal.on("hidden.bs.modal", function() {
    sessionStorage.removeItem("ilaclar");
    ilac_list.html("");
  });
});
