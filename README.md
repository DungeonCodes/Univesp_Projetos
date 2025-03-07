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

## 🚧 Como Executar o Projeto

### 🔄 Pré-requisitos
- Node.js instalado ([Baixar aqui](https://nodejs.org/))
- PostgreSQL instalado ([Baixar aqui](https://www.postgresql.org/))
- Git (para clonar o projeto, opcional mas recomendado)

### 📥 Passo a Passo

#### 1️⃣ Clone o repositório:
```bash
git clone https://github.com/seu-usuario/sistema-prontuarios.git
cd sistema-prontuarios
