#!/usr/bin/env python
"""Print the test matrix for the changes since the merge base with a base ref."""

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


def profile_tests(profile, pipelines):
    """Return the test of a profile and of each pipeline config it owns."""
    owned = {
        pipeline
        for pipeline, included in pipelines.items()
        if profile in {owner for owner, _ in included}
    }
    return {(profile, pipeline) for pipeline in owned | {""}}


def tests_for_file(path, profiles, pipelines):
    match path.split("/"):
        case ["conf", "pipeline", pipeline, name]:
            return pipeline_tests(pipeline, pipelines, Path(name).stem)
        case ["pipeline", name]:
            return pipeline_tests(Path(name).stem, pipelines)
        case ["conf", name, *_] if Path(name).stem in profiles:
            return profile_tests(Path(name).stem, pipelines)
    return set()


def select_tests(changed, profiles, pipelines):
    """Map changed files to (profile, pipeline) tests; pipeline is empty for a plain profile test."""
    tests = set().union(
        *(tests_for_file(path, profiles, pipelines) for path in changed)
    )
    return sorted(test for test in tests if test[0] not in UNTESTABLE_PROFILES)


def job_matrix(tests):
    """Group sorted (profile, pipeline) tests into one job per profile, with space-separated pipelines."""
    pipelines = {}
    for profile, pipeline in tests:
        pipelines.setdefault(profile, []).append(pipeline)
    return [
        {"profile": profile, "pipelines": " ".join(names).strip()}
        for profile, names in pipelines.items()
    ]


def changed_files(base):
    diff = ["git", "diff", "--name-only", f"{base}...HEAD"]
    return subprocess.check_output(diff, text=True).splitlines()


if __name__ == "__main__":
    tests = select_tests(
        changed_files(sys.argv[1]), registered_profiles(), pipeline_includes()
    )
    print(json.dumps(job_matrix(tests)))
