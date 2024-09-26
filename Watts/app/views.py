from django.shortcuts import redirect, render
from django.views import View
from .models import Locacao


class HomeViews(View):
    def get(self, request):
        return render(request, 'home.html')

class AddLocacao(View):
    def get(self, request):
        return render(request, 'AddLocacao.html')

    def post(self, request):
        name = request.POST.get("nome")
        state = request.POST.get("estado")

    locacao = Locacao(
        nome = name
        estado = state
    )
    
    locacao.save()
    return redirect('app:home')
