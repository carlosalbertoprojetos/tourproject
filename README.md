# Sistema de Gestão de Passeios e Pacotes Turísticos

## Descrição
Este sistema foi criado para facilitar o cadastro e gerenciamento de empresas de turismo, seus agentes, passeios e pacotes turísticos. Utilizando o Django 4.0, permite a criação de usuários, empresas e a administração de informações relacionadas ao setor de turismo.

## Funcionalidades
### Usuários
- Cadastro de agentes e administradores.
- Login com opções de recuperação de senha.
- Edição de perfil.

### Empresas
- Cadastro e gestão de empresas turísticas.
- Edição de informações empresariais e envio de documentos.

### Administração
- Gestão de usuários e empresas (apenas para administradores).
- Ativação/Inativação de usuários.

### Passeios e Pacotes
- Cadastro e controle de pacotes turísticos e passeios.
  
## Estrutura de Dados
### Models
- **User:** Campos relacionados a usuários como nome, email, permissões.
- **Company:** Informações empresariais (nome, CNPJ, endereço, etc.).
- **Contact:** Informações de contato.
- **SocialMedia:** Links para redes sociais da empresa.

## Como Rodar o Projeto

### 1. Pré-requisitos
- Python 3.9.5+
- pip

### 2. Instalação

#### a) Criar ambiente virtual
```bash
python -m venv venv_tourproject
```

#### b) Ativar ambiente virtual
- **Windows:**
  ```bash
  venv_tourproject\Scripts\activate.bat
  ```
- **Linux:**
  ```bash
  source venv_tourproject/bin/activate
  ```

#### c) Clonar o repositório
```bash
git clone https://github.com/carlosalbertoprojetos/tourproject.git
cd tourproject
```

#### d) Instalar dependências
```bash
pip install -r requirements.txt
```

#### e) Aplicar migrações
```bash
python manage.py migrate
```

#### f) Criar superusuário
```bash
python manage.py createsuperuser
```

#### g) Rodar o servidor local
```bash
python manage.py runserver
```

## Deployment
Este projeto também pode ser implantado usando plataformas como o Vercel.

## Contribuições
Contribuições são bem-vindas! Siga as práticas de código limpo e abra um pull request.
