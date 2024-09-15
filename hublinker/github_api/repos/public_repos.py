from .repos_base import ReposBase

class PublicRepos(ReposBase):
    def __init__(self,userName):
        super().__init__(f'users/{userName}/repos')

if __name__ == '__main__':
    publicRepos = PublicRepos('nataferreiradev')
    publicRepos.list_repos()