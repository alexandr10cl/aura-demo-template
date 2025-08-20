# 🚀 Template Base

Template base para desenvolvimento de aplicações web com Flask, configurado para deploy no Vercel com integração OpenAI.

## 📋 Características

- **Framework**: Flask 3.1.1
- **Deploy**: Configurado para Vercel
- **IA**: Integração com OpenAI GPT
- **Frontend**: HTML5, CSS3 (com variáveis CSS), JavaScript
- **Arquitetura**: Modular com Blueprints
- **Gerenciamento de Dados**: Sistema em memória (DataManager)

## 🏗️ Estrutura do Projeto

```
aura-demo-template/
├── index.py                 # Arquivo principal da aplicação
├── requirements.txt         # Dependências Python
├── vercel.json             # Configuração do Vercel
├── views/                  # Blueprints e rotas
│   ├── __init__.py
│   └── index.py           # Rota principal
├── services/              # Serviços e integrações
│   ├── data_manager.py    # Gerenciador de dados em memória
│   └── openai_service.py  # Cliente OpenAI
├── templates/             # Templates Jinja2
│   ├── base.html         # Template base
│   ├── index.html        # Página inicial
│   ├── navbar-demo.html  # Demo de navbar
│   └── sidebar-demo.html # Demo de sidebar
├── static/               # Arquivos estáticos
│   ├── css/
│   │   ├── style.css      # Estilos principais
│   │   ├── components.css # Estilos de componentes
│   │   └── variables.css  # Variáveis CSS
│   └── js/               # Diretório JavaScript (vazio)
└── utils/                # Utilitários
    └── __init__.py
```

## 🚀 Instalação e Configuração

### 1. Clone o projeto

### 2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
- `FLASK_SECRET_KEY`: Chave secreta do Flask
- `OPENAI_API_KEY`: Sua chave da API da OpenAI

### 5. Execute localmente
```bash
python index.py
```

## 🌐 Deploy no Vercel

### Pré-requisitos
- Conta no [Vercel](https://vercel.com)
- Vercel CLI instalado: `npm i -g vercel`

### Processo de Deploy
1. **Via Vercel CLI:**
   ```bash
   vercel
   ```

2. **Via GitHub:**
   - Conecte seu repositório no dashboard do Vercel
   - Configure as variáveis de ambiente no painel do Vercel

### Variáveis de Ambiente no Vercel
Configure as seguintes variáveis no dashboard do Vercel:
- `FLASK_SECRET_KEY`
- `OPENAI_API_KEY`


## 📁 Arquivos de Configuração

### requirements.txt
Lista das dependências Python necessárias.

### vercel.json
Configuração para deploy no Vercel:
- Define o ponto de entrada (`index.py`)
- Configura as rotas para direcionamento

