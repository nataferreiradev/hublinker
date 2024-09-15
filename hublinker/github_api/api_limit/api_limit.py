import datetime
from enum import Enum
from rich.console import Console
from rich.table import Table
from ..base_github_request import BaseRequest
from ...utils.config import ConfigManager


class RepositoryType(Enum):
    CORE = "core"
    GRAPHQL = "graphql"
    INTEGRATION_MANIFEST = "integration_manifest"
    SEARCH = "search"
    
    @classmethod
    def list_values(cls):
        return [member.value for member in cls]

class ApiLimit:
    def __init__(self) -> None:
        super().__init__()
        self.baseRequest = BaseRequest('rate_limit')
     
    def check_rate_limit(self):
        try:
            response = self.baseRequest.make_request_get('fetching data...')
        except Exception as e:
            print(e)
            return
        console = Console()
        
        data = response.json()
        resources = data.get('resources', {})

        table = Table(title="Rate Limit Status")
        table.add_column("Resource", style="bold")
        table.add_column("Limit", style="bold")
        table.add_column("Remaining", style="bold")
        table.add_column("Reset Time", style="bold")
        table.add_column("Used", style="bold")

        for resource_name, resource_data in resources.items():
            limit = resource_data.get('limit', 'Unknown')
            remaining = resource_data.get('remaining', 'Unknown')
            reset_epoch = resource_data.get('reset', 'Unknown')
            used = resource_data.get('used', 'Unknown')

            if reset_epoch != 'Unknown':
                reset_time = datetime.datetime.fromtimestamp(reset_epoch)
            else:
                reset_time = 'Unknown'

            table.add_row(
                resource_name.capitalize(),
                str(limit),
                str(remaining),
                str(reset_time),
                str(used)
            )

        console.clear()
        console.print(table)

    def is_resource_under_limit(self,resource: RepositoryType) -> bool:
        configManager = ConfigManager()

        try:
            response = self.baseRequest.make_request_get('Cheking resource limit...')
        except Exception as e:
            print(e)
            return
        
        data = response.json()
        resources = data.get('resources', {})
        resource_core_data = resources.get(resource.value,{})

        request_limit = configManager.get_int('git_hub_request_limit')
        if not request_limit:
            request_limit = 10
        
        remaining = resource_core_data.get('remaining', 'Unknown')

        return remaining > request_limit
        

