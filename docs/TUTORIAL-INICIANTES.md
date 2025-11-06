# 🎓 TUTORIAL COMPLETO PARA INICIANTES - AI Agent Assistant

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Pré-requisitos](#pré-requisitos)
3. [Passo 1: Obter Tokens das APIs](#passo-1-obter-tokens-das-apis)
4. [Passo 2: Instalar no Computador](#passo-2-instalar-no-computador)
5. [Passo 3: Configurar Netlify](#passo-3-configurar-netlify)
6. [Passo 4: Usar o Agente](#passo-4-usar-o-agente)
7. [Solução de Problemas](#solução-de-problemas)

---

## 🎯 Visão Geral

Este tutorial vai te ensinar, **passo-a-passo**, como configurar e usar seu AI Agent Assistant mesmo sem conhecimento técnico.

**O que você vai conseguir fazer:**
- ✅ Automatizar geração de código
- ✅ Executar testes automaticamente
- ✅ Fazer deploy de projetos com 1 comando
- ✅ Gerar documentação automática
- ✅ Monitorar métricas em tempo real

**Tempo estimado:** 30 minutos

---

## 📦 Pré-requisitos

Antes de começar, você precisa ter instalado no seu computador:

### Windows:
1. **Python 3.8+** - [Baixar aqui](https://www.python.org/downloads/)
   - Durante instalação, marque ☑️ "Add Python to PATH"
2. **Git** - [Baixar aqui](https://git-scm.com/download/win)
3. **Editor de texto** - VS Code [Baixar aqui](https://code.visualstudio.com/)

### Mac/Linux:
```bash
# Instalar Python
sudo apt install python3 python3-pip  # Ubuntu/Debian
brew install python3  # Mac

# Instalar Git
sudo apt install git  # Ubuntu/Debian
brew install git  # Mac
```

### Contas Online (gratuitas):
- ☑️ Conta no GitHub - [Criar aqui](https://github.com/join)
- ☑️ Conta no Netlify - [Criar aqui](https://app.netlify.com/signup)
- ☐ Conta OpenAI (opcional) - [Criar aqui](https://platform.openai.com/signup)

---

## 🔑 PASSO 1: Obter Tokens das APIs

Esta é a etapa mais importante! Vou te guiar passo-a-passo em cada tela.

### 1.1 Token do GitHub (OBRIGATÓRIO)

**O que é:** Um "token" é como uma senha especial que permite o agente acessar seu GitHub.

**Como obter (5 minutos):**

1. **Acesse:** https://github.com/settings/tokens
2. **Clique** no botão verde “Generate new token”
3. **Escolha:** "Generate new token (classic)"
4. **Preencha:**
   - Note: `AI Agent Assistant`
   - Expiration: `No expiration` (ou escolha um período)
5. **Marque estas caixas:**
   - ☑️ `repo` (todas as subcaixas)
   - ☑️ `workflow`
   - ☑️ `write:packages`
6. **Role até o fim** da página e clique em **"Generate token"**
7. **IMPORTANTE:** Copie o token que começa com `ghp_` e guarde em local seguro
   - ⚠️ Só aparece UMA VEZ! Se perder, precisa criar outro.

**Exemplo do token:**
```
ghp_1A2b3C4d5E6f7G8h9I0jK1L2M3N4O5P6Q7R8
```

---

### 1.2 Token do Netlify (OBRIGATÓRIO)

**O que é:** Permite o agente fazer deploy automático dos seus projetos.

**Como obter (3 minutos):**

1. **Acesse:** https://app.netlify.com/user/applications
2. **Clique** em "New access token"
3. **Preencha:**
   - Description: `AI Agent Assistant`
4. **Clique** em "Generate token"
5. **Copie** o token e guarde

**Exemplo do token:**
```
nfp_1234567890abcdefghijklmnopqrstuvwxyz123456789012
```

---

### 1.3 Chave OpenAI (OPCIONAL)

**O que é:** Permite usar IA para gerar código automaticamente.

**Custo:** Pago por uso (aproximadamente $0.002 por 1000 tokens)

**Como obter (5 minutos):**

1. **Acesse:** https://platform.openai.com/api-keys
2. **Crie conta** se não tiver
3. **Clique** em "Create new secret key"
4. **Preencha:**
   - Name: `AI Agent Assistant`
5. **Clique** em "Create secret key"
6. **Copie** a chave que começa com `sk-`

**Exemplo da chave:**
```
sk-proj-1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJK
```

⚠️ **ATENÇÃO:** Nunca compartilhe seus tokens ou chaves com ninguém!

---

## 💻 PASSO 2: Instalar no Computador

Agora vamos baixar e configurar o projeto no seu computador.

### 2.1 Clonar o Repositório

**No Windows:**
1. Abra o "Prompt de Comando" ou "PowerShell"
   - Pressione `Windows + R`
   - Digite `cmd` e pressione Enter
2. Navegue até a pasta onde quer instalar:
   ```cmd
   cd C:\Users\SeuNome\Documents
   ```
3. Clone o repositório:
   ```cmd
   git clone https://github.com/batista21batista-lab/ai-agent-assistant.git
   cd ai-agent-assistant
   ```

**No Mac/Linux:**
```bash
cd ~/Documents
git clone https://github.com/batista21batista-lab/ai-agent-assistant.git
cd ai-agent-assistant
```

---

### 2.2 Criar Ambiente Virtual

**O que é:** Um "ambiente virtual" isola as dependências do projeto.

**Windows:**
```cmd
python -m venv venv
venv\\Scripts\\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

✅ **Sucesso:** Você verá `(venv)` no início da linha do terminal.

---

### 2.3 Instalar Dependências

```bash
pip install -r requirements.txt
```

⏳ **Aguarde:** Pode levar 2-5 minutos para instalar tudo.

---

### 2.4 Configurar Arquivo .env

1. **Copie o arquivo de exemplo:**
   ```bash
   cp .env.example .env
   ```

2. **Abra o arquivo `.env` no editor de texto**
   - Windows: `notepad .env`
   - Mac: `open -e .env`
   - Linux: `nano .env`

3. **Cole seus tokens** que você copiou no Passo 1:
   ```env
   GITHUB_TOKEN=ghp_seu_token_aqui
   NETLIFY_TOKEN=nfp_seu_token_aqui
   OPENAI_API_KEY=sk-proj-sua_chave_aqui
   
   AGENT_NAME=AI-Agent-Assistant
   AGENT_VERSION=1.0.0
   LOG_LEVEL=INFO
   
   DEPLOY_ENVIRONMENT=production
   AUTO_DEPLOY=true
   ```

4. **Salve o arquivo** (Ctrl+S no Windows, Cmd+S no Mac)

---

## 🚀 PASSO 3: Configurar Netlify

### 3.1 Conectar Repositório ao Netlify

1. **Acesse:** https://app.netlify.com/start
2. **Clique** em "Import from Git"
3. **Escolha** "GitHub"
4. **Autorize** o Netlify a acessar seu GitHub (se solicitado)
5. **Procure** por `ai-agent-assistant` na lista de repositórios
6. **Clique** no repositório
7. **Configurações de Build:**
   - Branch: `main`
   - Build command: (deixe vazio)
   - Publish directory: (deixe vazio)
8. **Clique** em "Deploy site"

⏳ **Aguarde:** O primeiro deploy pode levar 2-3 minutos.

✅ **Sucesso:** Você verá uma URL tipo: `https://seu-projeto-123abc.netlify.app`

---

## 🎮 PASSO 4: Usar o Agente

### 4.1 Executar o Agente

No terminal (com o ambiente virtual ativado):

```bash
python src/main.py
```

### 4.2 Comandos Disponíveis

**Gerar Código:**
```bash
python src/main.py generate --type=web --framework=react
```

**Executar Testes:**
```bash
python src/main.py test --all
```

**Fazer Deploy:**
```bash
python src/main.py deploy --env=production
```

**Gerar Documentação:**
```bash
python src/main.py docs --format=markdown
```

**Ver Ajuda:**
```bash
python src/main.py --help
```

---

## 🔧 Solução de Problemas

### Erro: "Python não reconhecido"

**Solução:**
- Reinstale o Python marcando "Add Python to PATH"
- Ou use: `python3` em vez de `python`

### Erro: "Módulo não encontrado"

**Solução:**
```bash
pip install -r requirements.txt --upgrade
```

### Erro: "Token inválido"

**Solução:**
1. Verifique se copiou o token completo
2. Certifique-se que não há espaços antes/depois
3. Gere um novo token se necessário

### Erro: "Permission denied"

**Solução (Mac/Linux):**
```bash
chmod +x src/main.py
```

### Netlify não conecta com GitHub

**Solução:**
1. Revogue as permissões antigas: https://github.com/settings/applications
2. Tente conectar novamente no Netlify

---

## 🎉 Próximos Passos

Agora que você configurou tudo:

1. ✅ Explore os comandos do agente
2. ✅ Leia a [Documentação Completa](IMPLEMENTACAO-COMPLETA.md)
3. ✅ Configure [Google Sheets](https://sheets.google.com) para relatórios
4. ✅ Crie workflows personalizados
5. ✅ Junte-se à comunidade no GitHub Discussions

---

## 📞 Suporte

Precisa de ajuda?

- 🐛 **Issues:** [GitHub Issues](https://github.com/batista21batista-lab/ai-agent-assistant/issues)
- 💬 **Discussões:** [GitHub Discussions](https://github.com/batista21batista-lab/ai-agent-assistant/discussions)
- 📧 **Email:** batista21batista@gmail.com

---

**🌟 Se este tutorial foi útil, deixe uma estrela no repositório!**

[⭐ Star no GitHub](https://github.com/batista21batista-lab/ai-agent-assistant)
