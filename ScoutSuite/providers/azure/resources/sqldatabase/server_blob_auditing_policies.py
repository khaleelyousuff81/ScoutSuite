from ScoutSuite.providers.azure.facade.base import AzureFacade
from ScoutSuite.providers.azure.resources.base import AzureResources


class ServerBlobAuditingPolicies(AzureResources):
    def __init__(self, facade: AzureFacade, resource_group_name: str, server_name: str):
        self.resource_group_name = resource_group_name
        self.server_name = server_name

        super(ServerBlobAuditingPolicies, self).__init__(facade)

    async def fetch_all(self):
        policies = await self.facade.sqldatabase.get_server_blob_auditing_policies(
            self.resource_group_name, self.server_name)
        self._parse_policies(policies)

    def _parse_policies(self, policies):
        self.update({
            'auditing_enabled': policies.state == "Enabled",
            'retention_days': policies.retention_days
        })
