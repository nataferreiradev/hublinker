from ..utils.config import ConfigManager
import requests
from rich.console import Console

class BaseRequest:
    def __init__(self,path) -> None:
        self.url = "https://api.github.com/"
        self.resquestUrl = self.url+path
        token = ConfigManager.get_token()
        self.header = {}
        if token and token.strip(): 
            self.header = {'Authorization': f'Bearer {token}'}

    def make_request_get(self,fetch_msg: str):
      console = Console()
      with console.status(f"[bold green] {fetch_msg} [/]", spinner="dots"):
        response = requests.get(self.resquestUrl, headers=self.header)
        BaseRequest.handle_status_codes(response.status_code)
        return response

    def handle_status_codes(code):
      if code == 200:
        return
      elif code == 401:
         raise NotAuthorized()
      elif code == 403:
        raise LimitExeeded()
      else:
        raise UnexpectedCode()
    

class NotAuthorized(Exception):
  def __init__(self):
    super().__init__()
    
  def __str__(self):
    return f"Not authorized (verify your token)"

class UnexpectedCode(Exception):
  def __init__(self):
    super().__init__()
    
  def __str__(self):
    return f"Unexpected Code"

class LimitExeeded(Exception):
  def __init__(self):
    super().__init__()
    
  def __str__(self):
    return f"Limit exeeded"