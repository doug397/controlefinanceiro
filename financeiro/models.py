from django.db import models
from django.utils import timezone

STATE_CHOICES = (
    	('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
    	('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
    	('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
    	('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
    	('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
    	('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    	('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
    	('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
    	('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    	('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
    )

TIPO_PESSOA_CHOICES = (
        (u'FISICA', u'Fisica'),
        (u'JURIDICA', u'Juridica'),
    )

TIPO_CONTA = (
    (u'Titulo', u'Titulo'),
)
class Usuario(models.Model):
    usuario = models.CharField('Usuario',max_length=255,null=False)
    nome = models.CharField('Nome',max_length=255, null=False)
    senha = models.CharField('Senha',max_length=50, null=False)
    confirmesenha = models.CharField('ConfirmarSenha',max_length=50, null=False)

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    razaosocial = models.CharField('Razão Social',max_length=50, null=False)
    identificacao = models.CharField('Identificacao',max_length=50, null=False)
    cnpj = models.CharField('CNPJ',max_length=15, null=False)
    tipoPessoa = models.CharField('Tipo Pessoa',max_length=10, null=False,choices=TIPO_PESSOA_CHOICES, default='Tipo Pessoa')
    inscricaoEstadual = models.CharField('Inscrição Estadual',max_length=20, null=False)
    inscricaoMunicipal = models.CharField('Inscrição Municipal',max_length=20, null=False)
    endereco = models.CharField('Endereço',max_length=50, null=False)
    bairro = models.CharField('Bairro',max_length=50, null=False)
    municipio = models.CharField('Municipio',max_length=50, null=False)
    cep = models.CharField('CEP',max_length=10, null=False)
    uf = models.CharField('UF',max_length=2, null=False,choices=STATE_CHOICES,default='UF')
    telefone = models.CharField('Telefone',max_length=20, null=False)
    email = models.EmailField('Email')
    nomeTitular = models.CharField('Nome Titular',max_length=50, null=False)
    cpf = models.CharField('CPF',max_length=15, null=False)
    funcao = models.CharField('Funcao',max_length=50, null=False)

    def __str__(self):
        return self.razaosocial

class Cliente(models.Model):
    razaosocial = models.CharField('Razão Social',max_length=50, null=False)
    identificacao = models.CharField('Identificacao',max_length=50, null=False)
    classificacao = models.CharField('Classificação',max_length=50, null=False)
    tipoPessoa = models.CharField('Tipo Pessoa',max_length=10, null=False,choices=TIPO_PESSOA_CHOICES, default='Tipo Pessoa')
    cnpjCpf = models.CharField('CNPJ/CPF',max_length=15, null=False)
    inscricaoEstadual = models.CharField('Inscrição Estadual',max_length=20, null=False)
    inscricaoMunicipal = models.CharField('Inscrição Municipal',max_length=20, null=False)
    endereco = models.CharField('Endereço',max_length=50, null=False)
    bairro = models.CharField('Bairro',max_length=50, null=False)
    municipio = models.CharField('Municipio',max_length=50, null=False)
    cep = models.CharField('CEP',max_length=10, null=False)
    uf = models.CharField('UF',max_length=2, null=False,choices=STATE_CHOICES,default='UF')
    telefone = models.CharField('Telefone',max_length=20, null=False)
    email = models.EmailField('Email')
    nomeTitular = models.CharField('Nome Titular',max_length=50, null=False)
    cpf = models.CharField('CPF',max_length=15, null=False)
    funcao = models.CharField('Funcao',max_length=50, null=False)

    def __str__(self):
        return self.razaosocial

    def is_upperclass(self):
        return self.tipoPessoa in (self.FISICA, self.JURIDICA)

class Fornecedor(models.Model):
    razaosocial = models.CharField('Razão Social',max_length=50, null=False)
    identificacao = models.CharField('Identificacao',max_length=50, null=False)
    classificacao = models.CharField('Classificação',max_length=50, null=False)
    tipoPessoa = models.CharField('Tipo Pessoa',max_length=10, null=False,choices=TIPO_PESSOA_CHOICES, default='Tipo Pessoa')
    cnpjCpf = models.CharField('CNPJ/CPF',max_length=15, null=False)
    inscricaoEstadual = models.CharField('Inscrição Estadual',max_length=20, null=False)
    inscricaoMunicipal = models.CharField('Inscrição Municipal',max_length=20, null=False)
    endereco = models.CharField('Endereço',max_length=50, null=False)
    bairro = models.CharField('Bairro',max_length=50, null=False)
    municipio = models.CharField('Municipio',max_length=50, null=False)
    cep = models.CharField('CEP',max_length=10, null=False)
    uf = models.CharField('UF',max_length=2, null=False,choices=STATE_CHOICES,default='UF')
    telefone = models.CharField('Telefone',max_length=20, null=False)
    email = models.EmailField('Email')
    nomeTitular = models.CharField('Nome Titular',max_length=50, null=False)
    cpf = models.CharField('CPF',max_length=15, null=False)
    funcao = models.CharField('Funcao',max_length=50, null=False)

    def __str__(self):
        return self.razaosocial

class ContaBancaria(models.Model):
    classificacao = models.CharField('Classificação',max_length=18, null=False)
    descricao = models.CharField('Descrição',max_length=50, null=False)
    numeroConta = models.CharField('Numero Conta',max_length=20, null=False)
    numeroAgencia = models.CharField('Numero Agencia',max_length=20, null=False)
    dataSaldoInicial = models.CharField('Data Saldo Inicial',max_length=12, null=False)
    saldoInicial = models.CharField('Saldo Inicial',max_length=12, null=False)
    caixa = models.CharField('Caixa',max_length=1, null=False)
    banco = models.CharField('Banco',max_length=1, null=False)

    def __str__(self):
        return self.descricao

class PlanodeConta(models.Model):
        contas = models.ForeignKey(ContaBancaria, on_delete=models.CASCADE)
        classificacao = models.CharField('Classificação',max_length=18, null=False)
        tipoConta = models.CharField(max_length=15, null=False,choices=TIPO_CONTA,default='Tipo Conta')
        descricao = models.CharField('Descrição',max_length=50, null=False)
        caixa = models.CharField('Caixa',max_length=1, null=False)
        banco = models.CharField('Banco',max_length=1, null=False)
        fornecedor = models.CharField(max_length=1, null=False)
        entradaRecurso = models.CharField(max_length=1, null=False)
        saidaRecurso = models.CharField(max_length=1, null=False)

        def __str__(self):
           return self.descricao


class FormaPagamento(models.Model):
    descricao = models.CharField('Descrição',max_length=50, null=False)

    def __str__(self):
        return self.descricao


class LancamentoReceber(models.Model):
    dataVencimento = models.DateTimeField('Data Vencimento',default=timezone.now)
    dataEmissao = models.DateTimeField('Data emissão',default=timezone.now)
    valorItulo = models.CharField('Valor Titulo',max_length=14, null=False)
    numeroDocumento = models.CharField('Numero Documento',max_length=20, null=False)
    empresas = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.numeroDocumento

class LancamentoPagar(models.Model):
        dataVencimento = models.DateTimeField('Data Vencimento',default=timezone.now)
        dataEmissao = models.DateTimeField('Data emissão',default=timezone.now)
        valorItulo = models.CharField('Valor Titulo',max_length=14, null=False)
        numeroDocumento = models.CharField('Numero Documento',max_length=20, null=False)
        empresas = models.ForeignKey(Empresa, on_delete=models.CASCADE)
        fornecedores = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

        def __str__(self):
            return self.numeroDocumento

class BaixasPagar(models.Model):
        banco = models.CharField('Banco',max_length=1, null=False)
        disponibilidade = models.CharField('Disponibilidade',max_length=12, null=False)
        dataBaixa = models.DateTimeField('Data Baixa',default=timezone.now)
        valorPago = models.DecimalField(max_digits=8, decimal_places=2)
        residual = models.CharField('Residual',max_length=14, null=False)
        formasPagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
        lancamentosPagar = models.ForeignKey(LancamentoPagar, on_delete=models.CASCADE)

        def __str__(self):
            return self.banco

class BaixasReceber(models.Model):
        banco = models.CharField('Banco',max_length=1, null=False)
        disponibilidade = models.CharField('Disponibilidade',max_length=12, null=False)
        dataBaixa = models.DateTimeField('Data Baixa',default=timezone.now)
        valorPago = models.DecimalField(max_digits=8, decimal_places=2)
        residual = models.CharField('Residual',max_length=14, null=False)
        formasPagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
        lancamentosReceber = models.ForeignKey(LancamentoReceber, on_delete=models.CASCADE)

        def __str__(self):
            return self.banco

class Tesouraria(models.Model):
       valor = models.CharField('Valor',max_length=14, null=False)
       numero = models.CharField('Numero',max_length=14, null=False)
       dataEmissao = models.DateTimeField('Data emissão',default=timezone.now)
       dataVencimento = models.DateTimeField('Data Vencimento',default=timezone.now)
       datadisponibilidade = models.DateTimeField('Data Vencimento',default=timezone.now)
       empresas = models.ForeignKey(Empresa, on_delete=models.CASCADE)
       fornecedores = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
       formaspagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
       clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE)
       planodecontas = models.ForeignKey(PlanodeConta, on_delete=models.CASCADE)

       def __str__(self):
           return self.numero
