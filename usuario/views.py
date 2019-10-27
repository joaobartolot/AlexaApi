from django.shortcuts import render

from .forms import Usuario

# Create your views here.

def index(request):
    context = {}

    if request.method == 'POST':
        form = Usuario(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = Usuario()

    context['form'] = form

    return render(request, 'usuario/cadastro.html', context)
