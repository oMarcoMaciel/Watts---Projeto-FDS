from django.shortcuts import redirect, render
from django.views import View
from .models import Locacao, Comodo,Pontodeenergia


class HomeViews(View):
    def get(self, request):
        return render(request, 'home.html')

class AddLocacao(View):
    def get(self, request):
        return render(request, 'AddLocacao.html')

    def post(self, request):
        name = request.POST.get("nome")
        state = request.POST.get("locacao")

        locacao = Locacao(
            nome = name,
            estado = state
        )
        locacao.save()
        return redirect('app:home') 

def CriarComodo(request):
    locacoes = Locacao.objects.all()

    if request.method == "POST":
        locacao_id = request.POST.get('locacao')
        nome_comodo = request.POST.get('nome')

        locacao = Locacao.objects.get(id=locacao_id)
        Comodo.objects.create(locacao=locacao, nome=nome_comodo)

    return render(request, 'AddComodo.html', {'locacoes': locacoes})

def CriarPontodeenergia(request):
    locacoes = Locacao.objects.all()
    comodos = Comodo.objects.all()

    if request.method == "POST":
        locacao_id = request.POST.get('locacao')
        comodo_id = request.POST.get('comodo')
        nome_pontodeenergia = request.POST.get('nome')
        quant_gastos = request.POST.get('gastos')

        locacao = Locacao.objects.get(id=locacao_id)
        comodo = Comodo.objects.get(id=comodo_id)
        Pontodeenergia.objects.create(locacao=locacao, comodo=comodo, nome=nome_pontodeenergia, gastos=quant_gastos)

    return render(request, 'AddPontodeenergia.html', {'locacoes': locacoes, 'comodos': comodos})


