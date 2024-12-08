from django.shortcuts import render

# Función para el índice
def index(request):
    return render(request, 'index.html')
