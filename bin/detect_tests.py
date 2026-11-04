#!/usr/bin/env python
"""Print the GitHub Actions test matrix for a git range, or for all profiles without one."""

import json
import subprocess
import sys
from pathlib import Path

from cchecker import pipeline_includes, registered_profiles

# Registered, but CI cannot write to its private S3 work directory
UNTESTABLE_PROFILES = {"czbiohub_aws"}


def pipeline_tests(pipeline, pipelines, name=None):
    """Return the tests for one included config of a pipeline, or for all its profiles without a name."""
    included = pipelines.get(pipeline, [])
    profiles = {profile for profile, path in included if Path(path).name == name}
    if name is None or None in profiles:
        profiles = {profile for profile, _ in included if profile}
    return {(profile, pipeline) for profile in profiles}


def tests_for_file(path, profiles, pipelines):
    match path.split("/"):
        case ["conf", "pipeline", pipeline, name]:
            return pipeline_tests(pipeline, pipelines, Path(name).stem)
        case ["pipeline", name]:
            return pipeline_tests(Path(name).stem, pipelines)
        case ["conf", name, *_] if Path(name).stem in profiles:
            return {(Path(name).stem, "")}
    return set()


def select_tests(changed, profiles, pipelines):
    """Map changed files to (profile, pipeline) tests; pipeline is empty for a plain profile test."""
    if changed is None:
        tests = {(profile, "") for profile in profiles}
    else:
        tests = set().union(
            *(tests_for_file(path, profiles, pipelines) for path in changed)
        )
    return sorted(test for test in tests if test[0] not in UNTESTABLE_PROFILES)


def changed_files(git_range):
    diff = ["git", "diff", "--name-only", git_range]
    return subprocess.check_output(diff, text=True).splitlines()


if __name__ == "__main__":
    changed = changed_files(sys.argv[1]) if sys.argv[1:] else None
    tests = select_tests(changed, registered_profiles(), pipeline_includes())
    print(
        "tests="
        + json.dumps(
            [{"profile": profile, "pipeline": pipeline} for profile, pipeline in tests]
        )
    )
