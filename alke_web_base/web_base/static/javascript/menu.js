$(document).ready(function () {
    // MANTENEMOS: Solo la lógica visual para abrir/cerrar el menú lateral
    $("#menu-toggle, #sidebar-overlay").on('click', function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
        $("#sidebar-overlay").toggleClass("d-none");
    });

    // TODO LO DEMÁS FUE ELIMINADO
    // Las redirecciones ahora se hacen con etiquetas <a> en el HTML de Django
    // El saldo ahora lo inyecta Python con la etiqueta {{ saldo_actual }}
});