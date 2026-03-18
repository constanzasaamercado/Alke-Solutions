$(document).ready(function () {

    // Deshabilitar el botón al enviar para evitar doble clic
    // Django maneja el procesamiento del envío en views.py
    $('form').on('submit', function () {
        const btn = $(this).find('button[type="submit"]');
        btn.prop('disabled', true);
        btn.html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Procesando...');
    });

    // Lógica del modal "Nuevo Contacto"
    // Agrega visualmente el contacto al <select> sin recargar la página
    $('#btn-guardar-contacto').on('click', function () {
        const nombre = $('#nombre-contacto').val().trim();
        const id = $('#id-contacto').val().trim();

        if (nombre !== '' && id !== '') {
            $('#lista-contactos-select').append(new Option(nombre, id));
            // Seleccionar automáticamente el contacto recién agregado
            $('#lista-contactos-select').val(id);
            // Limpiar campos del modal
            $('#nombre-contacto').val('');
            $('#id-contacto').val('');
        } else {
            alert('Por favor, completa los datos del contacto.');
        }
    });

});