# 🤖 AI Agent Assistant

<div align="center">

**Sistema de IA para Automação Completa de Desenvolvimento**

[![Licença MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)](https://github.com/batista21batista-lab/ai-agent-assistant)

</div>

---

## 🎯 Sobre o Projeto

O **AI Agent Assistant** é um agente de IA completo que automatiza todo o ciclo de desenvolvimento de software, desde a geração de código até deploy em produção.

### ✨ Funcionalidades Principais

- ✅ **Geração de Código**: Cria código automaticamente usando IA
- 🧪 **Testes Automáticos**: Executa testes contínuos e validações
- 🚀 **Deploy Automático**: Publica em Netlify com um comando
- 📝 **Documentação**: Gera docs automaticamente
- 📈 **Monitoramento**: Dashboard com métricas em tempo real
- 🔧 **Integrações**: GitHub, Netlify, OpenAI, Google Sheets

---

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.8 ou superior
- Git
- Conta no GitHub
- Conta no Netlify (opcional)
- Chave da API OpenAI (opcional)

### Instalação

```bash
# 1. Clonar o repositório
git clone https://github.com/batista21batista-lab/ai-agent-assistant.git
cd ai-agent-assistant

# 2. Criar ambiente virtual
python -m venv venv

# 3. Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Instalar dependências
pip install -r requirements.txt

# 5. Configurar variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com seus tokens

# 6. Executar o agente
python src/main.py
```

---

## 📚 Documentação

- 📄 [Guia Rápido](docs/GUIA-RAPIDO.md) - Introdução e primeiros passos
- 🛠️ [Implementação Completa](docs/IMPLEMENTACAO-COMPLETA.md) - Guia detalhado
- 👥 [Tutorial para Iniciantes](docs/TUTORIAL-INICIANTES.md) - Passo-a-passo completo
- 💻 [Referência da API](docs/API-REFERENCE.md) - Documentação técnica

---

## 📁 Estrutura do Projeto

```
ai-agent-assistant/
├── src/                  # Código-fonte
│   ├── main.py          # Arquivo principal
│   ├── integrations/    # Integrações (GitHub, Netlify, etc)
│   ├── commands/        # Comandos do agente
│   └── utils/           # Utilitários
├── docs/                # Documentação
├── tests/               # Testes automatizados
├── workflows/           # Workflows N8N/Make
├── dashboard/           # Interface web
├── templates/           # Templates de prompts
├── .env.example         # Template de configurações
├── requirements.txt     # Dependências Python
└── README.md            # Este arquivo
```

---

## 🛠️ Configuração

### Obter Tokens Necessários

#### GitHub Token
1. Acesse https://github.com/settings/tokens
2. Clique em "Generate new token (classic)"
3. Selecione: `repo`, `workflow`, `write:packages`
4. Copie o token gerado

#### Netlify Token
1. Acesse https://app.netlify.com/user/applications
2. Clique em "New access token"
3. Copie o token gerado

#### OpenAI API Key
1. Acesse https://platform.openai.com/api-keys
2. Clique em "Create new secret key"
3. Copie a chave gerada

### Configurar `.env`

Edite o arquivo `.env` com seus tokens:

```bash
GITHUB_TOKEN=seu_token_aqui
NETLIFY_TOKEN=seu_token_aqui
OPENAI_API_KEY=seu_token_aqui
```

---

## 💻 Uso

### Comandos Básicos

```bash
# Executar o agente
python src/main.py

# Executar testes
pytest tests/

# Gerar documentação
mkdocs serve

# Fazer lint do código
black src/
flake8 src/
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga os passos:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

---

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👤 Autor

**batista21batista-lab**

- GitHub: [@batista21batista-lab](https://github.com/batista21batista-lab)
- Repositório: [ai-agent-assistant](https://github.com/batista21batista-lab/ai-agent-assistant)

---

## 🚀 Status do Projeto

🚧 **Em desenvolvimento ativo** - Novas funcionalidades sendo adicionadas regularmente!

---

<div align="center">

**Se este projeto foi útil, deixe uma ⭐ estrela!**

</div>
