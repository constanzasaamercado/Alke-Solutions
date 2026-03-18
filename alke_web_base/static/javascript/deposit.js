$(document).ready(function () {

    // Deshabilitar el botón al enviar para evitar doble clic
    // Django maneja el procesamiento del depósito en views.py
    $('form').on('submit', function () {
        const btn = $(this).find('button[type="submit"]');
        btn.prop('disabled', true);
        btn.html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Procesando...');
    });

    // Validación visual del monto antes de enviar
    $('#depositAmount').on('input', function () {
        const valor = parseFloat($(this).val());
        const btn = $('button[type="submit"]');
        if (valor <= 0 || isNaN(valor)) {
            $(this).addClass('is-invalid').removeClass('is-valid');
            btn.prop('disabled', true);
        } else {
            $(this).addClass('is-valid').removeClass('is-invalid');
            btn.prop('disabled', false);
        }
    });

});