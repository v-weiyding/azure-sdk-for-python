# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.appcontainers import ContainerAppsAPIClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestContainerAppsAPIContainerAppsSourceControlsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ContainerAppsAPIClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_container_app(self, resource_group):
        response = self.client.container_apps_source_controls.list_by_container_app(
            resource_group_name=resource_group.name,
            container_app_name="str",
            api_version="2024-03-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.container_apps_source_controls.get(
            resource_group_name=resource_group.name,
            container_app_name="str",
            source_control_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.container_apps_source_controls.begin_create_or_update(
            resource_group_name=resource_group.name,
            container_app_name="str",
            source_control_name="str",
            source_control_envelope={
                "branch": "str",
                "githubActionConfiguration": {
                    "azureCredentials": {
                        "clientId": "str",
                        "clientSecret": "str",
                        "kind": "str",
                        "subscriptionId": "str",
                        "tenantId": "str",
                    },
                    "contextPath": "str",
                    "githubPersonalAccessToken": "str",
                    "image": "str",
                    "os": "str",
                    "publishType": "str",
                    "registryInfo": {"registryPassword": "str", "registryUrl": "str", "registryUserName": "str"},
                    "runtimeStack": "str",
                    "runtimeVersion": "str",
                },
                "id": "str",
                "name": "str",
                "operationState": "str",
                "repoUrl": "str",
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.container_apps_source_controls.begin_delete(
            resource_group_name=resource_group.name,
            container_app_name="str",
            source_control_name="str",
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
