$(document).ready(function () {

    // Al enviar el formulario, mostramos feedback visual
    // Django maneja la autenticación en views.py
    $('#login').on('submit', function () {
        const btn = $(this).find('button[type="submit"]');
        btn.prop('disabled', true);
        btn.html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Ingresando...');
    });

});