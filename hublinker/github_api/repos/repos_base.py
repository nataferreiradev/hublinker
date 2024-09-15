import subprocess
import os
from rich.console import Console
from rich.table import Table
from ..base_github_request import BaseRequest
from ...utils.config import ConfigManager
from ..api_limit.api_limit import ApiLimit,RepositoryType

class ReposBase:
    def __init__(self,path):
        self.base_request = BaseRequest(path)
        self.console = Console()
        self.configManager = ConfigManager()
        rows = self.configManager.get_int('rows',5)
        self.per_page = rows if isinstance(rows, int)  else 5
        self.data = []  
        self.total_repos = 0

    def fetch_repos(self):
        try:
            response = self.base_request.make_request_get('Fetching repos...')
            return response.json()
        except Exception as e:
            self.console.print(f'[red]{e}[/red]')
            return None


    def list_repos(self, page=1):

        if not self.data:  
            apiLimit = ApiLimit()
            if not apiLimit.is_resource_under_limit(RepositoryType.CORE):
                self.console.print('[red]You reach your limit[/red]')
                return

            self.data = self.fetch_repos()
            if self.data is None:
                return
            self.total_repos = len(self.data)

        if self.total_repos <= 0:
            self.console.print("No data available to display.")
            return

        total_pages = (self.total_repos + self.per_page - 1) // self.per_page

        if page < 1 or page > total_pages:
            print(f"Page {page} is out of range. Please enter a page between 1 and {total_pages}.")
            return

        start_index = (page - 1) * self.per_page
        end_index = min(start_index + self.per_page, self.total_repos)
        page_data = self.data[start_index:end_index]

        table = Table(title=f"Repositories Page {page}/{total_pages}")

        table.add_column("No.", style="bold")
        table.add_column("Repository", style="bold")

        for i, repo in enumerate(page_data, start=start_index + 1):
            if(repo['private'] == True):
                table.add_row(str(i), f'[blue]{repo['name']}[/blue]')
                continue
            table.add_row(str(i), repo['name'])
            

        self.console.clear()
        self.console.print(table)
        self.options(page)
    
    def options(self, current_page):
        while True:
            print("\nOptions: [n] Next page | [p] Previous page | [q] Quit | [c] Clone repository")
            choice = input("Enter your choice: ").strip().lower()

            if choice == 'n':
                if current_page < (self.total_repos + self.per_page - 1) // self.per_page:
                    current_page += 1
                    self.list_repos(current_page)
                    break
                else:
                    print("You are already on the last page.")
            elif choice == 'p':
                if current_page > 1:
                    current_page -= 1
                    self.list_repos(current_page)
                    break
                else:
                    print("You are already on the first page.")
            elif choice == 'c':
                self.clone_repo()
            elif choice == 'q':
                break
            else:
                self.console.print("[red]Invalid choice[/red]")

    def clone_repo(self):
        repo_index = int(input("Enter the number of the repository to clone: ").strip())
        
        if not 1 <= repo_index <= self.total_repos:
            self.console.print("[red]Invalid repository number.[/red]")
            return

        clone_type = input("Option: [h] HTTP | [s] SSH: ").strip().lower()
        repo_data = self.data[repo_index - 1]
        
        if clone_type == 'h':
            repo_url = repo_data['clone_url']
        elif clone_type == 's':
            repo_url = repo_data['ssh_url']
        else:
            self.console.print("[red] Invalid choice [/red]")
            return
        
        self.console.print(f"Cloning repository from [blue]{repo_url}[/blue]...")
        try:
            clonePath = self.configManager.get('clone_path')
            if not clonePath.strip():
                clonePath = os.getcwd()

            subprocess.run(['git', 'clone', repo_url], cwd = clonePath, check=True)
            print("Repository cloned successfully.")
        except subprocess.CalledProcessError:
            self.console.print("[red]Failed to clone repository.[/red]")