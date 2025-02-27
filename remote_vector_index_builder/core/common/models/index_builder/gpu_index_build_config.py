# Copyright OpenSearch Contributors
# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.

from dataclasses import dataclass

from remote_vector_index_builder.core.common.models.space_type import SpaceType

from .gpu_index_cagra_config import GPUIndexCagraConfig
from .index_hnsw_cagra_config import IndexHNSWCagraConfig


@dataclass
class GPUIndexBuildConfig:
    index_hnsw_cagra_config: IndexHNSWCagraConfig = IndexHNSWCagraConfig()
    gpu_index_cagra_config: GPUIndexCagraConfig = GPUIndexCagraConfig()

    # type of metric the gpuIndex is created with
    metric: SpaceType = SpaceType.L2
