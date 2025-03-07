# 🩺 Sistema de Controle de Prontuários Médicos via Leitura de Código de Barras

## 📢 Descrição
Este projeto tem como objetivo desenvolver um sistema eficiente para consulta e controle de prontuários médicos através da leitura de códigos de barras. A solução busca otimizar o tempo de acesso às informações, reduzir falhas humanas e garantir a segurança e conformidade com a **LGPD**.

O sistema é composto por:
- **Front-end:** Desenvolvido com React.js e Tailwind CSS.
- **Back-end:** API construída com Node.js e Express.
- **Banco de Dados:** PostgreSQL para armazenar dados dos prontuários e conectores com Supabase.
- **Leitura de Código de Barras:** Utilizando a biblioteca QuaggaJS.

---

## 🚀 Funcionalidades
✅ Login e autenticação de usuários.  
✅ Consulta de prontuários via leitura de código de barras.  
✅ Histórico de acessos com data e horário.  
✅ Interface amigável e responsiva.  
✅ Conformidade com normas de segurança e LGPD.  

---

## 🛠️ Tecnologias Utilizadas
- **Front-end:** React.js, Tailwind CSS, QuaggaJS  
- **Back-end:** Node.js, Express  
- **Banco de Dados:** PostgreSQL  
- **Gerenciamento de Pacotes:** npm  
- **Versionamento:** Git e GitHub  
- **Documentação:** Markdown e ABNT (via Overleaf)  

---

## 🗂️ Estrutura do Projeto
Sistema-de-Controle-Prontuarios/
├── backend/
│   ├── server.js                # Servidor Node.js com rotas de consulta
│   ├── .env                     # Variáveis de ambiente (credenciais do banco)
│   └── package.json             # Gerenciador de dependências do back-end
│
├── frontend/
│   ├── public/
│   │   └── index.html           # Página base do React
│   ├── src/
│   │   ├── components/
│   │   │   ├── BarcodeScanner.js # Componente para leitura de código de barras
│   │   │   └── Prontuario.js     # Exibição das informações do paciente
│   │   ├── App.js               # Arquivo principal da aplicação
│   │   └── styles.css           # Estilização com Tailwind CSS
│   └── package.json             # Gerenciador de dependências do front-end
│
├── README.md                    # Documentação do projeto
├── .gitignore                   # Arquivos ignorados pelo Git
└── database/
    ├── init.sql                 # Scripts de criação e popularização do banco
    └── README.md                # Instruções sobre o banco de dados

---



---

# 🚧 **Como Executar o Projeto (após clonar o repositório)**

### **1️⃣ Criar e Ativar o Ambiente Virtual**
```sh
python -m venv venv       # Cria o ambiente virtual
```
- **No Windows (PowerShell)**:
  ```sh
  venv\Scripts\Activate
  ```
- **No Windows (CMD)**:
  ```sh
  venv\Scripts\activate.bat
  ```
- **No Linux/Mac**:
  ```sh
  source venv/bin/activate
  ```

---

### **2️⃣ Instalar as Dependências**
```sh
pip install -r requirements.txt  # Instala as bibliotecas necessárias
```

---

### **3️⃣ Aplicar as Migrações do Banco**
```sh
python manage.py migrate  # Configura as tabelas no banco de dados
```

---

### **4️⃣ Criar um Superusuário para o Django Admin**
```sh
python manage.py createsuperuser  # Opcional, caso queira acessar o Django Admin
```
- Insira um **nome de usuário, e-mail e senha**.

---

### **5️⃣ Iniciar o Servidor Local**
```sh
python manage.py runserver
```
- O servidor estará disponível em **http://127.0.0.1:8000/**.

---

## 🔄 **Pré-requisitos**
✅ **Obrigatórios:**
- **Python** instalado ([Baixar aqui](https://www.python.org/downloads/))
- **PostgreSQL** instalado ([Baixar aqui](https://www.postgresql.org/))  

✅ **Recomendados (opcionais, mas úteis):**
- **Git** (para clonar o projeto) → [Baixar aqui](https://git-scm.com/)
- **Node.js** (*se houver integração com o frontend React*) → [Baixar aqui](https://nodejs.org/)

---

**📌 Observações:**
- O **banco de dados já está configurado no Supabase**, então não precisa configurar manualmente o PostgreSQL.  
- Se houver **erros de dependências**, rode:
  ```sh
  pip install --upgrade pip
  pip install -r requirements.txt
  ```
- Se precisar **parar o servidor**, pressione **CTRL + C** no terminal.

Agora seu projeto Django estará rodando corretamente! 🚀

#### 1️⃣ Clone o repositório:
```bash
git clone https://github.com/seu-usuario/sistema-prontuarios.git
cd sistema-prontuarios
