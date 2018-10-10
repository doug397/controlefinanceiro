from django.contrib import admin
from .models import Usuario
from .models import Empresa
from .models import Cliente
from .models import Fornecedor
from .models import ContaBancaria
from .models import FormaPagamento
from .models import PlanodeConta
from .models import BaixasReceber
from .models import LancamentoReceber
from .models import BaixasPagar
from .models import LancamentoPagar
from .models import Tesouraria



admin.site.register(Usuario)
admin.site.register(Empresa)
admin.site.register(Cliente)
admin.site.register(Fornecedor)
admin.site.register(ContaBancaria)
admin.site.register(FormaPagamento)
admin.site.register(PlanodeConta)
admin.site.register(BaixasReceber)
admin.site.register(LancamentoReceber)
admin.site.register(LancamentoPagar)
admin.site.register(Tesouraria)
