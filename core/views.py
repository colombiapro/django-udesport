from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from .models import Usuario, Eventos
from .forms import EventoForm
from django.contrib.auth import authenticate, login
f = False

# Create your views here.
def home(request):
    return render(request, 'core/home.html')


@login_required
def eventos(request):
    eventos = Eventos.objects.all()  #recibir los objetos del modelo
    print(request.user)  # Verifica si el usuario está autenticado
    print(eventos)
    return render(request, 'core/eventos.html', {"user":request.user, "eventos":eventos})

def create_event(request):
    evento = Eventos(
        nombre_ev = request.POST['nombre_ev'],  #lo que esta dentro de POST es lo mismo que se pone en el name del input en html
        fecha = request.POST['fecha'],
        lugar = request.POST['lugar'],
        descripcion = request.POST['descripcion']
    )
    evento.save()
    return redirect('eventos')

def delete_event(request, id): #debe ir el id como parametro porque lo estamos capturando en el action del form
    delete_event = Eventos.objects.get(id=id)
    delete_event.delete()
    return redirect('eventos')

def edit_event(request, id):
    edit_event = Eventos.objects.get(id=id)
    forms = EventoForm(request.POST or None, instance=edit_event)
    if forms.is_valid() and request.POST:
        forms.save()
        return redirect('eventos')
    return render(request, 'core/edit_event.html', {"user":request.user, "forms":forms})
        
    


def exit(request):
    logout(request)
    return redirect('home')

@login_required
def rendimiento(request):
    
    return render(request, 'core/rendimiento.html',{ })


def signup(request):
    print("asdasd")
    if request.method == 'POST':
        codigo = request.POST['username']
        password = request.POST['password']
        try:
            usuario = Usuario.objects.get(codigo=codigo, password=password)
            print("entro ")
            #Autenticación exitosa, redirigir a una página de éxito o realizar alguna acción
            #Por ejemplo, puedes redirigir al usuario a su página de perfil
            f =  True
            login(request, usuario)

            return render(request,'core/eventos.html', {"user":request.user})   
        except Usuario.DoesNotExist:
            print("codigo o clave incorrecto")
            mensaje_error = "Código o clave incorrectos. Por favor, inténtalo de nuevo."
            return render(request, 'registration/login.html', {'mensaje_error': mensaje_error}) 
    else:
        #Si la solicitud no es POST, mostrar el formulario de inicio de sesión
        print("asdasd")
        return render(request, 'core/home.html')
      
