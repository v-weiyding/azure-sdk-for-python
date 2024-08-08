# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.appcontainers.aio import ContainerAppsAPIClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestContainerAppsAPIContainerAppsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ContainerAppsAPIClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_subscription(self, resource_group):
        response = self.client.container_apps.list_by_subscription(
            api_version="2024-03-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_resource_group(self, resource_group):
        response = self.client.container_apps.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-03-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.container_apps.get(
            resource_group_name=resource_group.name,
            container_app_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.container_apps.begin_create_or_update(
                resource_group_name=resource_group.name,
                container_app_name="str",
                container_app_envelope={
                    "location": "str",
                    "configuration": {
                        "activeRevisionsMode": "Single",
                        "dapr": {
                            "appId": "str",
                            "appPort": 0,
                            "appProtocol": "http",
                            "enableApiLogging": bool,
                            "enabled": False,
                            "httpMaxRequestSize": 0,
                            "httpReadBufferSize": 0,
                            "logLevel": "str",
                        },
                        "ingress": {
                            "additionalPortMappings": [{"external": bool, "targetPort": 0, "exposedPort": 0}],
                            "allowInsecure": False,
                            "clientCertificateMode": "str",
                            "corsPolicy": {
                                "allowedOrigins": ["str"],
                                "allowCredentials": bool,
                                "allowedHeaders": ["str"],
                                "allowedMethods": ["str"],
                                "exposeHeaders": ["str"],
                                "maxAge": 0,
                            },
                            "customDomains": [{"name": "str", "bindingType": "str", "certificateId": "str"}],
                            "exposedPort": 0,
                            "external": False,
                            "fqdn": "str",
                            "ipSecurityRestrictions": [
                                {"action": "str", "ipAddressRange": "str", "name": "str", "description": "str"}
                            ],
                            "stickySessions": {"affinity": "str"},
                            "targetPort": 0,
                            "traffic": [{"label": "str", "latestRevision": False, "revisionName": "str", "weight": 0}],
                            "transport": "auto",
                        },
                        "maxInactiveRevisions": 0,
                        "registries": [
                            {"identity": "str", "passwordSecretRef": "str", "server": "str", "username": "str"}
                        ],
                        "secrets": [{"identity": "str", "keyVaultUrl": "str", "name": "str", "value": "str"}],
                        "service": {"type": "str"},
                    },
                    "customDomainVerificationId": "str",
                    "environmentId": "str",
                    "eventStreamEndpoint": "str",
                    "extendedLocation": {"name": "str", "type": "str"},
                    "id": "str",
                    "identity": {
                        "type": "str",
                        "principalId": "str",
                        "tenantId": "str",
                        "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                    },
                    "latestReadyRevisionName": "str",
                    "latestRevisionFqdn": "str",
                    "latestRevisionName": "str",
                    "managedBy": "str",
                    "managedEnvironmentId": "str",
                    "name": "str",
                    "outboundIpAddresses": ["str"],
                    "provisioningState": "str",
                    "systemData": {
                        "createdAt": "2020-02-20 00:00:00",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20 00:00:00",
                        "lastModifiedBy": "str",
                        "lastModifiedByType": "str",
                    },
                    "tags": {"str": "str"},
                    "template": {
                        "containers": [
                            {
                                "args": ["str"],
                                "command": ["str"],
                                "env": [{"name": "str", "secretRef": "str", "value": "str"}],
                                "image": "str",
                                "name": "str",
                                "probes": [
                                    {
                                        "failureThreshold": 0,
                                        "httpGet": {
                                            "port": 0,
                                            "host": "str",
                                            "httpHeaders": [{"name": "str", "value": "str"}],
                                            "path": "str",
                                            "scheme": "str",
                                        },
                                        "initialDelaySeconds": 0,
                                        "periodSeconds": 0,
                                        "successThreshold": 0,
                                        "tcpSocket": {"port": 0, "host": "str"},
                                        "terminationGracePeriodSeconds": 0,
                                        "timeoutSeconds": 0,
                                        "type": "str",
                                    }
                                ],
                                "resources": {"cpu": 0.0, "ephemeralStorage": "str", "memory": "str"},
                                "volumeMounts": [{"mountPath": "str", "subPath": "str", "volumeName": "str"}],
                            }
                        ],
                        "initContainers": [
                            {
                                "args": ["str"],
                                "command": ["str"],
                                "env": [{"name": "str", "secretRef": "str", "value": "str"}],
                                "image": "str",
                                "name": "str",
                                "resources": {"cpu": 0.0, "ephemeralStorage": "str", "memory": "str"},
                                "volumeMounts": [{"mountPath": "str", "subPath": "str", "volumeName": "str"}],
                            }
                        ],
                        "revisionSuffix": "str",
                        "scale": {
                            "maxReplicas": 10,
                            "minReplicas": 0,
                            "rules": [
                                {
                                    "azureQueue": {
                                        "auth": [{"secretRef": "str", "triggerParameter": "str"}],
                                        "queueLength": 0,
                                        "queueName": "str",
                                    },
                                    "custom": {
                                        "auth": [{"secretRef": "str", "triggerParameter": "str"}],
                                        "metadata": {"str": "str"},
                                        "type": "str",
                                    },
                                    "http": {
                                        "auth": [{"secretRef": "str", "triggerParameter": "str"}],
                                        "metadata": {"str": "str"},
                                    },
                                    "name": "str",
                                    "tcp": {
                                        "auth": [{"secretRef": "str", "triggerParameter": "str"}],
                                        "metadata": {"str": "str"},
                                    },
                                }
                            ],
                        },
                        "serviceBinds": [{"name": "str", "serviceId": "str"}],
                        "terminationGracePeriodSeconds": 0,
                        "volumes": [
                            {
                                "mountOptions": "str",
                                "name": "str",
                                "secrets": [{"path": "str", "secretRef": "str"}],
                                "storageName": "str",
                                "storageType": "str",
                            }
                        ],
                    },
                    "type": "str",
                    "workloadProfileName": "str",
                },
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.container_apps.begin_delete(
                resource_group_name=resource_group.name,
                container_app_name="str",
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_update(self, resource_group):
        response = await (
            await self.client.container_apps.begin_update(
                resource_group_name=resource_group.name,
                container_app_name="str",
                container_app_envelope={
                    "location": "str",
                    "configuration": {
                        "activeRevisionsMode": "Single",
                        "dapr": {
                            "appId": "str",
                            "appPort": 0,
                            "appProtocol": "http",
                            "enableApiLogging": bool,
                            "enabled": False,
                            "httpMaxRequestSize": 0,
                            "httpReadBufferSize": 0,
                            "logLevel": "str",
                        },
                        "ingress": {
                            "additionalPortMappings": [{"external": bool, "targetPort": 0, "exposedPort": 0}],
                            "allowInsecure": False,
                            "clientCertificateMode": "str",
                            "corsPolicy": {
                                "allowedOrigins": ["str"],
                                "allowCredentials": bool,
                                "allowedHeaders": ["str"],
                                "allowedMethods": ["str"],
                                "exposeHeaders": ["str"],
                                "maxAge": 0,
                            },
                            "customDomains": [{"name": "str", "bindingType": "str", "certificateId": "str"}],
                            "exposedPort": 0,
                            "external": False,
                            "fqdn": "str",
                            "ipSecurityRestrictions": [
                                {"action": "str", "ipAddressRange": "str", "name": "str", "description": "str"}
                            ],
                            "stickySessions": {"affinity": "str"},
                            "targetPort": 0,
                            "traffic": [{"label": "str", "latestRevision": False, "revisionName": "str", "weight": 0}],
                            "transport": "auto",
                        },
                        "maxInactiveRevisions": 0,
                        "registries": [
                            {"identity": "str", "passwordSecretRef": "str", "server": "str", "username": "str"}
                        ],
                        "secrets": [{"identity": "str", "keyVaultUrl": "str", "name": "str", "value": "str"}],
                        "service": {"type": "str"},
                    },
                    "customDomainVerificationId": "str",
                    "environmentId": "str",
                    "eventStreamEndpoint": "str",
                    "extendedLocation": {"name": "str", "type": "str"},
                    "id": "str",
                    "identity": {
                        "type": "str",
                        "principalId": "str",
                        "tenantId": "str",
                        "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                    },
                    "latestReadyRevisionName": "str",
                    "latestRevisionFqdn": "str",
                    "latestRevisionName": "str",
                    "managedBy": "str",
                    "managedEnvironmentId": "str",
                    "name": "str",
                    "outboundIpAddresses": ["str"],
                    "provisioningState": "str",
                    "systemData": {
                        "createdAt": "2020-02-20 00:00:00",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20 00:00:00",
                        "lastModifiedBy": "str",
                        "lastModifiedByType": "str",
                    },
                    "tags": {"str": "str"},
                    "template": {
                        "containers": [
                            {
                                "args": ["str"],
                                "command": ["str"],
                                "env": [{"name": "str", "secretRef": "str", "value": "str"}],
                                "image": "str",
                                "name": "str",
                                "probes": [
                                    {
                                        "failureThreshold": 0,
                                        "httpGet": {
                                            "port": 0,
                                            "host": "str",
                                            "httpHeaders": [{"name": "str", "value": "str"}],
                                            "path": "str",
                                            "scheme": "str",
                                        },
                                        "initialDelaySeconds": 0,
                                        "periodSeconds": 0,
                                        "successThreshold": 0,
                                        "tcpSocket": {"port": 0, "host": "str"},
                                        "terminationGracePeriodSeconds": 0,
                                        "timeoutSeconds": 0,
                                        "type": "str",
                                    }
                                ],
                                "resources": {"cpu": 0.0, "ephemeralStorage": "str", "memory": "str"},
                                "volumeMounts": [{"mountPath": "str", "subPath": "str", "volumeName": "str"}],
                            }
                        ],
                        "initContainers": [
                            {
                                "args": ["str"],
                                "command": ["str"],
                                "env": [{"name": "str", "secretRef": "str", "value": "str"}],
                                "image": "str",
                                "name": "str",
                                "resources": {"cpu": 0.0, "ephemeralStorage": "str", "memory": "str"},
                                "volumeMounts": [{"mountPath": "str", "subPath": "str", "volumeName": "str"}],
                            }
                        ],
                        "revisionSuffix": "str",
                        "scale": {
                            "maxReplicas": 10,
                            "minReplicas": 0,
                            "rules": [
                                {
                                    "azureQueue": {
                                        "auth": [{"secretRef": "str", "triggerParameter": "str"}],
                                        "queueLength": 0,
                                        "queueName": "str",
                                    },
                                    "custom": {
                                        "auth": [{"secretRef": "str", "triggerParameter": "str"}],
                                        "metadata": {"str": "str"},
                                        "type": "str",
                                    },
                                    "http": {
                                        "auth": [{"secretRef": "str", "triggerParameter": "str"}],
                                        "metadata": {"str": "str"},
                                    },
                                    "name": "str",
                                    "tcp": {
                                        "auth": [{"secretRef": "str", "triggerParameter": "str"}],
                                        "metadata": {"str": "str"},
                                    },
                                }
                            ],
                        },
                        "serviceBinds": [{"name": "str", "serviceId": "str"}],
                        "terminationGracePeriodSeconds": 0,
                        "volumes": [
                            {
                                "mountOptions": "str",
                                "name": "str",
                                "secrets": [{"path": "str", "secretRef": "str"}],
                                "storageName": "str",
                                "storageType": "str",
                            }
                        ],
                    },
                    "type": "str",
                    "workloadProfileName": "str",
                },
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_custom_host_name_analysis(self, resource_group):
        response = await self.client.container_apps.list_custom_host_name_analysis(
            resource_group_name=resource_group.name,
            container_app_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_secrets(self, resource_group):
        response = await self.client.container_apps.list_secrets(
            resource_group_name=resource_group.name,
            container_app_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get_auth_token(self, resource_group):
        response = await self.client.container_apps.get_auth_token(
            resource_group_name=resource_group.name,
            container_app_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_start(self, resource_group):
        response = await (
            await self.client.container_apps.begin_start(
                resource_group_name=resource_group.name,
                container_app_name="str",
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_stop(self, resource_group):
        response = await (
            await self.client.container_apps.begin_stop(
                resource_group_name=resource_group.name,
                container_app_name="str",
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
