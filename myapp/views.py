from django.shortcuts import render, redirect
from django.contrib import messages
from firebase_admin import auth

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = auth.create_user(
                email=email,
                password=password,
            )
            messages.success(request, 'Registrasi berhasil. Silakan login.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error: {e}')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = auth.get_user_by_email(email)
            # Lakukan verifikasi password di sini sesuai kebutuhan
            messages.success(request, 'Login berhasil.')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'Error: {e}')

    return render(request, 'login.html')
