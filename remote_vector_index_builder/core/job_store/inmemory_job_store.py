from typing import Dict, Optional

from core.job_store.job_store import JobStore

from core.common.models.job.JobMetadata import JobMetadata


class InMemoryJobStore(JobStore):
    def __init__(self):
        self._db: Dict[str, JobMetadata] = {}

    def create_job(self, job: JobMetadata) -> bool:
        self._db[job.id] = job
        return True

    def get_job(self, job_id: str) -> Optional[JobMetadata]:
        return self._db.get(job_id)
