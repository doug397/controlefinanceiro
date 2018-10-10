from django import forms

from .models import Usuario,Empresa,Cliente,Fornecedor,ContaBancaria,PlanodeConta,FormaPagamento,LancamentoReceber,LancamentoPagar,BaixasPagar,BaixasReceber,Tesouraria

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('usuario', 'nome','senha','confirmesenha')

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = ('razaosocial', 'identificacao','cnpj','tipoPessoa','inscricaoEstadual','inscricaoMunicipal','endereco','bairro','municipio','cep','uf','telefone','email','nomeTitular','cpf','funcao')

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('razaosocial', 'identificacao','classificacao','tipoPessoa','cnpjCpf','inscricaoEstadual','inscricaoMunicipal','endereco','bairro','municipio','cep','uf','telefone','email','nomeTitular','cpf','funcao')

class FornecedorForm(forms.ModelForm):

    class Meta:
        model = Fornecedor
        fields = ('razaosocial', 'identificacao','classificacao','tipoPessoa','cnpjCpf','inscricaoEstadual','inscricaoMunicipal','endereco','bairro','municipio','cep','uf','telefone','email','nomeTitular','cpf','funcao')

class ContaBancariaForm(forms.ModelForm):

    class Meta:
        model = ContaBancaria
        fields = ('classificacao', 'descricao','numeroConta','numeroAgencia','dataSaldoInicial','saldoInicial','caixa','banco')

class PlanodeContaForm(forms.ModelForm):

    class Meta:
        model = PlanodeConta
        fields = ('contas', 'classificacao','tipoConta','descricao','caixa','banco','fornecedor','entradaRecurso','saidaRecurso')

class FormaPagamentoForm(forms.ModelForm):

    class Meta:
        model = FormaPagamento
        fields = ('descricao',)

class LancamentoReceberForm(forms.ModelForm):
    class Meta:
        model = LancamentoReceber
        fields = ('dataVencimento', 'dataEmissao','valorItulo','numeroDocumento','empresas','clientes')


class LancamentoPagarForm(forms.ModelForm):

    class Meta:
        model = LancamentoPagar
        fields = ('dataVencimento', 'dataEmissao','valorItulo','numeroDocumento','empresas','fornecedores')

class BaixasPagarForm(forms.ModelForm):

    class Meta:
        model = BaixasPagar
        fields = ('banco', 'disponibilidade','dataBaixa','valorPago','residual','formasPagamento','lancamentosPagar')

class BaixasReceberForm(forms.ModelForm):

    class Meta:
        model = BaixasReceber
        fields = ('banco', 'disponibilidade','dataBaixa','valorPago','residual','formasPagamento','lancamentosReceber')

class TesourariaForm(forms.ModelForm):

    class Meta:
        model = Tesouraria
        fields = ('valor', 'numero','dataEmissao','dataVencimento','empresas','fornecedores','formaspagamento','clientes','planodecontas')
