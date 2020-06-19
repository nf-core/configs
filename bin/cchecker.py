#!/usr/bin/env python
"""
Script to check correct setup for nf-core/config profiles
"""
import argparse
import os
import re
import sys
import yaml

# PARSE ARGUMENTS
argParser = argparse.ArgumentParser(description='Check the GitHub Actions CI tests all profiles')
argParser.add_argument(
    '--nextflow_config',
    default='nfcore_custom.config',
    help="Input nfcore_custom.config"
)
argParser.add_argument(
    '--github_config',
    default='.github/workflows/main.yml',
    help="Input Github Actions YAML"
)
args = argParser.parse_args()

# MAIN FUNCTION
def check_config(nf_config, gh_workflow):

    # Pull profile names from nextflow config file
    config_profiles = set()
    with open(nf_config, 'r') as cfg:
        for line in cfg:
            match = re.search('(\S+)\s*\{\s*includeConfig', line)
            if match:
                config_profiles.add(match.group(1))

    # Check GitHub Actions workflow file
    ci_tests = ['czbiohub_aws'] # Ignore these profiles
    with open(gh_workflow, 'r') as ghfile:
        gha_wf = yaml.safe_load(ghfile)
        ci_tests.extend(gha_wf['jobs']['profile_test']['strategy']['matrix']['profile'])

    # Check for profiles missing in GitHub Actions
    for p in config_profiles:
        if p not in ci_tests:
            sys.exit("Profile '{}' missing from GitHub Actions tests".format(p))

    # Check for profiles in GitHub Actions that shouldn't be there
    for p in ci_tests:
        if p not in config_profiles:
            sys.exit("Unexpected profile '{}' found in GitHub Actions tests".format(p))

    print("{} profiles found in Nextflow config and GitHub Actions linting matched".format(len(config_profiles)))

# Run if the script is called on the command line only
if __name__ == "__main__":
    check_config(nf_config=args.nextflow_config, gh_workflow=args.github_config)
