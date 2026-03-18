$(document).ready(function () {

    // Las transacciones ahora las entrega Django desde views.py
    // mediante el contexto del template: {{ transacciones }}
    // Este archivo queda disponible para agregar lógica visual en el futuro,
    // por ejemplo: filtros, ordenamiento o animaciones de la tabla.

    // Animación de entrada para las filas de la tabla
    $('#tabla-movimientos tr').each(function (index) {
        $(this).css('opacity', 0).delay(index * 80).animate({ opacity: 1 }, 300);
    });

});