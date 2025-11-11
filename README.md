# 🔐 Sistema de Login em Django – Engenharia de Software

## 🧩 **Descrição do Projeto**

Este projeto foi desenvolvido como parte da disciplina **Engenharia de Software**, simulando um ambiente ágil de desenvolvimento.  
O sistema implementa um **CRUD de login completo** utilizando o framework **Django**, permitindo o gerenciamento de usuários, autenticação e recuperação de senha.

Além da parte técnica, o repositório foi estruturado com:
- **Commits semânticos e frequentes** (mínimo de 10);
- **Quadro Kanban** no GitHub Projects;
- **Pipeline de integração contínua (CI)** com **GitHub Actions**;
- **Simulação de mudança de escopo** com adição da funcionalidade “Recuperar Senha”.

---

## 🚀 **Funcionalidades**
✅ Cadastro de usuários (Create)  
✅ Login de usuário (Read/Login)  
✅ Edição de perfil (Update)  
✅ Exclusão de usuário (Delete)  
✅ Logout seguro  
✅ Recuperação de senha por e-mail (mudança de escopo)  
✅ Testes automatizados  
✅ CI configurado com GitHub Actions  

---

## 🧠 **Tecnologias Utilizadas**
- Python 3.11+
- Django 5.x
- SQLite (banco padrão)
- HTML + CSS
- Pytest / Django TestCase
- GitHub Actions (para testes automáticos)

---

## ⚙️ **Instalação e Execução**

### 1️⃣ Clone o repositório:

```bash
git clone https://github.com/seu-usuario/sistema-login-django.git
cd sistema-login-django
```

### 2️⃣ Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # (Linux/macOS)
venv\Scripts\activate     # (Windows)
```

### 3️⃣ Instale as dependências:

```bash
pip install django pytest
```

### 4️⃣ Execute as migrações:

```bash
python manage.py migrate
```

### 5️⃣ Inicie o servidor:

```bash
python manage.py runserver

Acesse em: http://127.0.0.1:8000/
```

---

## 🧾 Estrutura do Projeto

```
login_project/
├── manage.py
├── login_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── accounts/
    ├── migrations/
    ├── templates/accounts/
    │   ├── base.html
    │   ├── login.html
    │   ├── register.html
    │   ├── profile.html
    │   ├── password_reset.html
    │   ├── password_reset_done.html
    │   ├── password_reset_confirm.html
    │   └── password_reset_complete.html
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── tests.py
.github/
└── workflows/
    └── tests.yml
```

## 🧩 Histórico de Commits

| Nº  | Tipo  | Mensagem                                                            |
| --- | ----- | ------------------------------------------------------------------- |
| 1️⃣ | feat  | cria estrutura inicial do projeto Django                            |
| 2️⃣ | feat  | adiciona app accounts para gerenciamento de usuários                |
| 3️⃣ | chore | registra app e configura templates                                  |
| 4️⃣ | feat  | implementa rotas principais e URLs do app                           |
| 5️⃣ | feat  | cria formulários de login e cadastro                                |
| 6️⃣ | feat  | implementa views de login, logout e registro                        |
| 7️⃣ | feat  | adiciona templates base, login e cadastro                           |
| 8️⃣ | test  | adiciona teste automatizado de criação de usuário                   |
| 9️⃣ | ci    | configura GitHub Actions para testes automatizados                  |
| 🔟  | feat  | adiciona funcionalidade de recuperação de senha (mudança de escopo) |

---

## 🔄 Metodologia Ágil (Kanban)

O desenvolvimento foi gerenciado através de um quadro Kanban no GitHub Projects com as seguintes colunas:

| A Fazer              | Em Progresso      | Concluído                  |
| -------------------- | ----------------- | -------------------------- |
| Criar projeto Django | Implementar views | Sistema funcional          |
| Criar app `accounts` | Criar templates   | CI configurado             |
| Configurar rotas     | Adicionar testes  | Mudança de escopo aplicada |

A cada etapa concluída, as tarefas foram movidas para a coluna Concluído, simulando o fluxo ágil de desenvolvimento.

---

## 🔄 Mudança de Escopo – Recuperar Senha

Durante o desenvolvimento, foi adicionada a funcionalidade Recuperar Senha, permitindo que o usuário redefina sua senha via e-mail.

Motivo:
Usuários poderiam esquecer suas credenciais, tornando a aplicação menos acessível.

Implementação:

 -Novas rotas adicionadas no urls.py;

 -Templates password_reset*.html criados;

 -Configuração de EMAIL_BACKEND no settings.py;

 -Novo commit registrado com mensagem:
    ```java
    feat: adiciona funcionalidade de recuperação de senha (mudança de escopo)
    ```

---

## 🧪 Testes Automatizados

Arquivo: `accounts/tests.py`
```python
    from django.test import TestCase
from django.contrib.auth.models import User

class UserTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='teste', password='1234')
        self.assertEqual(user.username, 'teste')
        self.assertTrue(user.check_password('1234'))
```

Para rodar:
    ```bash
    python manage.py test
    ```

---

## ⚙️ Pipeline CI (GitHub Actions)

Arquivo: `.github/workflows/tests.yml`

```yaml
    name: Django Tests

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install django pytest
      - name: Run migrations
        run: python manage.py migrate
      - name: Run tests
        run: python manage.py test
```

### 🔍 Função:

O pipeline instala dependências, aplica migrações e executa os testes automaticamente a cada push no repositório.

---

### 👨‍💻 Autor

Arthur Lima Pereira

Disciplina: Engenharia de Software

RA: 133275