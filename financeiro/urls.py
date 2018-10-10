"""financeiro URL Configuration

[...]
"""

from django.urls import path,include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
   path('usuarios',views.usuario_list,name="usuario_list"),
   path('cadusuario', views.cadUsuario, name='cadUsuario'),
   path('cadempresa', views.cadEmpresa, name='cadEmpresa'),
   path('cadconta', views.cadConta, name='cadConta'),
   path('cadplanoconta', views.cadConta, name='cadPlanoConta'),
   path('cadfornecedores', views.cadFornecedores, name='cadFornecedores'),
   path('cadformaspagamento', views.cadFormasPagamento, name='cadFormasPagamento'),
   path('cadlancamentoreceber', views.cadLacamentoReceber, name='cadLacamentoReceber'),
   path('cadbaixacontasreceber', views.cadBaixaContasReceber, name='cadBaixaContasReceber'),
   path('cadtesouraria', views.cadTesouraria, name='cadTesouraria'),
   path('cadcliente', views.cadCliente, name='cadCliente'),
   path('home', views.home, name='home'),
   path('', auth_views.login,{'template_name':'login.html'}, name='login'),
   path('logout', auth_views.logout, {'next_page': '/'}, name='logout'),


   path('relatorioLancamentosReceber', views.lancamento_receber_list, name='lancamento_receber_list'),
   path('relatorioLancamentosPagar', views.lancamento_pagar_list, name='lancamento_pagar_list'),
   path('relatoriotesouraria', views.tesouraria_list, name='tesouraria_list'),

]
