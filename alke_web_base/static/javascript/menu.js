$(document).ready(function () {

    // Abrir/cerrar el menú lateral (sidebar)
    $("#menu-toggle, #sidebar-overlay").on('click', function (e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
        $("#sidebar-overlay").toggleClass("d-none");
    });

    // Formatear el saldo con estilo de moneda chilena
    // El valor ya viene inyectado por Django en el template con {{ saldo_actual }}
    const saldoEl = document.getElementById('saldo-display');
    if (saldoEl) {
        const valor = parseFloat(saldoEl.dataset.valor) || 0;
        saldoEl.textContent = new Intl.NumberFormat('es-CL', {
            style: 'currency',
            currency: 'CLP',
            maximumFractionDigits: 0
        }).format(valor);
    }

});