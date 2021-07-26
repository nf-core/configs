#!/usr/bin/env python

#######################################################################
#######################################################################
## Created on November 26 to check pipeline configs for nf-core/configs
#######################################################################
#######################################################################

import os
import sys
import argparse
import re
import yaml

############################################
############################################
## PARSE ARGUMENTS
############################################
############################################

Description = 'Double check custom config file and github actions file to test all cases'
Epilog = """Example usage: python cchecker.py <nfcore_custom.config> <github_actions_file>"""

argParser = argparse.ArgumentParser(description=Description, epilog=Epilog)
## REQUIRED PARAMETERS
argParser.add_argument('CUSTOM_CONFIG', help="Input nfcore_custom.config.")
argParser.add_argument('GITHUB_CONFIG', help="Input Github Actions YAML")

args = argParser.parse_args()

############################################
############################################
## MAIN FUNCTION
############################################
############################################

def check_config(Config, Github):

    regex = 'includeConfig*'
    ERROR_STR = 'ERROR: Please check config file! Did you really update the profiles?'

    ## CHECK Config First
    config_profiles = set()
    with open(Config, 'r') as cfg:
        for line in cfg:
            if re.search(regex, line):
                hit = line.split('/')[2].split('.')[0]
                config_profiles.add(hit.strip())

    ### Check Github Config now
    tests = set()
    ### Ignore these profiles
    ignore_me = ['czbiohub_aws']
    tests.update(ignore_me)
    # parse yaml GitHub actions file
    try:
        with open(Github, 'r') as ghfile:
            wf = yaml.safe_load(ghfile)
            profile_list = wf["jobs"]["profile_test"]["strategy"]["matrix"]["profile"]
    except Exception as e:
        print("Could not parse yaml file: {}, {}".format(Github, e))
        sys.exit(1)
    # Add profiles to test
    for profile in profile_list:
        tests.add(profile.strip())

    ###Check if sets are equal
    try:
        assert tests == config_profiles
    except (AssertionError):
        print("Tests don't seem to test these profiles properly. Please check whether you added the profile to the Github Actions testing YAML.\n")
        print(config_profiles.symmetric_difference(tests))
        sys.exit(1)

check_config(Config=args.CUSTOM_CONFIG,Github=args.GITHUB_CONFIG)
