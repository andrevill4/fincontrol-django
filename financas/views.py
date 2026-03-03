from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Transacao
from .forms import TransacaoForms

def home(request):
    tipo=request.GET.get('tipo')

    transacoes = Transacao.objects.all().order_by('-data')

    if tipo in['R','D']:
        transacoes = transacoes.filter(tipo=tipo)

    receitas = (
            Transacao.objects
            .filter(tipo='R')
            .aggregate(total=Sum('valor'))['total'] or 0
        )

    despesas = (
            Transacao.objects
            .filter(tipo='D')
            .aggregate(total=Sum('valor'))['total'] or 0
        )

    saldo = receitas - despesas 

    context = {
            'transacoes': transacoes,
            'receitas': receitas,
            'despesas': despesas,
            'saldo': saldo,
            'tipo_selecionado': tipo,
        }

    return render(request, 'home.html', context) 
    

def nova_transacao(request):
    if request.method == 'POST':
        form = TransacaoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TransacaoForms()

    return render(request, 'nova_transacao.html', {'form': form})    