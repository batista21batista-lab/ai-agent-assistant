"""GitHub Integration Client

Módulo para integração com a API do GitHub.
Permite criar repositórios, commits, pull requests, etc.
"""

import os
from github import Github, GithubException
import logging

logger = logging.getLogger(__name__)

class GitHubClient:
    """
    Cliente para interagir com a API do GitHub
    """
    
    def __init__(self, token=None):
        """
        Inicializa o cliente GitHub
        
        Args:
            token (str): Token de acesso pessoal do GitHub
        """
        self.token = token or os.getenv('GITHUB_TOKEN')
        if not self.token:
            raise ValueError("❌ GITHUB_TOKEN não encontrado")
        
        try:
            self.client = Github(self.token)
            self.user = self.client.get_user()
            logger.info(f"✅ Conectado ao GitHub como: {self.user.login}")
        except GithubException as e:
            logger.error(f"❌ Erro ao conectar ao GitHub: {e}")
            raise
    
    def get_repository(self, repo_name):
        """
        Obtém um repositório pelo nome
        
        Args:
            repo_name (str): Nome do repositório (formato: owner/repo)
        
        Returns:
            Repository: Objeto do repositório
        """
        try:
            repo = self.client.get_repo(repo_name)
            logger.info(f"✅ Repositório encontrado: {repo.full_name}")
            return repo
        except GithubException as e:
            logger.error(f"❌ Erro ao buscar repositório: {e}")
            return None
    
    def create_repository(self, name, description="", private=False):
        """
        Cria um novo repositório
        
        Args:
            name (str): Nome do repositório
            description (str): Descrição
            private (bool): Se deve ser privado
        
        Returns:
            Repository: Repositório criado
        """
        try:
            repo = self.user.create_repo(
                name=name,
                description=description,
                private=private,
                auto_init=True
            )
            logger.info(f"✅ Repositório criado: {repo.full_name}")
            return repo
        except GithubException as e:
            logger.error(f"❌ Erro ao criar repositório: {e}")
            return None
    
    def create_file(self, repo_name, file_path, content, commit_message):
        """
        Cria ou atualiza um arquivo no repositório
        
        Args:
            repo_name (str): Nome do repositório
            file_path (str): Caminho do arquivo
            content (str): Conteúdo do arquivo
            commit_message (str): Mensagem do commit
        
        Returns:
            bool: True se sucesso
        """
        try:
            repo = self.get_repository(repo_name)
            if not repo:
                return False
            
            try:
                # Tentar atualizar arquivo existente
                contents = repo.get_contents(file_path)
                repo.update_file(
                    path=file_path,
                    message=commit_message,
                    content=content,
                    sha=contents.sha
                )
                logger.info(f"✅ Arquivo atualizado: {file_path}")
            except:
                # Criar novo arquivo
                repo.create_file(
                    path=file_path,
                    message=commit_message,
                    content=content
                )
                logger.info(f"✅ Arquivo criado: {file_path}")
            
            return True
        except GithubException as e:
            logger.error(f"❌ Erro ao criar/atualizar arquivo: {e}")
            return False
    
    def create_pull_request(self, repo_name, title, body, head, base="main"):
        """
        Cria um pull request
        
        Args:
            repo_name (str): Nome do repositório
            title (str): Título do PR
            body (str): Descrição
            head (str): Branch de origem
            base (str): Branch de destino
        
        Returns:
            PullRequest: Pull request criado
        """
        try:
            repo = self.get_repository(repo_name)
            if not repo:
                return None
            
            pr = repo.create_pull(
                title=title,
                body=body,
                head=head,
                base=base
            )
            logger.info(f"✅ Pull request criado: #{pr.number}")
            return pr
        except GithubException as e:
            logger.error(f"❌ Erro ao criar pull request: {e}")
            return None
    
    def get_issues(self, repo_name, state="open"):
        """
        Lista issues do repositório
        
        Args:
            repo_name (str): Nome do repositório
            state (str): Estado (open, closed, all)
        
        Returns:
            list: Lista de issues
        """
        try:
            repo = self.get_repository(repo_name)
            if not repo:
                return []
            
            issues = repo.get_issues(state=state)
            logger.info(f"✅ {issues.totalCount} issues encontradas")
            return list(issues)
        except GithubException as e:
            logger.error(f"❌ Erro ao listar issues: {e}")
            return []
    
    def create_issue(self, repo_name, title, body="", labels=None):
        """
        Cria uma nova issue
        
        Args:
            repo_name (str): Nome do repositório
            title (str): Título da issue
            body (str): Descrição
            labels (list): Lista de labels
        
        Returns:
            Issue: Issue criada
        """
        try:
            repo = self.get_repository(repo_name)
            if not repo:
                return None
            
            issue = repo.create_issue(
                title=title,
                body=body,
                labels=labels or []
            )
            logger.info(f"✅ Issue criada: #{issue.number}")
            return issue
        except GithubException as e:
            logger.error(f"❌ Erro ao criar issue: {e}")
            return None

if __name__ == "__main__":
    # Teste do cliente
    try:
        client = GitHubClient()
        print(f"✨ Cliente GitHub inicializado com sucesso!")
        print(f"👤 Usuário: {client.user.login}")
    except Exception as e:
        print(f"❌ Erro: {e}")
