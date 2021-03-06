# Generated by Django 2.0.9 on 2018-10-10 15:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaixasPagar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(max_length=1, verbose_name='Banco')),
                ('disponibilidade', models.CharField(max_length=12, verbose_name='Disponibilidade')),
                ('dataBaixa', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Baixa')),
                ('valorPago', models.DecimalField(decimal_places=2, max_digits=8)),
                ('residual', models.CharField(max_length=14, verbose_name='Residual')),
            ],
        ),
        migrations.CreateModel(
            name='BaixasReceber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(max_length=1, verbose_name='Banco')),
                ('disponibilidade', models.CharField(max_length=12, verbose_name='Disponibilidade')),
                ('dataBaixa', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Baixa')),
                ('valorPago', models.DecimalField(decimal_places=2, max_digits=8)),
                ('residual', models.CharField(max_length=14, verbose_name='Residual')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razaosocial', models.CharField(max_length=50, verbose_name='Razão Social')),
                ('identificacao', models.CharField(max_length=50, verbose_name='Identificacao')),
                ('classificacao', models.CharField(max_length=50, verbose_name='Classificação')),
                ('tipoPessoa', models.CharField(choices=[('FISICA', 'Fisica'), ('JURIDICA', 'Juridica')], default='Tipo Pessoa', max_length=10, verbose_name='Tipo Pessoa')),
                ('cnpjCpf', models.CharField(max_length=15, verbose_name='CNPJ/CPF')),
                ('inscricaoEstadual', models.CharField(max_length=20, verbose_name='Inscrição Estadual')),
                ('inscricaoMunicipal', models.CharField(max_length=20, verbose_name='Inscrição Municipal')),
                ('endereco', models.CharField(max_length=50, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('municipio', models.CharField(max_length=50, verbose_name='Municipio')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='UF', max_length=2, verbose_name='UF')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('nomeTitular', models.CharField(max_length=50, verbose_name='Nome Titular')),
                ('cpf', models.CharField(max_length=15, verbose_name='CPF')),
                ('funcao', models.CharField(max_length=50, verbose_name='Funcao')),
            ],
        ),
        migrations.CreateModel(
            name='ContaBancaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classificacao', models.CharField(max_length=18, verbose_name='Classificação')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('numeroConta', models.CharField(max_length=20, verbose_name='Numero Conta')),
                ('numeroAgencia', models.CharField(max_length=20, verbose_name='Numero Agencia')),
                ('dataSaldoInicial', models.CharField(max_length=12, verbose_name='Data Saldo Inicial')),
                ('saldoInicial', models.CharField(max_length=12, verbose_name='Saldo Inicial')),
                ('caixa', models.CharField(max_length=1, verbose_name='Caixa')),
                ('banco', models.CharField(max_length=1, verbose_name='Banco')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razaosocial', models.CharField(max_length=50, verbose_name='Razão Social')),
                ('identificacao', models.CharField(max_length=50, verbose_name='Identificacao')),
                ('cnpj', models.CharField(max_length=15, verbose_name='CNPJ')),
                ('tipoPessoa', models.CharField(choices=[('FISICA', 'Fisica'), ('JURIDICA', 'Juridica')], default='Tipo Pessoa', max_length=10, verbose_name='Tipo Pessoa')),
                ('inscricaoEstadual', models.CharField(max_length=20, verbose_name='Inscrição Estadual')),
                ('inscricaoMunicipal', models.CharField(max_length=20, verbose_name='Inscrição Municipal')),
                ('endereco', models.CharField(max_length=50, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('municipio', models.CharField(max_length=50, verbose_name='Municipio')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='UF', max_length=2, verbose_name='UF')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('nomeTitular', models.CharField(max_length=50, verbose_name='Nome Titular')),
                ('cpf', models.CharField(max_length=15, verbose_name='CPF')),
                ('funcao', models.CharField(max_length=50, verbose_name='Funcao')),
            ],
        ),
        migrations.CreateModel(
            name='FormaPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razaosocial', models.CharField(max_length=50, verbose_name='Razão Social')),
                ('identificacao', models.CharField(max_length=50, verbose_name='Identificacao')),
                ('classificacao', models.CharField(max_length=50, verbose_name='Classificação')),
                ('tipoPessoa', models.CharField(choices=[('FISICA', 'Fisica'), ('JURIDICA', 'Juridica')], default='Tipo Pessoa', max_length=10, verbose_name='Tipo Pessoa')),
                ('cnpjCpf', models.CharField(max_length=15, verbose_name='CNPJ/CPF')),
                ('inscricaoEstadual', models.CharField(max_length=20, verbose_name='Inscrição Estadual')),
                ('inscricaoMunicipal', models.CharField(max_length=20, verbose_name='Inscrição Municipal')),
                ('endereco', models.CharField(max_length=50, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('municipio', models.CharField(max_length=50, verbose_name='Municipio')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='UF', max_length=2, verbose_name='UF')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('nomeTitular', models.CharField(max_length=50, verbose_name='Nome Titular')),
                ('cpf', models.CharField(max_length=15, verbose_name='CPF')),
                ('funcao', models.CharField(max_length=50, verbose_name='Funcao')),
            ],
        ),
        migrations.CreateModel(
            name='LancamentoPagar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataVencimento', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Vencimento')),
                ('dataEmissao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data emissão')),
                ('valorItulo', models.CharField(max_length=14, verbose_name='Valor Titulo')),
                ('numeroDocumento', models.CharField(max_length=20, verbose_name='Numero Documento')),
                ('empresas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Empresa')),
                ('fornecedores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Fornecedor')),
            ],
        ),
        migrations.CreateModel(
            name='LancamentoReceber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataVencimento', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Vencimento')),
                ('dataEmissao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data emissão')),
                ('valorItulo', models.CharField(max_length=14, verbose_name='Valor Titulo')),
                ('numeroDocumento', models.CharField(max_length=20, verbose_name='Numero Documento')),
                ('clientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Cliente')),
                ('empresas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='PlanodeConta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classificacao', models.CharField(max_length=18, verbose_name='Classificação')),
                ('tipoConta', models.CharField(choices=[('Titulo', 'Titulo')], default='Tipo Conta', max_length=15)),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('caixa', models.CharField(max_length=1, verbose_name='Caixa')),
                ('banco', models.CharField(max_length=1, verbose_name='Banco')),
                ('fornecedor', models.CharField(max_length=1)),
                ('entradaRecurso', models.CharField(max_length=1)),
                ('saidaRecurso', models.CharField(max_length=1)),
                ('contas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.ContaBancaria')),
            ],
        ),
        migrations.CreateModel(
            name='Tesouraria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=14, verbose_name='Valor')),
                ('numero', models.CharField(max_length=14, verbose_name='Numero')),
                ('dataEmissao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data emissão')),
                ('dataVencimento', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Vencimento')),
                ('datadisponibilidade', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Vencimento')),
                ('clientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Cliente')),
                ('empresas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Empresa')),
                ('formaspagamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.FormaPagamento')),
                ('fornecedores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Fornecedor')),
                ('planodecontas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.PlanodeConta')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=255, verbose_name='Usuario')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('senha', models.CharField(max_length=50, verbose_name='Senha')),
                ('confirmesenha', models.CharField(max_length=50, verbose_name='ConfirmarSenha')),
            ],
        ),
        migrations.AddField(
            model_name='baixasreceber',
            name='formasPagamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.FormaPagamento'),
        ),
        migrations.AddField(
            model_name='baixasreceber',
            name='lancamentosReceber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.LancamentoReceber'),
        ),
        migrations.AddField(
            model_name='baixaspagar',
            name='formasPagamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.FormaPagamento'),
        ),
        migrations.AddField(
            model_name='baixaspagar',
            name='lancamentosPagar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.LancamentoPagar'),
        ),
    ]
