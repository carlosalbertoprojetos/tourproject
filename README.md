# travel-agency-platform

## Sistema de Gestão de Passeios e Pacotes Turísticos

Aplicação web desenvolvida com **Django** para gerenciamento de **empresas do setor turístico**, permitindo o cadastro e administração de **agências, fornecedores e seus respectivos agentes** responsáveis pela gestão de **passeios e pacotes turísticos**.

O sistema fornece uma base para plataformas de turismo que necessitam de **registro de empresas, autenticação de usuários e gestão administrativa**.

---

# Visão Geral

O **TourProject** foi desenvolvido utilizando **Python 3.9.5** e **Django 4.0**, com o objetivo de fornecer uma solução inicial para **gestão de empresas do setor turístico**.

A aplicação permite que empresas se registrem na plataforma, completem seus dados institucionais e utilizem o sistema para administrar suas operações. Administradores possuem acesso a ferramentas adicionais para gerenciar usuários e empresas cadastradas.

---

# Funcionalidades

## Cadastro de Usuários

* Registro de novos usuários
* Escolha do tipo de conta:

  * Agência
  * Fornecedor
* Autenticação utilizando **email ou username**
* Login automático após conclusão do cadastro

Campos de cadastro:

* Nome de usuário
* Email
* Senha
* Confirmação de senha

---

## Completar Cadastro da Empresa

Após o cadastro inicial, o usuário pode complementar os dados da empresa:

* Razão social
* CNPJ
* Endereço completo

  * Logradouro
  * Número
  * Complemento
  * Cidade
  * Estado
  * CEP
* Upload de imagem do documento da empresa

---

## Autenticação

* Login com **usuário ou email**
* Logout seguro
* Recuperação de senha

---

## Configurações da Conta

Usuários autenticados podem atualizar informações pessoais e empresariais.

### Dados do Usuário

* Alterar username
* Alterar email

### Dados da Empresa

* Editar razão social
* Editar CNPJ
* Atualizar endereço
* Atualizar imagem/documento da empresa

---

## Área Administrativa

Funcionalidades disponíveis apenas para **usuários administradores**.

### Gestão de Usuários

* Listagem de usuários cadastrados
* Paginação de resultados
* Campo de pesquisa
* Edição de dados de usuários
* Ativação ou desativação de contas

### Gestão de Empresas

* Listagem de empresas cadastradas
* Paginação de resultados
* Campo de pesquisa
* Edição de dados da empresa

---

# Modelos do Sistema

## User

Modelo responsável pela autenticação dos usuários.

Campos principais:

* id
* username
* email
* password
* first_name
* last_name
* is_superuser
* is_staff
* is_active
* last_login
* date_joined
* option (tipo de usuário)

---

## Company

Representa as empresas cadastradas no sistema.

Campos:

* id
* company_name
* document_number (CNPJ)
* document_image
* street
* number
* complement
* postal_code
* city
* state
* user_id

---

## Contact

Armazena informações de contato dos usuários.

Campos:

* id
* cell_phone
* user_id

---

## SocialMedia

Armazena redes sociais associadas ao usuário.

Campos:

* id
* social_media
* user_id

---

# Tecnologias Utilizadas

## Backend

* Python 3.9.5
* Django 4.0

## Frontend

* HTML
* CSS
* JavaScript

## Banco de Dados

* SQLite (padrão do Django)

---

# Estrutura do Projeto

```id="ojsgq4"
tourproject/
│
├── manage.py
├── requirements.txt
│
├── tourproject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── apps/
│
├── templates/
│
└── static/
```

---

# Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento.

---

## 1. Atualizar o pip

```bash id="o6tdal"
python -m pip install --upgrade pip
```

---

## 2. Criar pasta do projeto

```bash id="3hpgbo"
mkdir tourproject
cd tourproject
```

---

## 3. Criar ambiente virtual

```bash id="wqvsh5"
python -m venv venv_tourproject
```

---

## 4. Ativar ambiente virtual

### Windows

```bash id="nmumzd"
venv_tourproject\scripts\activate
```

### Linux / Mac

```bash id="3cclu3"
source venv_tourproject/bin/activate
```

---

## 5. Clonar o repositório

```bash id="5f4qwo"
git clone https://github.com/carlosalbertoprojetos/tourproject.git
```

---

## 6. Acessar a pasta do projeto

```bash id="zqtqii"
cd tourproject
```

---

## 7. Instalar dependências

```bash id="v8ld9c"
pip install -r requirements.txt
```

---

# Configuração do Banco de Dados

Aplicar migrações:

```bash id="c8oqc9"
python manage.py migrate
```

---

# Criar Usuário Administrador

```bash id="y9goxh"
python manage.py createsuperuser
```

Observação:

O **email será utilizado como identificador principal para login**.

---

# Executar a Aplicação

```bash id="05suzs"
python manage.py runserver
```

A aplicação estará disponível em:

```id="2l3n4n"
http://127.0.0.1:8000
```

---

# Possíveis Melhorias

* Implementação de **API REST com Django REST Framework**
* Sistema de **gestão de pacotes turísticos**
* Integração com **gateways de pagamento**
* Sistema de **reservas online**
* Dashboard analítico para empresas
* Dockerização da aplicação

---

# Autor

**Carlos Alberto Medeiros**

GitHub
https://github.com/carlosalbertoprojetos

