$(document).ready(function() {
    // Cuando el usuario haga clic en iniciar sesión...
    $('#login').submit(function() {
        // IMPORTANTE: Ya NO usamos event.preventDefault();
        // Esto permite que el formulario viaje a Python (views.py)

        // Mantenemos solo la parte visual (el loader)
        $('#login').fadeOut(300, function() {
            $('#loader').fadeIn(300);
        });
    });
});