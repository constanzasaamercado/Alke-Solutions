from django.shortcuts import render

# Vista para el Login
def login_view(request):
    return render(request, 'login.html')

# Vista para el Menú Principal (Aquí enviamos el saldo desde Python)
def menu_view(request):
    # En el futuro, estos datos vendrán de una base de datos
    context = {
        'nombre_usuario': 'Constanza Saa',
        'saldo_actual': 60000,
        'numero_cuenta': '123456789'
    }
    return render(request, 'menu.html', context)

# Vista para Depositar
def deposit_view(request):
    context = {
        'saldo_actual': 60000  # También enviamos el saldo aquí
    }
    return render(request, 'deposit.html', context)

# Vista para Enviar Dinero
def send_money_view(request):
    return render(request, 'sendmoney.html')

# Vista para Ver Transacciones
def transactions_view(request):
    return render(request, 'transactions.html')