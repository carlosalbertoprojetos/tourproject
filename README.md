# SISTEMA DE TURISMO

## Escopo
Desenvolver um sistema de cadastro e login para diferentes tipos de usuários (agência/agente, parceiro e cliente), utilizando o framework Django VERSÃO e a linguagem de programação Python VERSÃO.

# Estrutura

* models
    - User - email, opção
        * Tipos de usuários:
			- Agência - nome da agência, outras informações
            	* Agente - nome, nome da agência, outras informações
				* Cliente - nome, outras informações
				* Parceiro - nome, documento, nome da empresa, outras informações
		* Demais dados:
			- Documento - CNPJ/CPF
			- Endereço - logradouro, numero, complemento, bairro, cidade, estado, CEP
			- Telefone - telefone
			- Rede social - rede social

# Funcionalidades

* cadastro:
	- o usuário serleciona uma entre as opções Cliente, Agência ou parceiro, insere usuario, email, senha e confirmar senha
	- concluído o cadastro, o usuário será automaticamente logado
* login:
	- o usuário insere username/email e senha
	- o template possui link para recuperação de senha e cadastrar
* logout:
	- o usuário optar por clicar no botão 'sair' para confirmar logout.

* perfil de usuários:
	- tela para exibir
	- formulário para editar


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
mkdir projetotour
cd projetotour
```


### Criar ambiente virtual

```
py -m venv venv_projetotour
```


### Ativar ambiente virtual

```
- Windows -
venv_projetotour/scripts/activate.bat

- Linux -
venv_projetotour\bin\activate
```


### Clonar o projeto

```
git clone https://github.com/carlosalbertoprojetos/tourproject.git
```


### Acessar a pasta do projeto

```
cd projetotour

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
