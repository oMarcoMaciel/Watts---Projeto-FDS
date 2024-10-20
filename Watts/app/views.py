from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Locacao, Comodo, Pontodeenergia

class HomeViews(View):
    def get(self, request):
        pontosdeenergia = Pontodeenergia.objects.all()
        locacoes = Locacao.objects.all()
        comodos = Comodo.objects.all()
        return render(request, 'home.html', {
            'pontosdeenergia': pontosdeenergia,
            'locacoes': locacoes,
            'comodos': comodos
        })

class AddLocacao(View):
    def get(self, request):
        return render(request, 'AddLocacao.html')

    def post(self, request):
        name = request.POST.get("nome")
        state = request.POST.get("estado")

        locacao = Locacao(
            nome=name,
            estado=state
        )
        locacao.save()
        return redirect('home')

class DeleteLocacao(View):
    def post(self, request, locacao_id):
        locacao = get_object_or_404(Locacao, id=locacao_id)
        locacao.delete()
        return redirect('home')

class CriarComodo(View):
    def get(self, request):
        locacoes = Locacao.objects.all()
        return render(request, 'AddComodo.html', {'locacoes': locacoes})

    def post(self, request):
        locacao_id = request.POST.get('locacao')
        nome_comodo = request.POST.get('nome')

        try:
            locacao = Locacao.objects.get(id=locacao_id)
            Comodo.objects.create(locacao=locacao, nome=nome_comodo)
            return redirect('home')  # Redirecionar após sucesso
        except Locacao.DoesNotExist:
            # Se a locação não for encontrada, exiba uma mensagem de erro
            locacoes = Locacao.objects.all()
            return render(request, 'AddComodo.html', {'locacoes': locacoes, 'error': 'Locação inválida!'})

class DeleteComodo(View):
    def post(self, request, comodo_id):
        comodo = get_object_or_404(Comodo, id=comodo_id)
        comodo.delete()
        return redirect('home')

class CriarPontodeenergia(View):
    def get(self, request):
        locacoes = Locacao.objects.all()
        comodos = Comodo.objects.all()
        return render(request, 'AddPontodeenergia.html', {'locacoes': locacoes, 'comodos': comodos})

    def post(self, request):
        locacao_id = request.POST.get('locacao')
        comodo_id = request.POST.get('comodo')
        nome_pontodeenergia = request.POST.get('nome')
        quant_gastos = request.POST.get('gastos')
        quantidadeAparelhos = request.POST.get('quantidade')

        try:
            comodo = Comodo.objects.get(id=comodo_id)

            # Verificação: o cômodo pertence à locação selecionada?
            if comodo.locacao_id != int(locacao_id):
                return HttpResponse("Erro: O cômodo selecionado não pertence à locação escolhida.", status=400)

            # Validação: quantidade de aparelhos e gastos de energia não podem ser negativos
            if int(quantidadeAparelhos) < 0 or float(quant_gastos) < 0:
                return HttpResponse("Erro: A quantidade de aparelhos e o gasto de energia não podem ser negativos.", status=400)

            # Se a verificação for bem-sucedida, cria o ponto de energia
            Pontodeenergia.objects.create(
                locacao_id=locacao_id, 
                comodo=comodo, 
                nome=nome_pontodeenergia, 
                gastos=quant_gastos,
                quantidade=quantidadeAparelhos
            )
            return redirect('home')  # Redirecionar após sucesso

        except (Locacao.DoesNotExist, Comodo.DoesNotExist):
            # Exiba uma mensagem de erro se a locação ou cômodo não forem encontrados
            locacoes = Locacao.objects.all()
            comodos = Comodo.objects.all()
            return render(request, 'AddPontodeenergia.html', {
                'locacoes': locacoes,
                'comodos': comodos,
                'error': 'Locação ou cômodo inválidos!'
            })

class DeletePontodeenergia(View):
    def post(self, request, pontodeenergia_id):
        pontodeenergia = get_object_or_404(Pontodeenergia, id=pontodeenergia_id)
        pontodeenergia.delete()
        return redirect('home')