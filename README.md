# Projeto PVP 

<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</p>


## Descrição do projeto
Este projeto é um desafio para um teste prático, que é reponsável de exibir produtos na linha de produção e suas mudanças de setores de acordo com o procedimento, para o contrução deste projeto foi utilizado [Django](https://www.djangoproject.com/).

## Como rodar o projeto?

No projeto foi utilizado o [Python 3.10.0](https://www.python.org/downloads/)

Com o Python já instalado 

Precisamos ativar o ambiente virtual do python usando esse comando:

```sh
python -m venv venv
```

Depois precisamos adicionar as dependências

No Windows, execute:

```sh
python -m venv env
venv\Scripts\activate.bat
pip install -r requirements.txt
```

No Linux ou no MacOS, execute:
```sh
python -m venv env
source venv/bin/activate
pip install -r requirements.txt
```

Depois de restaurar o banco, precisamos rodar as migrações e mapear o banco:

```sh
python manage.py makemigrations                                 
python manage.py migrate
 ```






Depois podemos rodar o projeto
```sh
python manage.py runserver
```