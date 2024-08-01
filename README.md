# Sistema para Gestão de Passeios e Pacotes Turísticos

## Escopo

O propósito deste projeto é desenvolver um sistema para cadastro e administração de atividades de turismo. Consiste no cadastro e login para empresas do ramo turístico e afins, bem como o registro de seus respectivos agentes para administrar a gestão de passeios e pacotes turísticos. O projeto utiliza o framework Django 4.0 e a linguagem de programação Python 3.9.5.

## Estrutura

### Models

- **User**
  - Campos: `id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `is_staff`, `is_active`, `date_joined`, `email`, `option`

- **Company**
  - Campos: `id`, `company_name`, `document_number`, `document_image`, `street`, `number`, `complement`, `postal_code`, `city`, `state`, `user_id`

- **Contact**
  - Campos: `id`, `cell_phone`, `user_id`

- **SocialMedia**
  - Campos: `id`, `social_media`, `user_id`

## Funcionalidades

### Cadastro

- **Tela de Cadastro**
  - Opções: Agência ou Fornecedor
  - Campos: Nome de usuário, email, senha, confirmar senha
  - Botões: Salvar cadastro, link para tela de login

- **Tela de Completar Cadastro**
  - Campos: Razão social, CNPJ, logradouro, número, complemento, cidade, estado, CEP
  - Botões: Upload de imagem, salvar cadastro
  - Após cadastro, o usuário será automaticamente logado

### Login

- **Tela de Login**
  - Campos: Usuário/email, senha
  - Botões: Acessar, link para recuperar senha, link para tela de cadastro

### Configurações

- **Username/Email**
  - O usuário pode editar os campos Usuário e Email

- **Empresa**
  - O usuário pode editar os campos Razão social, CNPJ, Logradouro, Número, Complemento, Cidade, Estado, CEP, e fazer upload de uma imagem

### Administrador

- **Gestão de Usuários**
  - Listar usuários com opções de entrada por página, campo de pesquisa, paginador, ícone para editar dados do usuário
  - Opção para ativar/inativar usuário

- **Gestão de Empresas**
  - Listar empresas com opções de entrada por página, campo de pesquisa, paginador, ícone para editar dados da empresa

  > Estas opções estão disponíveis apenas para usuários administradores

### Logout

- **Opção Sair**
  - O usuário pode clicar no botão 'sair' para confirmar o logout

## Instruções de Instalação

1. Instalar e atualizar pip:
    ```bash
    pip install
    python -m pip install --upgrade pip
    ```

2. Criar e acessar a pasta do projeto:
    ```bash
    mkdir tourproject
    cd tourproject
    ```

3. Criar ambiente virtual:
    ```bash
    python -m venv venv_tourproject
    ```

4. Ativar ambiente virtual:
    - **Windows**:
        ```bash
        venv_tourproject\scripts\activate.bat
        ```
    - **Linux**:
        ```bash
        source venv_tourproject/bin/activate
        ```

5. Clonar o projeto:
    ```bash
    git init
    git clone https://github.com/carlosalbertoprojetos/tourproject.git
    ```

6. Acessar a pasta do projeto:
    ```bash
    cd tourproject
    ```

7. Instalar dependências:
    ```bash
    pip install -r requirements.txt
    ```

8. Aplicar migrações:
    ```bash
    python manage.py migrate
    ```

9. Criar super usuário:
    ```bash
    python manage.py createsuperuser
    ```
    > Obs.: O email será utilizado como username para login

10. Rodar o projeto:
    ```bash
    python manage.py runserver
    ```
