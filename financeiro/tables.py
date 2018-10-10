import django_tables2 as tables
from .models import  LancamentoPagar, LancamentoReceber

class LacamentosReceberTable(tables.Table):
    class Meta:
        model = LancamentoReceber

class LancamentoPagarTable(tables.Table):
    class Meta:
        model = LancamentoPagar
