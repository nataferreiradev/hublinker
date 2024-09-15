# hublinker/cli.py
import click
import os
from .github_api.repos.private_repos import PrivateRepos 
from .github_api.repos.public_repos import PublicRepos
from .utils.config import ConfigManager
from .github_api.api_limit.api_limit import ApiLimit

@click.group()
def main():
    """hublinker: A CLI tool for interacting with the GitHub API directly from the terminal, making listings, cloning, and more easy"""

@main.command()
def limit():
    """List your request limit"""
    apiLimit = ApiLimit()
    apiLimit.check_rate_limit()


@main.group()
def repos():
    """Commands related to repositories"""

@repos.command()
@click.option('--user', prompt="GitHub username", help='Some GitHub username')
def public(user):
    """List public repos from some user."""
    if user == '':
        print('User not defined or configured')
    repos =  PublicRepos(user)
    repos.list_repos()

@repos.command()
def private():
    """List your private repositories"""
    repos =  PrivateRepos()
    repos.list_repos()

@main.group()
def config():
    """Configuration commands"""

@config.command()
@click.option('--token',prompt="your token",help='Set your GitHub token')
def set_token(token):
    """Set your token to make more requests"""
    ConfigManager.set_token(token)
    click.echo('token set')

@config.command()
@click.option('--rows',prompt="rows", type=int ,help='rows in page')
def set_rows_page(rows):
    configManager = ConfigManager()
    configManager.set('rows', rows)
    click.echo(f'rows set to: {rows}')

@config.command()
@click.option('--path',prompt="path",help='clone_path')
def set_clone_path(path):
    if not os.path.isdir(path):  # Verifica se é um diretório válido
        click.echo('Error: The specified path does not exist or is not a directory.')
        return
    configManager = ConfigManager()
    configManager.set('clone_path', path)
    click.echo(f'Clone path set to: {path}')

if __name__ == '__main__':
    main()
