import pytest

from typing import cast

from core.job_store.job_store_types import JobStoreType

from core.job_store.inmemory_job_store import InMemoryJobStore

from core.common.exceptions import UnsupportedJobStoreTypeError

from core.job_store.job_store_factory import JobStoreFactory


def test_create_job_store_inmemory_success():
    store = JobStoreFactory.create_job_store(job_store_type=JobStoreType.InMemory)
    assert isinstance(store, InMemoryJobStore)


def test_create_job_store_unsupported_type_raises_exception():
    invalid_type = cast(JobStoreType, "INVALID_TYPE_REPRESENTATION")

    with pytest.raises(UnsupportedJobStoreTypeError) as exc_info:
        JobStoreFactory.create_job_store(job_store_type=invalid_type)
    assert invalid_type in str(exc_info.value)
