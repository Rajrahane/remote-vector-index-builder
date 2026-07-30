from abc import abstractmethod, ABC
from typing import Optional

from core.common.models.job.JobMetadata import JobMetadata


class JobStore(ABC):
    @abstractmethod
    def create_job(self, job: JobMetadata) -> bool:
        pass

    @abstractmethod
    def get_job(self, job_id: str) -> Optional[JobMetadata]:
        pass
