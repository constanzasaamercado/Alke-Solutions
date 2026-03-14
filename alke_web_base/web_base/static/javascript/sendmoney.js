$(document).ready(function() {
    
    // 1. EFECTO VISUAL AL ENVIAR EL FORMULARIO
    // En lugar de calcular el saldo aquí, dejamos que el <form> viaje a Django.
    // Solo agregamos este detalle para evitar que el usuario haga doble clic.
    $('form').on('submit', function() {
        const btnSubmit = $(this).find('button[type="submit"]');
        btnSubmit.prop('disabled', true);
        btnSubmit.html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Procesando...');
    });

    // 2. LÓGICA DEL MODAL "NUEVO CONTACTO"
    // Mantenemos esto en JavaScript para que la experiencia sea fluida sin recargar la página.
    $('#btn-guardar-contacto').on('click', function() {
        const nombreContacto = $('#nombre-contacto').val();
        const idContacto = $('#id-contacto').val();

        if(nombreContacto !== "" && idContacto !== "") {
            // Agregamos visualmente el nuevo contacto a la lista desplegable (<select>)
            $('#lista-contactos-select').append(new Option(nombreContacto, idContacto));
            
            // Limpiamos los campos del modal para la próxima vez
            $('#nombre-contacto').val('');
            $('#id-contacto').val('');
            
            // Nota: El modal se cierra automáticamente gracias al atributo data-bs-dismiss="modal" que pusimos en el HTML.
        } else {
            alert("Por favor, completa los datos del contacto.");
        }
    });

    // TODO LO DEMÁS FUE ELIMINADO:
    // - Las funciones registrarMovimiento()
    // - El uso de localStorage.getItem('saldo')
    // - La función formatCLPLocal() (En Django usaremos filtros de plantillas)
});