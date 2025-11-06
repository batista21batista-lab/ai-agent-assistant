#!/usr/bin/env python3
"""
AI Agent Assistant - Sistema de Automação Completo
Autor: batista21batista-lab
Versão: 1.0.0
"""

import os
import sys
from dotenv import load_dotenv
import logging

# Carregar variáveis de ambiente
load_dotenv()

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('agent.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

class AIAgent:
    """
    Classe principal do agente de IA para automação de desenvolvimento
    """
    
    def __init__(self):
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.netlify_token = os.getenv('NETLIFY_TOKEN')
        self.openai_key = os.getenv('OPENAI_API_KEY')
        logger.info("✅ AI Agent iniciado com sucesso!")
    
    def run(self):
        """
        Método principal de execução do agente
        """
        logger.info("🚀 Iniciando AI Agent Assistant...")
        
        # Verificar configurações
        if not self.github_token:
            logger.warning("⚠️ GITHUB_TOKEN não configurado")
        
        if not self.netlify_token:
            logger.warning("⚠️ NETLIFY_TOKEN não configurado")
        
        if not self.openai_key:
            logger.warning("⚠️ OPENAI_API_KEY não configurado")
        
        logger.info("✨ Agente pronto para receber comandos!")
        logger.info("📚 Use 'python src/main.py --help' para ver comandos disponíveis")

if __name__ == "__main__":
    try:
        agent = AIAgent()
        agent.run()
    except KeyboardInterrupt:
        logger.info("\n🛑 Agente interrompido pelo usuário")
        sys.exit(0)
    except Exception as e:
        logger.error(f"❌ Erro ao executar agente: {e}")
        sys.exit(1)
