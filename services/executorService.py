import os
from services.impl.pingExecutorService import PingExecutorService
from services.impl.mockExecutorService import MockExecutorService

IMPL = os.environ.get("ExecutorService", "PingExecutorService")


class ExecutorService(object):

    @classmethod
    def get_instance(cls):
        if os.environ.get("DEMO_MODE", "disable") == "disable":
            return MockExecutorService()
        if IMPL == "PingExecutorService":
            return PingExecutorService()
        if IMPL == "MockExecutorService":
            return MockExecutorService()
