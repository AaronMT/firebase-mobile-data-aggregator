#! /usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import argparse
import sys
from enum import Enum

from firebase import ExecutionOutcome, FirebaseHelper

PROJECTS = [
    'moz-fenix',
    'moz-focus-android',
    'moz-reference-browser',
    'moz-android-components'
]

FILTER_NAME_PACKAGE = [
    'org.mozilla.fenix.debug',
    'org.mozilla.fenix',
    'org.mozilla.focus.debug',
    'org.mozilla.focus.nightly'
]


class AndroidTest(Enum):
    ANDROID_INSTRUMENTATION_TEST = 'androidInstrumentationTest'
    ANDROID_ROBO_TEST = 'androidRoboTest'


def parse_args(cmdln_args):
    parser = argparse.ArgumentParser(
        description="Query Firebase Cloud ToolResults API for execution data"
    )

    parser.add_argument(
        "--project",
        help="Indicate project",
        required=True,
        choices=PROJECTS
    )

    parser.add_argument(
        "--filter-by-name",
        help="Indicate filter by name",
        required=True,
        choices=FILTER_NAME_PACKAGE
    )

    return parser.parse_args(args=cmdln_args)


def main():
    args = parse_args(sys.argv[1:])

    FirebaseHelperClient = FirebaseHelper(args.project, args.filter_by_name)
    # FirebaseHelperClient.print_test_results_by_execution_summary(
    #     execution_outcome_summary=ExecutionOutcome.FAILURE.value
    # )
    # FirebaseHelperClient.print_recent_execution_times_by_execution_summary(
    #     execution_outcome_summary=ExecutionOutcome.SUCCESS.value,
    #     specification=AndroidTest.ANDROID_INSTRUMENTATION_TEST.value
    # )
    # FirebaseHelperClient.print_recent_execution_times_by_execution_summary(
    #     execution_outcome_summary=ExecutionOutcome.SUCCESS.value,
    #     specification=AndroidTest.ANDROID_ROBO_TEST.value
    # )
    FirebaseHelperClient.print_test_results_by_execution_summary(
        execution_outcome_summary=ExecutionOutcome.SUCCESS.value
    )
    # FirebaseHelperClient.post_recent_step_count_by_execution_summary(
    #     execution_outcome_summary=ExecutionOutcome.SUCCESS.value
    # )
    # # FirebaseHelperClient.get_executions_from_past_day_by_execution_summary(
    # #     ExecutionOutcome.SUCCESS.value)
    # FirebaseHelperClient.get_pending_executions(specification=AndroidTest.ANDROID_INSTRUMENTATION_TEST.value)


if __name__ == '__main__':
    main()
