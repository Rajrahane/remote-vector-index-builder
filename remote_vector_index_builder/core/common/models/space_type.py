# Copyright OpenSearch Contributors
# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.

from enum import Enum
from dataclasses import dataclass


@dataclass
class SpaceType(Enum):
    L2 = "l2"
    COSINESIMIL = "cosinesimil"
    L1 = "l1"
    LINF = "linf"
    INNERPRODUCT = "innerproduct"
    HAMMING = "hamming"
