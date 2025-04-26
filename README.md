🥖 Sistema de Gestão e Análise de Pedidos - Projeto Capstone


✨ Descrição
Este projeto simula a gestão e análise de pedidos de uma padaria, integrando práticas de backend com Django, persistência com PostgreSQL e análise de dados com Python.
Além de estruturar o cadastro e controle de produtos e pedidos, foi implementada uma rotina de análise e visualização dos dados utilizando Pandas e Matplotlib.

O projeto foi desenvolvido como forma prática de consolidar os conhecimentos adquiridos nas certificações de Data Science e Artificial Intelligence da IBM.

⚙️ Tecnologias Utilizadas
Python 3.x

Django: Para criação da API e gerenciamento dos dados no backend.

PostgreSQL: Banco de dados para armazenamento dos registros de pedidos e produtos.

Pandas: Para leitura e transformação dos dados extraídos do banco.

Matplotlib: Para geração de gráficos de vendas e análise de produtos mais vendidos.

🔧 Instalação
Antes de rodar o projeto, instale as dependências necessárias:

bash
```
pip install django psycopg2-binary pandas matplotlib sqlalchemy
```

🎮 Como Rodar o Projeto
Configure o banco de dados PostgreSQL no arquivo settings.py do Django:

python
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'smart_place',
        'USER': 'postgres',
        'PASSWORD': 'sua_senha',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
Crie as tabelas no banco:

bash
```
python manage.py makemigrations
python manage.py migrate
```
Inicie o servidor Django:

bash
```
python manage.py runserver
```
Execute o script de análise de dados:

bash
```
python analise.py
```

Este script conecta ao banco de dados, extrai as informações dos pedidos e gera gráficos de vendas por produto.

📊 Exemplo de Uso
Cadastro de produtos e pedidos pelo Admin do Django.

Extração de vendas totais por produto.

Geração de gráfico de barras dos produtos mais vendidos.

Exemplo de gráfico gerado:

Produtos mais vendidos na padaria (baseado nos dados dos pedidos).

