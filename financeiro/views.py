"""financeiro VIEW Configuration

[...]
"""
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django_tables2 import RequestConfig


from financeiro import models
from rest_framework import viewsets
from . import serializers
from . import models
from .models import Usuario, LancamentoPagar, LancamentoReceber,Tesouraria

from .forms import UsuarioForm,EmpresaForm,ClienteForm,FornecedorForm,ContaBancariaForm,PlanodeContaForm,FormaPagamentoForm,LancamentoReceberForm,LancamentoPagarForm,BaixasPagarForm,BaixasReceberForm,TesourariaForm


def cadUsuario(request):
         form = UsuarioForm(request.POST)
         if form.is_valid():
             usaurio = form.save(commit=False)
             usaurio.save()
         return render(request, 'CadastroUsuario.html', {'form': form})



def cadEmpresa(request):
     form = EmpresaForm()
     if form.is_valid():
         empresa = form.save(commit=False)
         empresa.save()
     return render(request, 'CadastroEmpresa.html', {'form': form})


def cadCliente(request):
    form = ClienteForm(request.POST)
    if form.is_valid():
        cliente = form.save(commit=False)
        cliente.save()
    return render(request, 'CadastroClientes.html', {'form': form})

def cadFornecedores(request):
    form = FornecedorForm(request.POST)
    if form.is_valid():
        fonecedore = form.save(commit=False)
        fonecedore.save()
    return render(request, 'CadastroFornecedores.html', {'form': form})


def cadConta(request):
    form = ContaBancariaForm(request.POST)
    if form.is_valid():
        conta = form.save(commit=False)
        conta.save()

    return render(request, 'CadastroConta.html', {'form': form})


def cadPlanoConta(request):
    form = PlanodeContaForm(request.POST)
    if form.is_valid():
        planoconta = form.save(commit=False)
        planoconta.save()

    return render(request, 'PlanosDeContas.html', {'form': form})



def cadFormasPagamento(request):
    form = FormaPagamentoForm(request.POST)
    if form.is_valid():
        formapagamento = form.save(commit=False)
        formapagamento.save()

    return render(request, 'FormaDePagamento.html', {'form': form})


def cadLacamentoReceber(request):
    form = LancamentoReceberForm(request.POST)
    if form.is_valid():
        lancamentoreceber = form.save(commit=False)
        lancamentoreceber.save()
    return render(request, 'LancamentoReceber.html', {'form': form})


def cadBaixaContasReceber(request):
    form = LancamentoReceberForm(request.POST)
    if form.is_valid():
        lancamentoreceber = form.save(commit=False)
        lancamentoreceber.save()
    return render(request, 'BaixaDeContasReceber.html', {'form': form})

def cadTesouraria(request):
    form = TesourariaForm(request.POST)
    if form.is_valid():
        tesourario = form.save(commit=False)
        tesourario.save()

    return render(request, 'Tesouraria.html',{'form': form})



def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'registration/login.html')

def logout_view(request):
   logout(request)
   return redirect('login.html')



"Relatorio  lancamentos de contas a receber cadastradas "
def lancamento_receber_list(request):
    lancamentosreceber =LancamentoReceber.objects.filter()
    return render(request, 'lancamentosReceberList.html', {'lancamentosreceber' : lancamentosreceber})


"Relatorio  lancamentos de contas a Pagar cadastradas "
def lancamento_pagar_list(request):
    lancamentospagar = LancamentoPagar.objects.filter()
    return render(request, 'lancamentosPagarList.html', {'lancamentospagar' : lancamentospagar})


"Relatorio  lancamentos de contas a Pagar cadastradas "
def tesouraria_list(request):
    tesouraria = Tesouraria.objects.filter()
    return render(request, 'tesouriaList.html', {'tesouraria' : tesouraria})




def usuario_list(request):
    usuarios = Usuario.objects.filter()
    return render(request, 'usuario_list.html', {'usuarios': usuarios})

def empresa_list(request):
    empresas = Empresa.objects.filter()
    return render(request, 'financeiro', {'empresas': empresas})

def cliente_list(request):
    clientes = Cliente.objects.filter()
    return render(request, 'financeiro', {'clientes': clientes})

def fornecedor_list(request):
    fornecedores = Fornecedor.objects.filter()
    return render(request, 'financeiro', {'fornecedores': fornecedores})
