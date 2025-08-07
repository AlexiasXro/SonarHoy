from django.shortcuts import render, redirect
from .forms import ContactoForm

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'components/contacto_admin/gracias.html')  
    else:
        form = ContactoForm()
    return render(request, 'components/contacto_admin/contacto.html', {'form': form})
