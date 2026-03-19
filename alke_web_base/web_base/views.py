from django.shortcuts import render, redirect
from datetime import datetime


# ── Login ──
def login_view(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'correo@correo.com' and password == '12345':
            request.session['saldo'] = 60000
            request.session['movimientos'] = []
            request.session['contactos'] = [
                {
                    'nombre': 'María González',
                    'cbu': '0000003100012345678901',
                    'alias': 'maria.gonzalez',
                    'banco': 'Banco Nación',
                    'correo': 'maria@correo.com'
                },
                {
                    'nombre': 'Juan Pérez',
                    'cbu': '0000003100098765432101',
                    'alias': 'juan.perez',
                    'banco': 'Banco Santander',
                    'correo': 'juan@correo.com'
                },
            ]
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
            request.session['saldo'] = saldo + monto

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


# ── Agregar contacto ──
def add_contact_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        cbu    = request.POST.get('cbu', '').strip()
        alias  = request.POST.get('alias', '').strip()
        banco  = request.POST.get('banco', '').strip()
        correo = request.POST.get('correo', '').strip()

        if nombre:
            contactos = request.session.get('contactos', [])
            contactos.append({
                'nombre': nombre,
                'cbu':    cbu,
                'alias':  alias,
                'banco':  banco,
                'correo': correo
            })
            request.session['contactos'] = contactos

    return redirect('send_money')


# ── Enviar Dinero ──
def send_money_view(request):
    saldo     = request.session.get('saldo', 60000)
    contactos = request.session.get('contactos', [])
    error     = None

    if request.method == 'POST':
        monto    = int(request.POST.get('monto', 0))
        contacto = request.POST.get('contacto', '').strip()

        if not contacto:
            error = 'Debes seleccionar un contacto.'
        elif monto <= 0:
            error = 'El monto debe ser mayor a 0.'
        elif monto > saldo:
            error = 'Saldo insuficiente.'
        else:
            request.session['saldo'] = saldo - monto

            movimientos = request.session.get('movimientos', [])
            movimientos.insert(0, {
                'fecha':   datetime.now().strftime('%d/%m/%Y %H:%M'),
                'tipo':    'Envío',
                'detalle': f'Enviado a {contacto}',
                'monto':   f'-${monto:,}'.replace(',', '.')
            })
            request.session['movimientos'] = movimientos
            return redirect('menu')

    context = {
        'saldo_actual': saldo,
        'contactos':    contactos,
        'error':        error
    }
    return render(request, 'sendmoney.html', context)


# ── Transacciones ──
def transactions_view(request):
    context = {
        'movimientos': request.session.get('movimientos', [])
    }
    return render(request, 'transactions.html', context)