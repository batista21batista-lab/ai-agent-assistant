# Guia Rápido - AI Agent Assistant

## O que é este projeto?

Sistema de IA para automação de desenvolvimento, testes, deploy e documentação de projetos.

## Funcionalidades

- ✍️ **Geração de Código**: Usa IA para gerar código baseado em requisitos
- ✅ **Testes Automáticos**: Executa testes contínuos
- 🚀 **Deploy Automático**: Faz deploy em Netlify
- 📋 **Documentação**: Gera documentação automática
- 📈 **Monitoramento**: Dashboard com métricas em tempo real

## Como Usar

### 1. Clonar o Repositório
```bash
git clone https://github.com/batista21batista-lab/ai-agent-assistant.git
cd ai-agent-assistant
```

### 2. Instalar Dependências
```bash
npm install
# ou
pip install -r requirements.txt
```

### 3. Configurar Token do GitHub
Guarde seu token em um arquivo `.env`:
```
GITHUB_TOKEN=seu_token_aqui
```

### 4. Executar o Agente
```bash
npm start
# ou
python main.py
```

## Estrutura do Projeto

```
.
├── config/          # Arquivos de configuração
├── docs/            # Documentação
├── src/             # Código-fonte
├── tests/           # Testes
├── .gitignore       # Arquivos ignorados
├── LICENSE          # Licença MIT
├── package.json     # Dependências Node
├── README.md        # Este arquivo
```

## Próximos Passos

1. Conectar com Netlify
2. Configurar Google Sheets para monitoramento
3. Adicionar workflows N8N/Make
4. Integrar com APIs externas

## Suporte

Para dúvidas ou problemas, abra uma **Issue** no GitHub.
