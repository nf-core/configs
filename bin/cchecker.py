#!/usr/bin/env python
"""
Script to check correct setup for nf-core/config profiles
"""
import os
import sys
import argparse
import re

# PARSE ARGUMENTS
argParser = argparse.ArgumentParser(description='Check the GitHub Actions CI tests all profiles')
argParser.add_argument(
    'nextflow_config',
    default='nfcore_custom.config',
    help="Input nfcore_custom.config"
)
argParser.add_argument(
    'github_config',
    default='.github/workflows/main.yml',
    help="Input Github Actions YAML"
)
args = argParser.parse_args()

# MAIN FUNCTION
def check_config(Config, Github):

    # Pull profile names from nextflow config file
    config_profiles = set()
    with open(Config, 'r') as cfg:
        for line in cfg:
            if re.search('includeConfig*', line):
                hit = line.split('/')[-1].split('.')[0]
                config_profiles.add(hit.strip())

    # Check GitHub Actions workflow file
    tests = set()
    ### Ignore these profiles
    ignore_me = ['czbiohub_aws']
    tests.update(ignore_me)
    with open(Github, 'r') as ghfile:
        for line in ghfile:
            if re.search('profile: ', line):
                line = line.replace('\'','').replace('[','').replace(']','').replace('\n','')
                profiles = line.split(':')[1].split(',')
                for p in profiles:
                    tests.add(p.strip())

    ###Check if sets are equal
    if tests == config_profiles:
        sys.exit(0)
    else:
        #Maybe report what is missing here too
        print("Tests don't seem to test these profiles properly. Please check whether you added the profile to the Github Actions testing YAML.\n")
        print(config_profiles.symmetric_difference(tests))
        sys.exit(1)

check_config(Config=args.CUSTOM_CONFIG,Github=args.GITHUB_CONFIG)
