# SISTEMA DE TURISMO

## Escopo
Desenvolver um sistema de cadastro e login para diferentes tipos de usuários (agência/agente, parceiro e cliente), utilizando o framework Django VERSÃO e a linguagem de programação Python VERSÃO.

# Estrutura

* models
    - User - email, opção
        -> Agência - nome da agência, outras informações
            + Agente - nome, nome da agência, outras informações
        -> Cliente - nome, outras informações
        -> Parceiro - nome, documento, nome da empresa, outras informações
        -> Documento - CNPJ/CPF
        -> Endereço - logradouro, numero, complemento, bairro, cidade, estado, CEP
        -> Telefone - telefone
        -> Rede social - rede social

# Funcionalidades

* cadastro (email e senha):
	- com o cadastro concluído, será enviado link no email informado, para confirmar o cadastro;
	- o link direcionará para um formulário de conclusão de cadastro;
	- concluído o cadastro, o usuário será automaticamente logado.
* login (email e senha):
	- link para recuperação de senha.
	- formulário para informar email cadastrado para envio do link de recuperação de senha.
	- o link enviado redicionará para o formulário de renovação de senha.
* logout:
	- tela para confirmar logout.

* perfil de usuários:
	- tela para exibir
	- formulário para editar
	- tela para confirmar exclusão

* contato
	- formuláro para envio de mensagens ao administrador do framework;


## Instruções de nstalação

### Instalar e atualizar pip

```
pip install
python.exe -m pip install --upgrade pip
```


### Criar e acessar pasta do projeto

```
mkdir nome_projeto
cd nome_projeto
```


### Criar ambiente virtual

```
py -m venv venv_nome_projeto
```


### Ativar ambiente virtual

```
- Windows -
venv_nome_projeto/scripts/activate.bat

- Linux -
venv_nome_projeto\bin\activate
```


### Clonar o projeto

```
git clone 
```


### Acessar a pasta do projeto

```
cd cl_completo
```

### Instalar dependências

```
pip install -r requirements.txt
```


### Aplicar migrações

```
python manage.py migrate
```


### Criar super usuário

```
python manage.py createsuperuser
```

obs.: o email será utilizado como username para login


### Rodar o projeto

```
python manage.py runserver
```
