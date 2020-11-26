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
