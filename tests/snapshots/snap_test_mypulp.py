# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_sample 1'] = 1

snapshots['test_sample 2'] = 30.0

snapshots['test_sample 3'] = [
    (
        'x1',
        0.0
    ),
    (
        'x2',
        0.0
    ),
    (
        'x3',
        1.0
    ),
    (
        'x_1',
        1.0
    )
]

snapshots['test_sample 4'] = [
    (
        'c_1',
        30.0
    ),
    (
        'c_2',
        -0.0
    ),
    (
        'c_3',
        -0.0
    ),
    (
        'c_4',
        -0.0
    ),
    (
        'c_5',
        -0.0
    )
]

snapshots['test_option 1'] = 6491.707815518645
