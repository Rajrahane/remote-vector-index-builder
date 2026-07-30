from typing import Optional, Any, Dict

from core.job_store.dynamodb_job_store import DynamoDBJobStore
from core.job_store.inmemory_job_store import InMemoryJobStore
from core.job_store.job_store_types import JobStoreType
from core.job_store.job_store import JobStore

from core.common.exceptions import UnsupportedJobStoreTypeError


class JobStoreFactory:
    @staticmethod
    def create_job_store(job_store_type: JobStoreType, config_dict: Optional[Dict[str, Any]] = None) -> JobStore:
        config_dict = config_dict or {}

        if job_store_type == JobStoreType.InMemory:
            return InMemoryJobStore()

        elif job_store_type == JobStoreType.DynamoDB:
            table_name = config_dict.get("table_name", "vector_index_jobs")

            return DynamoDBJobStore(table_name=table_name, client_config=config_dict)
        else:
            raise UnsupportedJobStoreTypeError(
                f"Unsupported JobStore type specified: {job_store_type}"
            )
