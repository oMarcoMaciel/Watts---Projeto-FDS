from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from .models import Locacao, Comodo, Pontodeenergia


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
            nome=name,
            estado=state
        )
        locacao.save()
        return redirect('app:home')


def CriarComodo(request):
    locacoes = Locacao.objects.all()

    if request.method == "POST":
        locacao_id = request.POST.get('locacao')
        nome_comodo = request.POST.get('nome')

        try:
            locacao = Locacao.objects.get(id=locacao_id)
            Comodo.objects.create(locacao=locacao, nome=nome_comodo)
            return redirect('app:home')  # Redirecionar após sucesso
        except Locacao.DoesNotExist:
            # Se a locação não for encontrada, exiba uma mensagem de erro
            return render(request, 'AddComodo.html', {'locacoes': locacoes, 'error': 'Locação inválida!'})

    return render(request, 'AddComodo.html', {'locacoes': locacoes})


def CriarPontodeenergia(request):
    locacoes = Locacao.objects.all()

    # Inicialmente, nenhum cômodo é carregado até que uma locação seja selecionada
    comodos = Comodo.objects.all()

    if request.method == "POST":
        locacao_id = request.POST.get('locacao')
        comodo_id = request.POST.get('comodo')
        nome_pontodeenergia = request.POST.get('nome')
        quant_gastos = request.POST.get('gastos')
        quantidadeAparelhos = request.POST.get('quantidade')

        try:
            locacao = Locacao.objects.get(id=locacao_id)
            comodo = Comodo.objects.get(id=comodo_id)

            # Verificação: o cômodo pertence à locação selecionada?
            if comodo.locacao_id != locacao.id:
                return HttpResponse("Erro: O cômodo selecionado não pertence à locação escolhida.", status=400)

            # Se a verificação for bem-sucedida, cria o ponto de energia
            Pontodeenergia.objects.create(
                locacao=locacao, 
                comodo=comodo, 
                nome=nome_pontodeenergia, 
                gastos=quant_gastos,
                quantidade = quantidadeAparelhos
            )
            return redirect('app:home')  # Redirecionar após sucesso

        except (Locacao.DoesNotExist, Comodo.DoesNotExist):
            # Exiba uma mensagem de erro se a locação ou cômodo não forem encontrados
            return render(request, 'AddPontodeenergia.html', {
                'locacoes': locacoes,
                'comodos': Comodo.objects.filter(locacao_id=locacao_id),  # Filtrar os cômodos pelo ID da locação
                'error': 'Locação ou cômodo inválidos!'
            })

    # Caso contrário, apenas carregue os cômodos da locação selecionada, se houver
    if 'locacao' in request.GET:
        locacao_id = request.GET.get('locacao')
        comodos = Comodo.objects.filter(locacao_id=locacao_id)  # Filtra cômodos pela locação

    return render(request, 'AddPontodeenergia.html', {'locacoes': locacoes, 'comodos': comodos})
