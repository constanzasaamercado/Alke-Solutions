from django.shortcuts import render, redirect
from datetime import datetime


# ── Login ──
def login_view(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin@alkewallet.com' and password == '1234':
            request.session['saldo'] = 60000
            request.session['movimientos'] = []
            return redirect('menu')
        else:
            error = 'Correo o contraseña incorrectos.'

    return render(request, 'login.html', {'error': error})


# ── Menú principal ──
def menu_view(request):
    context = {
        'nombre_usuario': 'Constanza Saa',
        'saldo_actual': request.session.get('saldo', 60000),
        'numero_cuenta': '123456789'
    }
    return render(request, 'menu.html', context)


# ── Depositar ──
def deposit_view(request):
    saldo = request.session.get('saldo', 60000)

    if request.method == 'POST':
        monto = int(request.POST.get('monto', 0))
        if monto > 0:
            # Actualizar saldo
            request.session['saldo'] = saldo + monto

            # Registrar movimiento
            movimientos = request.session.get('movimientos', [])
            movimientos.insert(0, {
                'fecha': datetime.now().strftime('%d/%m/%Y %H:%M'),
                'tipo': 'Depósito',
                'detalle': 'Depósito en cuenta',
                'monto': f'+${monto:,}'.replace(',', '.')
            })
            request.session['movimientos'] = movimientos

        return redirect('menu')

    context = {'saldo_actual': saldo}
    return render(request, 'deposit.html', context)


# ── Enviar Dinero ──
def send_money_view(request):
    saldo = request.session.get('saldo', 60000)

    if request.method == 'POST':
        monto = int(request.POST.get('monto', 0))
        contacto = request.POST.get('contacto', 'Contacto')

        if monto > 0 and monto <= saldo:
            # Actualizar saldo
            request.session['saldo'] = saldo - monto

            # Registrar movimiento
            movimientos = request.session.get('movimientos', [])
            movimientos.insert(0, {
                'fecha': datetime.now().strftime('%d/%m/%Y %H:%M'),
                'tipo': 'Envío',
                'detalle': f'Enviado a {contacto}',
                'monto': f'-${monto:,}'.replace(',', '.')
            })
            request.session['movimientos'] = movimientos

        return redirect('menu')

    return render(request, 'sendmoney.html')


# ── Transacciones ──
def transactions_view(request):
    context = {
        'movimientos': request.session.get('movimientos', [])
    }
    return render(request, 'transactions.html', context)