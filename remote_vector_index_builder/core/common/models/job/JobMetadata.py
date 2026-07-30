from typing import Optional

from core.common.models.job.JobStatus import JobStatus

from core.common.models import IndexBuildParameters
from pydantic import BaseModel


class JobMetadata(BaseModel):
    id: str
    status: JobStatus
    request_parameters: IndexBuildParameters
    file_name: Optional[str] = None
    error_message: Optional[str] = None

    @property
    def is_terminated(self) -> bool:
        return self.status in (JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.TIMEOUT)
