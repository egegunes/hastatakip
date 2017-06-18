$(document).ready(function() {

    $('.datepicker').datepicker({
        format: "yyyy-mm-dd",
        language: "tr",
        todayHighlight: true
    });

    $('[data-toggle="popover"]').popover()

    $('#homahesapla').click(function() {
        glikoz = $('#glikoz').val();
        insulin = $('#insulin').val();

        homa = (glikoz * insulin) / 405

        $('#homasonuc').append('<h5>HOMA: ' + homa + '</h5>');
    });

    $('#hba1chesapla').click(function() {
        glikozhba1c = $('#glikozhba1c').val();

        hba1c = (28.7 * glikozhba1c) - 46.7

        $('#hba1csonuc').append('<h5>HbA1c: ' + hba1c + '</h5');
    });

    function getCookie(name) {
        var cookieValue = null;
        if(document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for(var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if(cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $('#id_ilac1').on('change', function() {
        $ilac = parseInt($(this).val());
        $.ajax({
            beforeSend: function(xhr, settings) {
                if(!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            type: "POST",
            data: {action: "get_kullanim", ilac: $ilac},
            success: function(data) {
                var obj = jQuery.parseJSON(data);
                $('#id_ilac1_kullanim').val(obj.kullanim);
            }
        });
    });

    $('#id_ilac2').on('change', function() {
        $ilac = parseInt($(this).val());
        $.ajax({
            beforeSend: function(xhr, settings) {
                if(!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            type: "POST",
            data: {action: "get_kullanim", ilac: $ilac},
            success: function(data) {
                var obj = jQuery.parseJSON(data);
                $('#id_ilac2_kullanim').val(obj.kullanim);
            }
        });
    });

    $('#id_ilac3').on('change', function() {
        $ilac = parseInt($(this).val());
        $.ajax({
            beforeSend: function(xhr, settings) {
                if(!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            type: "POST",
            data: {action: "get_kullanim", ilac: $ilac},
            success: function(data) {
                var obj = jQuery.parseJSON(data);
                $('#id_ilac3_kullanim').val(obj.kullanim);
            }
        });
    });

    $('#id_ilac4').on('change', function() {
        $ilac = parseInt($(this).val());
        $.ajax({
            beforeSend: function(xhr, settings) {
                if(!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            type: "POST",
            data: {action: "get_kullanim", ilac: $ilac},
            success: function(data) {
                var obj = jQuery.parseJSON(data);
                $('#id_ilac4_kullanim').val(obj.kullanim);
            }
        });
    });

    $('#id_ilac5').on('change', function() {
        $ilac = parseInt($(this).val());
        $.ajax({
            beforeSend: function(xhr, settings) {
                if(!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            type: "POST",
            data: {action: "get_kullanim", ilac: $ilac},
            success: function(data) {
                var obj = jQuery.parseJSON(data);
                $('#id_ilac5_kullanim').val(obj.kullanim);
            }
        });
    });

    $('.print').on('click', function() {
        setTimeout(function() {
            window.location.reload(true);
        }, 100);
    });

    $('#TTF').click(function() {
        $("#TTFform").submit();
    });

    $('#muayene-list-pdf').click(function() {
        $("#MuayeneListForm").submit();
    });

    $('#yakinma-label').on('click', function() {
        $field = $('#id_yakinma')
        $shorthand = $field.val();
        $.ajax({
            beforeSend: function(xhr, settings) {
                if(!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            type: "POST",
            data: {action: "get_long", shorthand: $shorthand},
            success: function(data) {
                var obj = jQuery.parseJSON(data);
                $field.val(obj.longhand);
            }
            
        });
    });

    $('#baki-label').on('click', function() {
        $field = $('#id_baki')
        $shorthand = $field.val();
        $.ajax({
            beforeSend: function(xhr, settings) {
                if(!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            type: "POST",
            data: {action: "get_long", shorthand: $shorthand},
            success: function(data) {
                var obj = jQuery.parseJSON(data);
                $field.val(obj.longhand);
            }
            
        });
    });

    $('#tani-label').on('click', function() {
        $field = $('#id_ontani_tani')
        $shorthand = $field.val();
        $.ajax({
            beforeSend: function(xhr, settings) {
                if(!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            type: "POST",
            data: {action: "get_long", shorthand: $shorthand},
            success: function(data) {
                var obj = jQuery.parseJSON(data);
                $field.val(obj.longhand);
            }
            
        });
    });

    $('#oneri-label').on('click', function() {
        $field = $('#id_oneri_gorusler')
        $shorthand = $field.val();
        $.ajax({
            beforeSend: function(xhr, settings) {
                if(!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            type: "POST",
            data: {action: "get_long", shorthand: $shorthand},
            success: function(data) {
                var obj = jQuery.parseJSON(data);
                $field.val(obj.longhand);
            }
            
        });
    });

    $('#id_custom1_ad').on('change', function() {
        $checkbox = $('#id_custom1') 
        $checkbox.prop('checked', true);
    });

    $('#id_custom2_ad').on('change', function() {
        $checkbox = $('#id_custom2') 
        $checkbox.prop('checked', true);
    });

    $('#id_custom3_ad').on('change', function() {
        $checkbox = $('#id_custom3') 
        $checkbox.prop('checked', true);
    });

    $('#id_custom4_ad').on('change', function() {
        $checkbox = $('#id_custom4') 
        $checkbox.prop('checked', true);
    });

    $('#id_custom5_ad').on('change', function() {
        $checkbox = $('#id_custom5') 
        $checkbox.prop('checked', true);
    });
});
