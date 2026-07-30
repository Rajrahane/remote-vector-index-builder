from typing import Dict, Any, Optional

from core.job_store.job_store import JobStore
from core.common.models.aws_config import AWSConfig
from core.common.models.job.JobMetadata import JobMetadata


class DynamoDBJobStore(JobStore):
    def __init__(self, table_name: str, client_config: Dict[str, Any]):
        aws_config: AWSConfig = client_config.get("s3_client_config")
        self.dynamodb_resource = aws_config.create_resource("dynamodb")
        self.table = self.dynamodb_resource.Table(table_name)

    def create_job(self, job: JobMetadata) -> bool:
        self.table.put_item(Item=job.model_dump(exclude_none=True))
        return True

    def get_job(self, job_id: str) -> Optional[JobMetadata]:
        response = self.table.get_item(Key={"id": job_id})
        item = response.get("Item")
        if not item:
            return None
        return JobMetadata(**item)
