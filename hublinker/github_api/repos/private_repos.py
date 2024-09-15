from .repos_base import ReposBase

class PrivateRepos(ReposBase):
    def __init__(self):
        super().__init__(f'user/repos')
        self.base_request.header['visibility'] = 'all'

if __name__ == '__main__':
    privateRepos = PrivateRepos()
    privateRepos.list_repos()