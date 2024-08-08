# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: router_worker_crud_ops.py
DESCRIPTION:
    These samples demonstrates how to create Workers used in ACS JobRouter.
    You need a valid connection string to an Azure Communication Service to execute the sample

USAGE:
    python router_worker_crud_ops.py
    Set the environment variables with your own values before running the sample:
    1) AZURE_COMMUNICATION_SERVICE_CONNECTION_STRING - Communication Service connection string
"""

import os


class RouterWorkerSamples(object):
    connection_string = os.environ["AZURE_COMMUNICATION_SERVICE_CONNECTION_STRING"]

    _worker_id = "sample_worker"
    _distribution_policy_id = "sample_dp_policy"

    def setup_distribution_policy(self):
        connection_string = self.connection_string
        distribution_policy_id = self._distribution_policy_id

        from azure.communication.jobrouter import JobRouterAdministrationClient
        from azure.communication.jobrouter.models import LongestIdleMode, DistributionPolicy

        router_admin_client = JobRouterAdministrationClient.from_connection_string(conn_str=connection_string)
        distribution_policy = router_admin_client.upsert_distribution_policy(
            distribution_policy_id,
            DistributionPolicy(
                offer_expires_after_seconds=10 * 60,
                mode=LongestIdleMode(min_concurrent_offers=1, max_concurrent_offers=1),
            ),
        )
        print(f"Sample setup completed: Created distribution policy")

    def setup_queues(self):
        connection_string = self.connection_string
        distribution_policy_id = self._distribution_policy_id

        from azure.communication.jobrouter import JobRouterAdministrationClient
        from azure.communication.jobrouter.models import RouterQueue

        router_admin_client = JobRouterAdministrationClient.from_connection_string(conn_str=connection_string)
        job_queue1: RouterQueue = router_admin_client.upsert_queue(
            "worker-q-1",
            RouterQueue(
                distribution_policy_id=distribution_policy_id,
            ),
        )

        job_queue2: RouterQueue = router_admin_client.upsert_queue(
            "worker-q-2",
            RouterQueue(
                distribution_policy_id=distribution_policy_id,
            ),
        )

        job_queue3: RouterQueue = router_admin_client.upsert_queue(
            "worker-q-3",
            RouterQueue(
                distribution_policy_id=distribution_policy_id,
            ),
        )

        print(f"Sample setup completed: Created queues")

    def create_worker(self):
        connection_string = self.connection_string
        worker_id = self._worker_id
        # [START create_worker]
        from azure.communication.jobrouter import (
            JobRouterClient,
        )
        from azure.communication.jobrouter.models import (
            RouterWorker,
            RouterChannel,
        )

        # set `connection_string` to an existing ACS endpoint
        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)
        print("JobRouterClient created successfully!")

        router_worker: RouterWorker = router_client.upsert_worker(
            worker_id,
            RouterWorker(
                capacity=100,
                queues=["worker-q-1", "worker-q-2"],
                channels=[
                    RouterChannel(channel_id="WebChat", capacity_cost_per_job=1),
                    RouterChannel(channel_id="WebChatEscalated", capacity_cost_per_job=20),
                    RouterChannel(channel_id="Voip", capacity_cost_per_job=100),
                ],
                labels={"Location": "NA", "English": 7, "O365": True, "Xbox_Support": False},
                tags={"Name": "John Doe", "Department": "IT_HelpDesk"},
            ),
        )

        print(f"Router worker successfully created with id: {router_worker.id}")

        # [END create_worker]

    def create_worker_w_limit_concurrent_offers(self):
        connection_string = self.endpoint
        worker_id = self._worker_id
        # [START create_worker_w_limit_concurrent_offers]
        from azure.communication.jobrouter import (
            JobRouterClient,
        )
        from azure.communication.jobrouter.models import (
            RouterWorker,
            RouterChannel,
        )

        # set `connection_string` to an existing ACS endpoint
        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)
        print("JobRouterClient created successfully!")

        router_worker: RouterWorker = router_client.upsert_worker(
            worker_id,
            RouterWorker(
                capacity=100,
                queues=["worker-q-1", "worker-q-2"],
                channels=[
                    RouterChannel(channel_id="WebChat", capacity_cost_per_job=1),
                    RouterChannel(channel_id="WebChatEscalated", capacity_cost_per_job=20),
                    RouterChannel(channel_id="Voip", capacity_cost_per_job=100),
                ],
                labels={"Location": "NA", "English": 7, "O365": True, "Xbox_Support": False},
                tags={"Name": "John Doe", "Department": "IT_HelpDesk"},
                max_concurrent_offers=1,
            ),
        )

        print(f"Router worker successfully created with id: {router_worker.id}")

        # [END create_worker_w_limit_concurrent_offers]

    def update_worker(self):
        connection_string = self.connection_string
        worker_id = self._worker_id
        # [START update_worker]
        from azure.communication.jobrouter import (
            JobRouterClient,
        )
        from azure.communication.jobrouter.models import (
            RouterWorker,
            RouterChannel,
        )

        # set `connection_string` to an existing ACS endpoint
        router_client: JobRouterClient = JobRouterClient.from_connection_string(conn_str=connection_string)
        print("JobRouterClient created successfully!")

        # we are going to
        # 1. Assign the worker to another queue
        # 2. Modify an value of label: `O365`
        # 3. Delete label: `Xbox_Support`
        # 4. Add a new label: `Xbox_Support_EN` and set value true
        # 5. Increase capacityCostPerJob for channel `WebChatEscalated` to 50

        updated_router_worker: RouterWorker = router_client.upsert_worker(
            worker_id,
            queues=["worker-q-3"],
            channels=[RouterChannel(channel_id="WebChatEscalated", capacity_cost_per_job=50)],
            labels={"O365": "Supported", "Xbox_Support": None, "Xbox_Support_EN": True},
        )

        print(f"Router worker successfully update with labels {updated_router_worker.labels}")
        # [END update_worker]

    def get_worker(self):
        connection_string = self.connection_string
        worker_id = self._worker_id
        # [START get_worker]
        from azure.communication.jobrouter import JobRouterClient

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        router_worker = router_client.get_worker(worker_id=worker_id)

        print(f"Successfully fetched router worker with id: {router_worker.id}")
        # [END get_worker]

    def register_worker(self):
        connection_string = self.connection_string
        worker_id = self._worker_id
        # [START register_worker]
        from azure.communication.jobrouter import JobRouterClient

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        router_worker = router_client.upsert_worker(worker_id, available_for_offers=True)

        print(f"Successfully registered router worker with id: {router_worker.id} with status: {router_worker.state}")
        # [END register_worker]

    def deregister_worker(self):
        connection_string = self.connection_string
        worker_id = self._worker_id
        # [START deregister_worker]
        from azure.communication.jobrouter import JobRouterClient

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        router_worker = router_client.upsert_worker(worker_id, available_for_offers=False)

        print(
            f"Successfully de-registered router worker with id: {router_worker.id} with status: {router_worker.state}"
        )
        # [END deregister_worker]

    def list_workers(self):
        connection_string = self.connection_string
        # [START list_workers]
        from azure.communication.jobrouter import JobRouterClient

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        router_worker_iterator = router_client.list_workers()

        for w in router_worker_iterator:
            print(f"Retrieved worker with id: {w.id}")

        print(f"Successfully completed fetching workers")
        # [END list_workers]

    def list_workers_batched(self):
        connection_string = self.connection_string
        # [START list_workers_batched]
        from azure.communication.jobrouter import JobRouterClient

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        router_worker_iterator = router_client.list_workers(results_per_page=10)

        for worker_page in router_worker_iterator.by_page():
            workers_in_page = list(worker_page)
            print(f"Retrieved {len(workers_in_page)} workers in current page")

            for w in workers_in_page:
                print(f"Retrieved worker with id: {w.id}")

        print(f"Successfully completed fetching workers")
        # [END list_workers_batched]

    def clean_up(self):
        connection_string = self.connection_string
        worker_id = self._worker_id

        # [START delete_worker]
        from azure.communication.jobrouter import JobRouterClient

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        router_client.delete_worker(worker_id=worker_id)

        # [END delete_worker]


if __name__ == "__main__":
    sample = RouterWorkerSamples()
    sample.setup_distribution_policy()
    sample.setup_queues()
    sample.create_worker()
    sample.create_worker_w_limit_concurrent_offers()
    sample.update_worker()
    sample.get_worker()
    sample.register_worker()
    sample.deregister_worker()
    sample.list_workers()
    sample.list_workers_batched()
    sample.clean_up()
