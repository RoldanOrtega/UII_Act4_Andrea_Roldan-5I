from django.shortcuts import render 

# Create your views here.

def index(request):
    productos = [
        {
            'nombre': 'Superman #1',
            'precio': '3.99',
            'imagen': 'superman_1.jpg' # Puedes cambiar esto por la URL real de la imagen
        },
        {
            'nombre': 'Batman: The Killing Joke',
            'precio': '14.99',
            'imagen': 'batman_killing_joke.jpg'
        },
        {
            'nombre': 'Watchmen',
            'precio': '19.99',
            'imagen': 'watchmen.jpg'
        }
    ]
    contexto = {'productos': productos}
    return render(request, 'index.html', contexto)
